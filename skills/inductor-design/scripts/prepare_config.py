#!/usr/bin/env python3
"""Преобразовать минимальное ТЗ в полный design_config.json проекта."""
from __future__ import annotations

import argparse
import copy
import json
import sys
from pathlib import Path
from typing import Any, Dict

from jsonschema import Draft202012Validator


SCRIPT_ROOT = Path(__file__).resolve().parent
SKILL_ROOT = SCRIPT_ROOT.parent
SCHEMA_PATH = SKILL_ROOT / "references" / "tz-input.schema.json"
TEMPLATE_CONFIG = (
    SKILL_ROOT / "assets" / "project_template" / "2_input_files"
    / "design_config.json"
)


def load_json(path: Path) -> Dict[str, Any]:
    with path.open(encoding="utf-8") as stream:
        return json.load(stream)


def validate_minimal_tz(data: Dict[str, Any]) -> Dict[str, Any]:
    """Проверить структуру и физическую непротиворечивость минимального ТЗ."""

    schema = load_json(SCHEMA_PATH)
    errors = sorted(
        Draft202012Validator(schema).iter_errors(data),
        key=lambda item: tuple(str(part) for part in item.absolute_path),
    )
    if errors:
        rows = []
        for error in errors:
            location = ".".join(str(part) for part in error.absolute_path) or "<root>"
            rows.append(f"{location}: {error.message}")
        raise ValueError("ошибки структуры ТЗ:\n- " + "\n- ".join(rows))

    u_in = float(data["u_in_nom_V"])
    u_out = float(data["u_out_nom_V"])
    if u_in >= u_out:
        raise ValueError(
            "для boost в режиме CCM требуется u_in_nom_V < u_out_nom_V"
        )
    if data.get("ambient_temperature_C", 40.0) >= data.get(
        "core_temperature_max_C", 100.0
    ):
        raise ValueError(
            "ambient_temperature_C должна быть меньше core_temperature_max_C"
        )
    if data.get("ambient_temperature_C", 40.0) >= data.get(
        "winding_temperature_max_C", 100.0
    ):
        raise ValueError(
            "ambient_temperature_C должна быть меньше winding_temperature_max_C"
        )

    search = data.get("search", {})
    n_min = int(search.get("parallel_conductors_min", 1))
    n_max = int(search.get("parallel_conductors_max", 12))
    if n_min > n_max:
        raise ValueError(
            "search.parallel_conductors_min не может превышать "
            "search.parallel_conductors_max"
        )

    tolerance = float(data.get("load_consistency_tolerance", 0.01))
    power_from_current = u_out * float(data.get("i_out_A", 0.0))
    supplied_power = float(data.get("p_out_W", 0.0))
    if supplied_power > 0.0 and power_from_current > 0.0:
        relative_error = abs(supplied_power - power_from_current) / max(
            supplied_power, power_from_current
        )
        if relative_error > tolerance:
            raise ValueError(
                "противоречие нагрузки: p_out_W отличается от "
                f"u_out_nom_V·i_out_A на {relative_error * 100.0:.3f} %; "
                "удалите вторую величину либо увеличьте "
                "load_consistency_tolerance осознанно"
            )
    return copy.deepcopy(data)


def resolve_load(data: Dict[str, Any]) -> tuple[float, float]:
    """Вернуть согласованные выходную мощность и ток."""

    u_out = float(data["u_out_nom_V"])
    if data["load_definition"] == "output_power":
        power = float(data["p_out_W"])
        current = power / u_out
    else:
        current = float(data["i_out_A"])
        power = u_out * current
    return power, current


def build_design_config(data: Dict[str, Any], base: Dict[str, Any]) -> Dict[str, Any]:
    """Сформировать полный конфигурационный снимок расчёта."""

    data = validate_minimal_tz(data)
    config = copy.deepcopy(base)
    topology = data["topology"]
    power, current = resolve_load(data)

    config["project"]["name"] = data["project_name"]
    config["project"]["load_definition"] = data["load_definition"]
    config["single"]["enabled"] = topology in ("single", "both")
    config["interleaved"]["enabled"] = topology in ("interleaved", "both")

    common = {
        "u_in_nom": float(data["u_in_nom_V"]),
        "u_out_nom": float(data["u_out_nom_V"]),
        "i_out_nom": current,
        "p_out_nom": power,
        "eta": float(data["eta"]),
        "ripple_u_in": float(data.get("input_voltage_ripple_ratio", 0.10)),
        "ripple_u_out": float(data.get("output_voltage_ripple_ratio", 0.10)),
        "r_i": float(data["current_ripple_ratio"]),
        "f_sw_list": sorted(float(value) for value in data["switching_frequencies_Hz"]),
        "tol_u_in": float(data.get("input_voltage_tolerance", 0.05)),
        "tol_i_load": float(data.get("load_tolerance", 0.10)),
        "tol_L": float(data.get("inductance_tolerance", 0.10)),
        "t_amb": float(data.get("ambient_temperature_C", 40.0)),
        "t_core_max": float(data.get("core_temperature_max_C", 100.0)),
        "t_wind_max": float(data.get("winding_temperature_max_C", 100.0)),
    }
    config["single"]["tz"].update(common)
    config["interleaved"]["tz"].update(common)

    phase = data.get("interleaved", {})
    config["interleaved"]["tz"]["n_phases"] = int(phase.get("n_phases", 3))
    config["interleaved"]["tz"]["tol_i_share"] = float(
        phase.get("current_sharing_tolerance", 0.02)
    )

    limits = data.get("limits", {})
    if "current_density_prelim_A_mm2" in limits:
        value = float(limits["current_density_prelim_A_mm2"]) * 1.0e6
        config["single"]["tz"]["j_prelim"] = value
        config["interleaved"]["tz"]["j_dop"] = value
    if "current_density_max_A_mm2" in limits:
        value = float(limits["current_density_max_A_mm2"]) * 1.0e6
        config["single"]["tz"]["j_final_max"] = value
        config["interleaved"]["tz"]["j_final_max"] = value
    for source, target in (
        ("copper_fill_max", "k_cu_dop"),
        ("window_fill_max", "k_zan_dop"),
        ("B_utilization_prelim", "k_B_prelim"),
        ("B_utilization_final", "k_B"),
    ):
        if source in limits:
            value = float(limits[source])
            config["single"]["tz"][target] = value
            config["interleaved"]["tz"][target] = value

    search = config.setdefault("search", {})
    search.update(
        {
            "parallel_conductors_min": 1,
            "parallel_conductors_max": 12,
            "inductance_upper_factor": 2.5,
            "exhaustive_core_search": True,
            "record_rejection_counts": True,
        }
    )
    supplied_search = data.get("search", {})
    for key in (
        "parallel_conductors_min",
        "parallel_conductors_max",
        "inductance_upper_factor",
        "exhaustive_core_search",
        "record_rejection_counts",
    ):
        if key in supplied_search:
            search[key] = supplied_search[key]
    if "loss_window_ratio" in supplied_search:
        value = float(supplied_search["loss_window_ratio"])
        config["single"]["tz"]["loss_window"] = value
        config["interleaved"]["tz"]["loss_window"] = value
    if "preferred_core_families" in supplied_search:
        families = list(supplied_search["preferred_core_families"])
        config["single"]["tz"]["preferred_core_families"] = families
        config["interleaved"]["tz"]["preferred_core_families"] = families

    config["input_tz"] = data
    return config


def configure_project(data: Dict[str, Any], project: Path) -> Path:
    """Обновить design_config.json уже созданного проекта."""

    project = project.resolve()
    config_path = project / "2_input_files" / "design_config.json"
    if not config_path.is_file():
        raise FileNotFoundError(f"не найден файл конфигурации проекта: {config_path}")
    config = build_design_config(data, load_json(config_path))
    with config_path.open("w", encoding="utf-8") as stream:
        json.dump(config, stream, ensure_ascii=False, indent=2, allow_nan=False)
        stream.write("\n")
    return config_path


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("tz", type=Path, help="минимальный JSON-файл ТЗ")
    parser.add_argument("project", type=Path, help="созданный проект расчёта")
    args = parser.parse_args()
    data = validate_minimal_tz(load_json(args.tz.resolve()))
    path = configure_project(data, args.project)
    power, current = resolve_load(data)
    print(f"конфигурация сформирована: {path}")
    print(f"принято: P_вых={power:g} Вт; I_вых={current:g} А")


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    main()
