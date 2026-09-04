# -*- coding: utf-8 -*-
"""Расчёт дросселя фазы многофазного interleaved boost-преобразователя.

Общая физика дросселя находится в ``3_calc/inductor_design.py``. Скрипт
формирует единый JSON для рисунков и отчёта. Итог до повторного МКЭ и
измерений имеет статус ``analytical_preliminary``.
"""
from __future__ import annotations

import json
import math
import os
import sys
from dataclasses import asdict, dataclass
from typing import Dict, List, Optional, Tuple

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(ROOT, "3_calc"))
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

import inductor_design as ind
from inductor_design import Core, Litz, Material, Mode

JSON_PATH = os.path.join(HERE, "results_interleaved.json")


@dataclass
class TZ3:
    """Исходные данные многофазного преобразователя."""

    n_phases: int = 3
    u_in_nom: float = 160.0
    u_out_nom: float = 235.0
    i_out_nom: float = 25.0
    p_out_nom: float = 6000.0
    eta: float = 0.90
    ripple_u_in: float = 0.10
    ripple_u_out: float = 0.10
    r_i: float = 0.10
    f_sw_list: Tuple[float, ...] = (100e3, 150e3)
    tol_u_in: float = 0.05
    tol_i_load: float = 0.10
    tol_L: float = 0.10
    tol_i_share: float = 0.02
    t_amb: float = 40.0
    t_core_max: float = 100.0
    t_wind_max: float = 100.0
    k_B: float = 0.65
    k_B_prelim: float = 0.60
    u_B_num: Optional[float] = None
    k_cu_dop: float = 0.35
    k_zan_dop: float = 0.70
    k_reluctance_min: float = 4.0
    k_f_res: float = 3.0
    M_EMC: float = 6.0
    gap_clearance: float = 5.0e-3
    side_margin_fraction: float = 0.05
    turn_spacing_ratio: float = 0.10
    interlayer_insulation: float = 0.20e-3
    bend_radius_ratio: float = 3.0
    q_fringe: float = 0.90
    k_r_gap: float = 1.0
    r_gap_min: float = 1.0e-3
    n_gaps: int = 1
    f_treb_ratio: float = 5.0
    loss_window: float = 0.02
    r_probe: float = 50.0e-3
    j_dop: float = 2.5e6
    j_final_max: float = 2.5e6
    k_w_prelim: float = 0.20
    preferred_core_families: Tuple[str, ...] = (
        "EQ", "ETD", "PM", "PQ", "RM", "EER")

    @property
    def p_in_nom(self) -> float:
        return self.p_out_nom / self.eta

    @property
    def i_in_nom(self) -> float:
        return self.p_in_nom / self.u_in_nom

    @property
    def p_out_phase(self) -> float:
        return self.p_out_nom / self.n_phases

    def f_treb_max(self, f_sw: float) -> float:
        return self.f_treb_ratio * f_sw

    def phase_tz(self) -> ind.TZ:
        # Наихудшая фаза одновременно несёт перегрузку и небаланс токов.
        tol_combined = (1.0 + self.tol_i_load) * (1.0 + self.tol_i_share) - 1.0
        return ind.TZ(
            u_in_nom=self.u_in_nom, u_out_nom=self.u_out_nom,
            i_out_nom=self.i_out_nom / self.n_phases,
            p_out_nom=self.p_out_nom / self.n_phases,
            eta=self.eta, ripple_u_in=self.ripple_u_in,
            ripple_u_out=self.ripple_u_out, r_i=self.r_i,
            f_sw_list=self.f_sw_list, tol_u_in=self.tol_u_in,
            tol_i_load=tol_combined, tol_L=self.tol_L,
            t_amb=self.t_amb, t_core_max=self.t_core_max,
            t_wind_max=self.t_wind_max, k_B=self.k_B,
            k_B_prelim=self.k_B_prelim, u_B_num=self.u_B_num,
            k_cu_dop=self.k_cu_dop, k_zan_dop=self.k_zan_dop,
            k_reluctance_min=self.k_reluctance_min,
            k_f_res=self.k_f_res, M_EMC=self.M_EMC,
            gap_clearance=self.gap_clearance,
            side_margin_fraction=self.side_margin_fraction,
            turn_spacing_ratio=self.turn_spacing_ratio,
            interlayer_insulation=self.interlayer_insulation,
            bend_radius_ratio=self.bend_radius_ratio,
            q_fringe=self.q_fringe, k_r_gap=self.k_r_gap,
            r_gap_min=self.r_gap_min, n_gaps_list=(self.n_gaps,),
            loss_window=self.loss_window, f_treb_ratio=self.f_treb_ratio,
            k_w_prelim=self.k_w_prelim, j_prelim=self.j_dop,
            j_final_max=self.j_final_max,
            preferred_core_families=self.preferred_core_families,
        )


def load_tz3() -> TZ3:
    """Загрузить ТЗ interleaved-варианта из единого файла проекта."""
    raw = dict(ind.PROJECT_CONFIG.get("interleaved", {}).get("tz", {}))
    for key in ("f_sw_list", "preferred_core_families"):
        if key in raw:
            raw[key] = tuple(raw[key])
    if "preferred_core_families" in raw:
        raw["preferred_core_families"] = tuple(
            family for family in raw["preferred_core_families"]
            if str(family).upper() != "ER"
        )
    allowed = set(TZ3.__dataclass_fields__)
    unknown = sorted(set(raw) - allowed)
    if unknown:
        raise KeyError(f"неизвестные поля interleaved.tz: {', '.join(unknown)}")
    tz = TZ3(**raw)
    if tz.n_phases < 2:
        raise ValueError("interleaved.tz.n_phases должно быть не меньше 2")
    if not 0.0 <= tz.tol_i_share < 1.0:
        raise ValueError("interleaved.tz.tol_i_share должно находиться в диапазоне [0; 1)")
    ind.validate_tz(tz.phase_tz(), "interleaved.tz")
    return tz


def ripple_cancellation_factor(D: float, n_ph: int) -> float:
    """K = ΔI_вх/ΔI_ф для N одинаковых фаз со сдвигом T/N."""

    if not 0.0 < D < 1.0:
        return 1.0
    x = n_ph * D
    m = math.floor(x)
    if abs(x - round(x)) < 1e-12:
        return 0.0
    return (m + 1.0 - x) * (x - m) / (x * (1.0 - D))


def ripple_cancellation_numeric(D: float, n_ph: int, n_pts: int = 12000) -> float:
    total = [0.0] * n_pts
    for phase in range(n_ph):
        shift = phase / n_ph
        for k in range(n_pts):
            x = (k / n_pts + shift) % 1.0
            y = -0.5 + x / D if x < D else 0.5 - (x - D) / (1.0 - D)
            total[k] += y
    return max(total) - min(total)


def _frequency_key(frequency_hz: float) -> str:
    """Сформировать устойчивый JSON-ключ без округления дробной частоты."""

    value = f"{frequency_hz / 1e3:.6f}".rstrip("0").rstrip(".")
    return f"{value.replace('.', 'p')}kHz"


@dataclass
class InterleavedMode:
    n_phases: int
    phase: Mode
    i_in_dc: float
    K_ripple: float
    K_ripple_num: float
    dI_in_pp: float
    dI_in_rel: float
    f_in_ripple: float
    w_total: float


def compute_mode_3ph(tz: TZ3, f_sw: float) -> InterleavedMode:
    phase = ind.compute_mode(tz.phase_tz(), f_sw)
    k = ripple_cancellation_factor(phase.D, tz.n_phases)
    k_num = ripple_cancellation_numeric(phase.D, tz.n_phases)
    d_i = k * phase.dI_pp
    return InterleavedMode(
        n_phases=tz.n_phases, phase=phase, i_in_dc=tz.i_in_nom,
        K_ripple=k, K_ripple_num=k_num, dI_in_pp=d_i,
        dI_in_rel=d_i / tz.i_in_nom, f_in_ripple=tz.n_phases * f_sw,
        w_total=phase.W_max * tz.n_phases,
    )


def core_library_3ph() -> Dict[str, Core]:
    """Совместимый вход: библиотека полностью загружается из knowledge_base."""

    return ind.core_library()


def area_product_screening(tz: TZ3, mode: Mode,
                           cores: Optional[Dict[str, Core]] = None,
                           materials: Optional[Dict[str, Material]] = None) -> List[Dict]:
    """Предварительный фильтр A_e·A_w по формуле Легостаева в СИ."""

    cores = cores or core_library_3ph()
    materials = materials or ind.material_library()
    mat = max((m for m in materials.values() if m.f_min <= mode.f_sw <= m.f_max),
              key=lambda m: m.B_S(tz.t_core_max))
    b_m = tz.k_B_prelim * mat.B_S(tz.t_core_max)
    k_peak = mode.I_peak_design / math.sqrt(mode.I_dc_max ** 2 + (tz.r_i * mode.I_dc_max) ** 2 / 12.0)
    ap_req = 2.0 * mode.W_max / (k_peak * tz.k_w_prelim * b_m * tz.j_dop)
    rows: List[Dict] = []
    for core in cores.values():
        ap = core.A_e * core.A_N
        rows.append({
            "core": core.name, "A_e_mm2": core.A_e * 1e6,
            "A_w_mm2": core.A_N * 1e6, "Ap_catalog_mm4": ap * 1e12,
            "Ap_required_mm4": ap_req * 1e12, "ok": ap >= ap_req,
            "custom_gap_possible": core.A_g is not None,
            "catalog_gap_count": len(core.gapped),
        })
    turn_criteria = ind.turn_window_screening(tz.phase_tz(), mode, cores, materials)[-1]["_criteria"]
    rows.append({"_criteria": {
        "material": mat.name, "B_prelim_mT": b_m * 1e3,
        "k_peak": k_peak, "k_w": tz.k_w_prelim,
        "J_A_mm2": tz.j_dop / 1e6, "W_max_mJ": mode.W_max * 1e3,
        "psi_max_mWb": mode.psi_max * 1e3,
        "Ap_required_mm4": ap_req * 1e12,
        "N_A_min_required_mm2": turn_criteria["N_A_min_required_mm2"],
        "S_cu_per_turn_mm2": turn_criteria["S_cu_per_turn_mm2"],
        "S_slot_per_turn_mm2": turn_criteria["S_slot_per_turn_mm2"],
        "J_dop_A_mm2": turn_criteria["J_dop_A_mm2"],
        "k_zan_dop": turn_criteria["k_zan_dop"],
    }})
    return rows


def stray_field_estimate(candidate: ind.Candidate, r_probe: float) -> Dict[str, float | str | None]:
    """Сравнительная дипольная оценка; не является результатом FEM."""

    if candidate.core.A_g is None:
        return {"status": "not_calculated_without_A_g", "r_probe_mm": r_probe * 1e3}
    b_ac = candidate.dB_pp / 2.0
    h_gap = b_ac / ind.MU0
    moment = h_gap * candidate.gap * candidate.core.A_g
    b_probe = ind.MU0 * moment / (2.0 * math.pi * r_probe ** 3)
    b_rms = b_probe / math.sqrt(2.0)
    u_ind = 2.0 * math.pi * candidate.mode.f_sw * b_rms * 1.0e-4
    return {
        "status": "preliminary_dipole_estimate", "r_probe_mm": r_probe * 1e3,
        "A_g_mm2": candidate.core.A_g * 1e6, "B_ac_pk_core_T": b_ac,
        "H_gap_ac_A_m": h_gap, "m_dipole_A_m2": moment,
        "B_stray_pk_uT": b_probe * 1e6, "B_stray_rms_uT": b_rms * 1e6,
        "U_induced_rms_mV": u_ind * 1e3,
    }


def enumerate_phase_candidates(tz: TZ3, mode: Mode, cores: Dict[str, Core],
                               mats: Dict[str, Material], litzes: Dict[str, Litz],
                               search: ind.SearchSettings
                               ) -> Tuple[List[ind.Candidate], int, int, Dict[str, int]]:
    """Полный перебор N_B…N_w без искусственного ограничения числа витков."""

    screen = area_product_screening(tz, mode, cores, mats)
    allowed_names = {row["core"] for row in screen if row.get("ok")}
    searched_cores = cores if search.exhaustive_core_search else {
        key: core for key, core in cores.items() if core.name in allowed_names
    }
    candidates, seen, rejected = ind.enumerate_candidates(
        tz.phase_tz(), mode, searched_cores, mats, litzes, search)
    return candidates, seen, len(candidates), rejected


def select_with_margins(cands: List[ind.Candidate], tz: TZ3
                        ) -> Tuple[Optional[ind.Candidate], List[ind.Candidate], Dict]:
    """Истинный фронт Парето и окно потерь; финальные FEM-критерии не имитируются."""

    best, front = ind.pareto_select(cands, tz.loss_window,
                                    tz.preferred_core_families)
    feasible = [c for c in cands if c.margins["_analytical_ok"]]
    preferred = [c for c in feasible if c.core.family in tz.phase_tz().preferred_core_families]
    selection_pool = preferred or feasible
    p_min = min((c.thermal["P_total_W"] for c in selection_pool), default=None)
    in_window = [c for c in front if p_min is not None and
                 c.thermal["P_total_W"] <= p_min * (1.0 + tz.loss_window)]
    return best, front, {
        "n_feasible": len(feasible), "n_pareto": len(front),
        "n_in_window": len(in_window), "loss_window_pct": tz.loss_window * 100.0,
        "preferred_feasible": len(preferred),
        "fallback_E_used": not bool(preferred),
        "policy": (
            f"предпочтительные {'/'.join(tz.preferred_core_families)}; "
            "E только при отсутствии допустимого предпочтительного кандидата"
        ),
        "selection_status": "analytical_preliminary",
    }


def _core_material_table(cores: Dict[str, Core], mats: Dict[str, Material],
                         candidates: List[ind.Candidate], tz: TZ3) -> List[Dict]:
    mode = candidates[0].mode if candidates else compute_mode_3ph(TZ3(), 100e3).phase
    return ind.core_material_comparison(cores, mats, candidates, mode, tz.phase_tz())


def _material_comparison(best: ind.Candidate, mode: Mode, tz: TZ3,
                         materials: Dict[str, Material]) -> Dict:
    return ind.material_comparison_for_selected(best, tz.phase_tz(), materials)


def _selected_case_ripple(tz: TZ3, candidate: ind.Candidate) -> Dict:
    rows = []
    for case in candidate.mode.cases:
        d_i_phase = case["lambda_plus_Vs"] / candidate.L_min
        k = ripple_cancellation_factor(case["D"], tz.n_phases)
        rows.append({
            "label": case["label"], "D": case["D"],
            "dI_phase_pp_A_at_Lmin": d_i_phase,
            "K_ripple": k, "dI_input_pp_A": k * d_i_phase,
            "dI_input_rel_pct": k * d_i_phase / (case["I_dc_A"] * tz.n_phases) * 100.0,
        })
    return max(rows, key=lambda x: x["dI_input_pp_A"])


def main() -> None:
    tz = load_tz3()
    search = ind.load_search_settings()
    cores = core_library_3ph()
    materials = ind.material_library()
    litzes = ind.litz_library()
    results: Dict[str, Dict] = {}

    print(f"{tz.n_phases}-фазный interleaved boost: исправленный аналитический пересчёт")
    print(f"Pвых={tz.p_out_nom:.0f} Вт; Uвх={tz.u_in_nom:.0f} В; Uвых={tz.u_out_nom:.0f} В; фаз={tz.n_phases}")
    for f_sw in tz.f_sw_list:
        inter = compute_mode_3ph(tz, f_sw)
        mode = inter.phase
        screening = area_product_screening(tz, mode, cores, materials)
        turn_screening = ind.turn_window_screening(tz.phase_tz(), mode, cores, materials)
        candidates, seen, calculated, rejection_counts = enumerate_phase_candidates(
            tz, mode, cores, materials, litzes, search)
        best, pareto, selection = select_with_margins(candidates, tz)
        if best is None:
            raise RuntimeError(f"{f_sw / 1e3:.0f} кГц: нет аналитически допустимого варианта")

        selected = ind.candidate_to_dict(best, tz.phase_tz())
        p_total_system = selected["losses"]["P_total_W"] * tz.n_phases
        selected["losses"]["P_total_system_W"] = p_total_system
        if tz.n_phases == 3:
            # Совместимость со старыми JSON трёхфазного шаблона.
            selected["losses"]["P_total_3ph_W"] = p_total_system
        selected["losses"]["loss_pct_system"] = (
            p_total_system / tz.p_in_nom * 100.0)
        selected["design"]["wire_length_total_system_m"] = (
            selected["design"]["wire_length_total_m"] * tz.n_phases)
        selected["verification"]["status"] = "analytical_preliminary"
        worst_ripple = _selected_case_ripple(tz, best)

        key = _frequency_key(f_sw)
        results[key] = {
            "f_sw_Hz": f_sw,
            "mode_converter": {
                "D": mode.D, "D_ideal": mode.D_ideal,
                "volt_second_error_V": mode.volt_second_error,
                "I_in_dc_A": inter.i_in_dc, "K_ripple": inter.K_ripple,
                "K_ripple_numeric": inter.K_ripple_num,
                "dI_in_pp_A": inter.dI_in_pp,
                "dI_in_rel_pct": inter.dI_in_rel * 100.0,
                "f_in_ripple_Hz": inter.f_in_ripple,
                "W_total_mJ": inter.w_total * 1e3,
                "worst_case_ripple": worst_ripple,
            },
            "mode_phase": {
                "I_dc_A": mode.I_dc, "dI_pp_A": mode.dI_pp,
                "I_max_A": mode.I_max, "I_rms_A": mode.I_rms,
                "L_req_uH": mode.L_req * 1e6,
                "L_nom_target_uH": mode.L_req / (1.0 - tz.tol_L) * 1e6,
                "psi_max_mWb": mode.psi_max * 1e3,
                "W_max_mJ": mode.W_max * 1e3,
                "lam_plus_mVs": mode.lam_plus * 1e3,
                "lambda_max_mVs": mode.lambda_max * 1e3,
                "case_L": mode.case_L, "case_I": mode.case_I,
                "cases": mode.cases,
            },
            "enumeration": {
                "n_seen": seen, "n_calculated": calculated,
                "rejection_counts": rejection_counts, **selection,
            },
            "quantities": {
                "phase_inductors": tz.n_phases,
                "core_halves_per_inductor": 2,
                "core_halves_total": 2 * tz.n_phases,
                "core_sets_per_inductor": 1,
                "core_sets_total": tz.n_phases,
            },
            "selected": selected,
            "stray_field": stray_field_estimate(best, tz.r_probe),
            "core_material_table": _core_material_table(cores, materials, candidates, tz),
            "area_product_screening": screening,
            "turn_window_screening": turn_screening,
            "catalog_gapped": {},
            "material_comparison": _material_comparison(best, mode, tz, materials),
            "litz_comparison": [],
        }
        print(f"{f_sw / 1e3:.0f} кГц: {best.core.name}/{best.mat.name}; N={best.n_turns}; "
              f"g={best.gap * 1e3:.3f} мм; Lном={best.L_nom * 1e6:.2f} мкГн; "
              f"Bнх={best.B_max_wc * 1e3:.1f} мТл; Pсист={p_total_system:.2f} Вт")

    payload = {
        "meta": {
            "schema_version": "1.0",
            "script": "5_interleaved/interleaved_design.py",
            "methodology": "0_references/Metodika_VCh_silovykh_drosseley_bez_rascheta.tex",
            "database": os.path.relpath(ind.DB_ROOT, ROOT),
            "project": dict(ind.PROJECT_CONFIG.get("project", {})),
            "config": ind.PROJECT_CONFIG,
            "search": asdict(search),
            "topology": (
                f"{tz.n_phases}-фазный interleaved boost, отдельный дроссель каждой фазы"
            ),
            "core_quantity_convention": (
                "один дроссель содержит один комплект из двух половинок; "
                f"система содержит {tz.n_phases} комплектов, то есть "
                f"{2 * tz.n_phases} половинок"
            ),
            "status": "analytical_preliminary",
            "final_verification": False,
            "limitations": [
                "L_diff(I) не подтверждена FEM или измерением",
                "локальная B с физическим радиусом кромки и u_B,числ не определены",
                "потери iGSE рассчитаны без карты DC bias",
                "потери меди у зазора, тепловой режим, собственный резонанс и ЭМС требуют проверки",
                "частотные варианты "
                + ", ".join(f"{frequency / 1e3:g} кГц" for frequency in tz.f_sw_list)
                + " являются альтернативными конструкциями",
            ],
        },
        "tz": asdict(tz),
        "tz_derived": {
            "P_in_W": tz.p_in_nom, "I_in_A": tz.i_in_nom,
            "I_phase_dc_A": tz.i_in_nom / tz.n_phases,
            "P_out_phase_W": tz.p_out_phase,
        },
        "materials": {name: {
            "name": mat.name, "datasheet": mat.datasheet,
            "f_min_kHz": mat.f_min / 1e3, "f_max_kHz": mat.f_max / 1e3,
            "B_S_25C_mT": mat.B_S(25.0) * 1e3,
            "B_S_100C_mT": mat.B_S(100.0) * 1e3,
            "T_curie_C": mat.T_curie, "mu_i": mat.mu_i,
            "density_kg_m3": mat.density,
            "steinmetz": {"k": mat.k_st, "alpha": mat.alpha, "beta": mat.beta,
                           "fit_limitation": mat.fit_limitation,
                           "iGSE_normalization": "full_0_2pi"},
        } for name, mat in materials.items()},
        "results": results,
    }
    with open(JSON_PATH, "w", encoding="utf-8") as stream:
        json.dump(payload, stream, ensure_ascii=False, indent=2)
    print(f"Сохранено: {JSON_PATH}")


if __name__ == "__main__":
    main()
