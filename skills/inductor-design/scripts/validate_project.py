#!/usr/bin/env python3
"""Проверить JSON, рисунки и OOXML-отчёты проекта дросселя."""
from __future__ import annotations

import argparse
import json
import os
import re
import zipfile
from pathlib import Path
from xml.etree import ElementTree


SECTIONS = (
    "1 ИСХОДНЫЕ ДАННЫЕ",
    "2 ЭЛЕКТРИЧЕСКИЙ РЕЖИМ",
    "3 ВЫБОР МАГНИТОПРОВОДА",
    "4 РАСЧЁТ ЧИСЛА ВИТКОВ",
    "5 УКЛАДКА ОБМОТКИ",
    "6 ПОТЕРИ",
    "7 СОБСТВЕННАЯ ЁМКОСТЬ",
    "8 ЭЛЕКТРОМАГНИТНАЯ СОВМЕСТИМОСТЬ",
    "9 ЗАПАСЫ",
    "10 СРАВНЕНИЕ",
    "11 ИТОГОВЫЕ ДАННЫЕ",
    "12 ВЫВОДЫ",
    "13 СОСТАВ ОТЧЁТА",
    "СПИСОК ИСПОЛЬЗОВАННЫХ ИСТОЧНИКОВ",
)


def load_json(path: Path):
    with path.open(encoding="utf-8") as stream:
        return json.load(stream)


def fail(condition: bool, message: str) -> None:
    if condition:
        raise AssertionError(message)


def docx_text(path: Path) -> str:
    fail(not path.is_file(), f"не найден отчёт: {path}")
    with zipfile.ZipFile(path) as package:
        names = set(package.namelist())
        fail("[Content_Types].xml" not in names or "word/document.xml" not in names,
             f"неполный OOXML-пакет: {path}")
        root = ElementTree.fromstring(package.read("word/document.xml"))
    return " ".join(node.text or "" for node in root.iter()
                    if node.tag.endswith("}t"))


def validate_runtime_sources(project: Path) -> None:
    for folder in (project / "3_calc", project / "5_interleaved"):
        for path in folder.glob("*.py"):
            text = path.read_text(encoding="utf-8")
            fail(bool(re.search(r"(?i)(drossel1|[/\\]Backup[/\\])", text)),
                 f"runtime-зависимость от старого проекта: {path}")


def validate_comparison(rows, required_pairs: int, label: str) -> None:
    fail(len(rows) < required_pairs,
         f"{label}: неполное сравнение core×material: {len(rows)} < {required_pairs}")
    for row in rows:
        fail(not row.get("reason"),
             f"{label}: отсутствует причина решения для {row.get('core')}/{row.get('material')}")
        if row.get("status") == "rejected" and row.get("nearest_rejected"):
            fail(not row["nearest_rejected"].get("margins"),
                f"{label}: нет численных запасов ближайшего отклонённого варианта")


def validate_rejection_counts(item: dict, label: str) -> None:
    counts = item.get("rejection_counts")
    fail(not isinstance(counts, dict), f"{label}: отсутствует журнал причин отсева")
    for reason, count in counts.items():
        fail(not isinstance(reason, str) or not reason,
             f"{label}: некорректный код причины отсева")
        fail(not isinstance(count, int) or count < 0,
             f"{label}: некорректный счётчик причины {reason}")


def validate_report(path: Path, results: dict) -> None:
    text = docx_text(path)
    upper = text.upper()
    for heading in SECTIONS:
        fail(heading not in upper, f"{path.name}: отсутствует раздел «{heading}»")
    fail("(1)" not in text, f"{path.name}: формулы не имеют сквозной нумерации")
    for key, item in results.items():
        selected = item["selected"]
        for value in (selected["core"]["name"], selected["material"]["name"],
                      str(selected["design"]["N"]),
                      f"{selected['design']['gap_mm']:.3f}".replace(".", ",")):
            fail(value not in text, f"{path.name}: значение {value!r} из {key} не найдено")


def validate_single(project: Path, required_pairs: int) -> None:
    data = load_json(project / "3_calc" / "results_single_gap.json")
    fail(data.get("meta", {}).get("schema_version") != "1.0",
         "single: отсутствует поддерживаемая версия схемы")
    fail("config" not in data.get("meta", {}), "single: отсутствует снимок config")
    fail(data["meta"].get("final_verification") is not False,
         "single: ошибочно присвоен финальный статус")
    fail(not data.get("results"), "single: нет частотных результатов")
    for key, item in data["results"].items():
        fail(item.get("status") != "analytical_solution", f"single {key}: нет решения")
        selected = item["selected"]
        fail(selected["verification"].get("final_verified") is not False,
             f"single {key}: ошибочно присвоен финальный статус")
        fail(selected["design"].get("n_gaps") != 1, f"single {key}: зазор не один")
        if data.get("meta", {}).get("config", {}).get("search", {}).get(
            "record_rejection_counts", False
        ):
            validate_rejection_counts(item, f"single {key}")
        quantities = item["quantities"]
        fail(quantities.get("core_sets") != 1 or quantities.get("core_halves_total") != 2,
             f"single {key}: неверное количество магнитопроводов")
        validate_comparison(item["core_material_table"], required_pairs, f"single {key}")
        for image in (f"winding_{key}.png", f"waveform_{key}.png"):
            fail(not (project / "1_output_files" / "img" / image).is_file(),
                 f"single {key}: отсутствует {image}")
    fail(not (project / "1_output_files" / "img" / "impedance.png").is_file(),
         "single: отсутствует impedance.png")
    validate_report(project / "1_output_files" / "Расчёт_дросселя_boost.docx",
                    data["results"])


def validate_interleaved(project: Path, required_pairs: int) -> None:
    data = load_json(project / "5_interleaved" / "results_interleaved.json")
    fail(data.get("meta", {}).get("schema_version") != "1.0",
         "interleaved: отсутствует поддерживаемая версия схемы")
    fail("config" not in data.get("meta", {}), "interleaved: отсутствует снимок config")
    fail(data["meta"].get("final_verification") is not False,
         "interleaved: ошибочно присвоен финальный статус")
    results = data.get("results", {})
    fail(not results, "interleaved: нет частотных результатов")
    phases = int(data["tz"]["n_phases"])
    for key, item in results.items():
        selected = item["selected"]
        fail(selected["verification"].get("final_verified") is not False,
             f"interleaved {key}: ошибочно присвоен финальный статус")
        fail(selected["design"].get("n_gaps") != 1, f"interleaved {key}: зазор не один")
        if data.get("meta", {}).get("config", {}).get("search", {}).get(
            "record_rejection_counts", False
        ):
            validate_rejection_counts(item.get("enumeration", {}),
                                      f"interleaved {key}")
        quantities = item["quantities"]
        fail(quantities.get("phase_inductors") != phases or
             quantities.get("core_sets_total") != phases or
             quantities.get("core_halves_total") != 2 * phases,
             f"interleaved {key}: неверное количество магнитопроводов")
        validate_comparison(item["core_material_table"], required_pairs,
                            f"interleaved {key}")
        for stem in ("winding", "waveform", "phases"):
            image = project / "1_output_files" / "img_3ph" / f"{stem}_{key}.png"
            fail(not image.is_file(), f"interleaved {key}: отсутствует {image.name}")
    for image in ("ripple_vs_D.png", "impedance.png"):
        fail(not (project / "1_output_files" / "img_3ph" / image).is_file(),
             f"interleaved: отсутствует {image}")
    validate_report(project / "1_output_files" / "Расчёт_дросселя_interleaved.docx",
                    results)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project", type=Path)
    parser.add_argument("--only", choices=("single", "interleaved", "both"), default=None)
    args = parser.parse_args()
    project = args.project.resolve()
    config = load_json(project / "2_input_files" / "design_config.json")
    configured = config.get("knowledge_base_path", "__AUTO__")
    candidates = []
    if configured != "__AUTO__":
        path = Path(configured)
        candidates.append(path if path.is_absolute() else project / path)
    if os.environ.get("INDUCTOR_KNOWLEDGE_BASE"):
        candidates.append(Path(os.environ["INDUCTOR_KNOWLEDGE_BASE"]))
    candidates.extend(parent / "knowledge_base" for parent in (project, *project.parents))
    candidates.extend(parent for parent in (project, *project.parents)
                      if parent.name == "knowledge_base")
    knowledge_base = next((path.resolve() for path in candidates
                           if (path / "components_db" / "cores.json").is_file()), None)
    fail(knowledge_base is None,
         "не найден knowledge_base; задайте knowledge_base_path или INDUCTOR_KNOWLEDGE_BASE")
    cores = load_json(knowledge_base / "components_db" / "cores.json")["cores"]
    materials = load_json(knowledge_base / "components_db" / "ferrite_materials.json")["materials"]
    required_pairs = len(cores) * len(materials)
    validate_runtime_sources(project)

    single = config.get("single", {}).get("enabled", False)
    interleaved = config.get("interleaved", {}).get("enabled", False)
    if args.only:
        single = args.only in ("single", "both")
        interleaved = args.only in ("interleaved", "both")
    if single:
        validate_single(project, required_pairs)
    if interleaved:
        validate_interleaved(project, required_pairs)
    print(f"валидация пройдена: {project}")


if __name__ == "__main__":
    main()
