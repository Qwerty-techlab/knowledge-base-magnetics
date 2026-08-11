# -*- coding: utf-8 -*-
"""Расчёт ВЧ-дросселя по исправленной методике проекта.

Нормативный источник формул:
``0_references/Metodika_VCh_silovykh_drosseley_bez_rascheta.tex``.
Компонентные данные загружаются из ``knowledge_base/components_db``.

Аналитический расчёт является этапом проектирования. Критерии, которым по
методике требуются L_diff(I), локальная B с физическим радиусом кромки,
тепловая модель и ЭМС-измерения, в JSON помечаются как ``pending`` и не
подменяются расчётом малосигнальной индуктивности или произвольным запасом.
"""
from __future__ import annotations

import functools
import json
import math
import os
import sys
from dataclasses import asdict, dataclass, field, replace
from typing import Dict, List, Optional, Tuple

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

MU0 = 4.0e-7 * math.pi
RHO_CU_20 = 1.724e-8
ALPHA_CU = 3.93e-3

HERE = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(HERE)
WORKSPACE_ROOT = os.path.dirname(PROJECT_ROOT)
CONFIG_PATH = os.path.join(PROJECT_ROOT, "2_input_files", "design_config.json")


def _load_project_config() -> Dict:
    if not os.path.exists(CONFIG_PATH):
        return {}
    with open(CONFIG_PATH, encoding="utf-8") as stream:
        return json.load(stream)


PROJECT_CONFIG = _load_project_config()


def _resolve_db_root() -> str:
    candidates: List[str] = []
    env_path = os.environ.get("INDUCTOR_KNOWLEDGE_BASE")
    if env_path:
        candidates.append(env_path)
    configured = PROJECT_CONFIG.get("knowledge_base_path")
    if configured and configured != "__AUTO__":
        candidates.append(configured)
    candidates.append(os.path.join(WORKSPACE_ROOT, "knowledge_base"))
    current = PROJECT_ROOT
    for _ in range(8):
        candidates.append(current)
        candidates.append(os.path.join(current, "knowledge_base"))
        parent = os.path.dirname(current)
        if parent == current:
            break
        current = parent
    for candidate in candidates:
        db_root = os.path.join(os.path.abspath(candidate), "components_db")
        if os.path.isfile(os.path.join(db_root, "cores.json")):
            return db_root
    raise FileNotFoundError(
        "не найдена knowledge_base/components_db; задайте knowledge_base_path "
        "в 2_input_files/design_config.json или INDUCTOR_KNOWLEDGE_BASE"
    )


DB_ROOT = _resolve_db_root()


def _load_json(name: str) -> Dict:
    path = os.path.join(DB_ROOT, name)
    with open(path, encoding="utf-8") as stream:
        return json.load(stream)


@dataclass
class TZ:
    """Техническое задание для одного дросселя."""

    u_in_nom: float = 160.0
    u_out_nom: float = 235.0
    i_out_nom: float = 25.0
    p_out_nom: float = 6000.0
    eta: float = 0.90
    ripple_u_in: float = 0.10       # размах, доля номинала
    ripple_u_out: float = 0.10      # размах, доля номинала
    r_i: float = 0.10               # требуемый размах тока / I_DC
    f_sw_list: Tuple[float, ...] = (100e3, 150e3)
    tol_u_in: float = 0.05          # независимый допуск среднего U_in
    tol_i_load: float = 0.10
    tol_L: float = 0.10
    t_amb: float = 40.0
    t_core_max: float = 100.0
    t_wind_max: float = 100.0
    k_B: float = 0.65               # только для финальной FEM-проверки
    k_B_prelim: float = 0.60        # аналитический отбор без FEM
    u_B_num: Optional[float] = None  # назначается только по сеточной сходимости
    k_cu_dop: float = 0.35          # проектный предел после выбора реального кабеля
    k_zan_dop: float = 0.70
    k_reluctance_min: float = 4.0
    k_w_prelim: float = 0.20        # первый фильтр по произведению площадей
    j_prelim: float = 2.5e6         # естественная конвекция, первый проход, А/м²
    j_final_max: float = 2.5e6      # предельная плотность тока по ТЗ, А/м²
    k_f_res: float = 3.0
    M_EMC: float = 6.0
    gap_clearance: float = 5.0e-3   # конструктивное допущение до МКЭ поля зазора
    side_margin_fraction: float = 0.05
    turn_spacing_ratio: float = 0.10
    interlayer_insulation: float = 0.20e-3
    bend_radius_ratio: float = 3.0
    # Поля оставлены для совместимости с interleaved_design.py. В новом
    # расчёте q берётся из геометрии сердечника, а отступ не связывается с g.
    q_fringe: float = 0.90
    k_r_gap: float = 1.0
    r_gap_min: float = 1.0e-3
    n_gaps_list: Tuple[int, ...] = (1,)
    loss_window: float = 0.02
    f_treb_ratio: float = 5.0
    preferred_core_families: Tuple[str, ...] = ("EQ", "ETD", "PM", "PQ", "RM", "EER")

    def f_treb_max(self, f_sw: float) -> float:
        return self.f_treb_ratio * f_sw


def load_tz() -> TZ:
    """Загрузить ТЗ одиночного дросселя из единого файла проекта."""
    raw = dict(PROJECT_CONFIG.get("single", {}).get("tz", {}))
    for key in ("f_sw_list", "n_gaps_list", "preferred_core_families"):
        if key in raw:
            raw[key] = tuple(raw[key])
    allowed = set(TZ.__dataclass_fields__)
    unknown = sorted(set(raw) - allowed)
    if unknown:
        raise KeyError(f"неизвестные поля single.tz: {', '.join(unknown)}")
    return TZ(**raw)


@dataclass
class Core:
    """Геометрия и магнитные параметры комплекта сердечника в СИ."""

    name: str
    A_e: float
    A_min: float
    l_e: float
    V_e: float
    sigma_l_A: float
    A_L0: float
    mass: float
    d_center: float
    d_bore: float
    h_window: float
    A_N: float
    l_N: float
    A_R: float
    family: str = ""
    shape: str = ""
    outer_width: float = 0.0
    set_height: float = 0.0
    depth: float = 0.0
    radial_window: float = 0.0
    l_N_base: float = 0.0
    datasheet: str = ""
    A_g: Optional[float] = None
    G_gap: Optional[float] = None
    G_gap_bounds: Tuple[float, float] = (0.0, 0.0)
    q_fringe_bounds: Tuple[float, float] = (0.0, 0.0)
    gap_surface: Optional[str] = None
    A_g_source: Optional[str] = None
    gapped: Dict[str, Tuple[float, float, float]] = field(default_factory=dict)
    gapped_material: Dict[str, str] = field(default_factory=dict)
    A_L0_by_mat: Dict[str, float] = field(default_factory=dict)
    part_ungapped: Dict[str, str] = field(default_factory=dict)
    db_key: str = ""

    def A_L0_of(self, mat_name: str) -> float:
        # Отсутствующий материал нельзя подменять первым попавшимся A_L0:
        # это создало бы несуществующую комбинацию сердечник/материал.
        return self.A_L0_by_mat.get(mat_name, 0.0)


def core_library() -> Dict[str, Core]:
    """Загрузить сердечники из единой базы knowledge_base."""

    raw = _load_json("cores.json")["cores"]
    out: Dict[str, Core] = {}
    for key, item in raw.items():
        geo = item["geometry"]
        mag = item["magnetic"]
        wnd = item["winding"]
        al_raw = item.get("A_L_ungapped_nH", {})
        al_by_mat = {
            name: value * 1e-9 for name, value in al_raw.items()
            if name != "tolerance_pct" and isinstance(value, (int, float))
        }
        al0 = next(iter(al_by_mat.values()), 0.0)

        A_g = None
        gap_surface = None
        A_g_source = None
        surfaces = geo.get("gap_surfaces") or {}
        surface: Dict = {}
        if surfaces:
            preferred = [(name, value) for name, value in surfaces.items()
                         if value.get("preferred_for_single_gap")]
            gap_surface, surface = preferred[0] if preferred else next(iter(surfaces.items()))
            value = surface.get("A_g_mm2_estimated")
            if value is not None:
                A_g = value * 1e-6
                A_g_source = surface.get("source")

        gapped: Dict[str, Tuple[float, float, float]] = {}
        gapped_material: Dict[str, str] = {}
        for pn, entry in (item.get("gapped_catalog") or {}).items():
            gapped[pn] = (
                entry["A_L_nH"] * 1e-9,
                entry.get("gap_total_mm", 0.0) * 1e-3,
                entry.get("A_L_tolerance_pct", 0.0) / 100.0,
            )
            gapped_material[pn] = entry.get("material", "")

        family = item.get("family", "")
        q_default = (1.0, 1.1) if family in ("E", "EE", "EI") else (0.85, 0.95)
        q_bounds = tuple(surface.get("q_fringe_bounds", q_default))
        g_values = surface.get("G_gap_bounds_mm")
        if g_values is None and A_g is not None:
            # Границы составлены только из размеров выбранной геометрии, без
            # произвольного единственного G; окончательный F_f подтверждает МКЭ.
            g_values = sorted((geo.get("d_center_mm", geo["h_window_mm"]),
                               geo["h_window_mm"]))
        G_bounds = tuple(x * 1e-3 for x in (g_values or (0.0, 0.0)))
        radial = geo.get("window_radial_mm")
        if radial is None:
            radial = (geo["d_bore_mm"] - geo["d_center_mm"]) / 2.0
        l_n = wnd["l_N_mm"] * 1e-3
        l_n_base = wnd.get("l_N_base_mm_estimated")
        if l_n_base is None:
            l_n_base = max(0.0, l_n - math.pi * radial * 1e-3)

        out[key] = Core(
            name=item["name"],
            A_e=mag["A_e_mm2"] * 1e-6,
            A_min=mag["A_min_mm2"] * 1e-6,
            l_e=mag["l_e_mm"] * 1e-3,
            V_e=mag["V_e_mm3"] * 1e-9,
            sigma_l_A=mag["sigma_l_A_per_mm"] * 1e3,
            A_L0=al0,
            mass=item["mass_kg"],
            d_center=geo["d_center_mm"] * 1e-3,
            d_bore=geo["d_bore_mm"] * 1e-3,
            h_window=geo["h_window_mm"] * 1e-3,
            A_N=wnd["A_N_mm2"] * 1e-6,
            l_N=wnd["l_N_mm"] * 1e-3,
            A_R=wnd["A_R_uOhm"] * 1e-6,
            family=family, shape=item.get("shape", ""),
            outer_width=geo.get("D_outer_mm", 0.0) * 1e-3,
            set_height=geo.get("H_set_mm", 0.0) * 1e-3,
            depth=geo.get("depth_mm", geo.get("D_outer_mm", 0.0)) * 1e-3,
            radial_window=radial * 1e-3,
            l_N_base=l_n_base * 1e-3 if isinstance(l_n_base, (int, float)) and l_n_base > 1.0 else l_n_base,
            datasheet=item.get("datasheet", ""),
            A_g=A_g,
            G_gap=(sum(G_bounds) / 2.0 if A_g is not None else None),
            G_gap_bounds=G_bounds,
            q_fringe_bounds=q_bounds,
            gap_surface=gap_surface,
            A_g_source=A_g_source,
            gapped=gapped,
            gapped_material=gapped_material,
            A_L0_by_mat=al_by_mat,
            part_ungapped=(item.get("part_numbers") or {}).get("ungapped", {}),
            db_key=key,
        )
    return out


@dataclass
class Material:
    name: str
    mu_i: float
    B_S_25: float
    B_S_100: float
    f_min: float
    f_max: float
    T_curie: float
    density: float
    k_st: float
    alpha: float
    beta: float
    datasheet: str = ""
    fit_limitation: str = ""

    def B_S(self, t_c: float) -> float:
        return self.B_S_25 + (self.B_S_100 - self.B_S_25) * (t_c - 25.0) / 75.0


def material_library() -> Dict[str, Material]:
    raw = _load_json("ferrite_materials.json")["materials"]
    out: Dict[str, Material] = {}
    for key, item in raw.items():
        sat = item["saturation"]
        freq = item["frequency_range"]
        stein = item["steinmetz"]
        out[key] = Material(
            name=item["name"],
            mu_i=item["permeability"]["mu_i"],
            B_S_25=sat["B_S_25C_T"],
            B_S_100=sat["B_S_100C_T"],
            f_min=freq["f_min_Hz"],
            f_max=freq["f_max_Hz"],
            T_curie=item["temperature"]["T_curie_C"],
            density=item["physical"]["density_kg_m3"],
            k_st=stein["k_st"],
            alpha=stein["alpha"],
            beta=stein["beta"],
            datasheet=item.get("datasheet", ""),
            fit_limitation=stein.get("fit_limitation", ""),
        )
    return out


@dataclass
class Litz:
    name: str
    n_strands: int
    d_strand: float
    d_outer: float
    t_index: float
    std: str
    price: float
    price_unit: str
    url: str
    n_parallel: int = 1
    S_cu_db: Optional[float] = None
    R_dc_ref: Optional[float] = None
    length_per_kg: Optional[float] = None
    db_key: str = ""

    @property
    def S_cu_single(self) -> float:
        if self.S_cu_db is not None:
            return self.S_cu_db
        return self.n_strands * math.pi * self.d_strand ** 2 / 4.0

    @property
    def S_cu(self) -> float:
        return self.S_cu_single * self.n_parallel

    @property
    def S_out(self) -> float:
        return self.n_parallel * math.pi * self.d_outer ** 2 / 4.0

    @property
    def designation(self) -> str:
        parallel = f" × {self.n_parallel} парал." if self.n_parallel > 1 else ""
        return f"{self.name} {self.n_strands}×{self.d_strand * 1e3:.3f} мм".replace(".", ",") + parallel


def litz_library() -> Dict[str, Litz]:
    raw = _load_json("litz_wire.json")["wires"]
    out: Dict[str, Litz] = {}
    for key, item in raw.items():
        price = item.get("price") or {}
        insulation = item.get("insulation") or {}
        unit = price.get("unit", "")
        length = price.get("length_per_kg_m")
        if length:
            unit = f"{unit} ({length:g} м/кг)"
        out[key] = Litz(
            name=item["designation"].split(" ", 1)[0] if item["designation"].startswith("ЛЭШО") else "Litz wire (нейлон)",
            n_strands=item["n_strands"],
            d_strand=item["d_strand_mm"] * 1e-3,
            d_outer=item["d_outer_mm"] * 1e-3,
            t_index=insulation.get("t_index_C", 105.0),
            std=item.get("standard", ""),
            price=price.get("value", 0.0),
            price_unit=unit,
            url=item.get("url", ""),
            S_cu_db=item.get("S_cu_mm2", 0.0) * 1e-6,
            R_dc_ref=item.get("R_dc_mOhm_per_m", 0.0) * 1e-3,
            length_per_kg=length,
            db_key=key,
        )
    return out


@dataclass
class Mode:
    f_sw: float
    D_ideal: float
    D: float
    p_in: float
    I_dc: float
    dI_pp: float
    I_max: float
    I_min: float
    I_rms: float
    I_ac_rms: float
    L_req: float
    lam_plus: float
    psi_max: float
    W_max: float
    f_eff: float
    B_ac_pk: float = 0.0
    u_in: float = 0.0
    u_out: float = 0.0
    volt_second_error: float = 0.0
    lambda_max: float = 0.0
    I_dc_max: float = 0.0
    I_peak_design: float = 0.0
    case_L: str = ""
    case_I: str = ""
    cases: List[Dict] = field(default_factory=list)


def _operating_cases(tz: TZ, f_sw: float) -> List[Dict]:
    """Перебрать крайние сочетания входного и выходного напряжения."""

    uin_factors = sorted({
        (1.0 - tz.ripple_u_in / 2.0) * (1.0 - tz.tol_u_in),
        1.0,
        (1.0 + tz.ripple_u_in / 2.0) * (1.0 + tz.tol_u_in),
    })
    uout_factors = sorted({1.0 - tz.ripple_u_out / 2.0, 1.0, 1.0 + tz.ripple_u_out / 2.0})
    p_in = tz.p_out_nom / tz.eta
    cases: List[Dict] = []
    for ku in uin_factors:
        for ko in uout_factors:
            u_in = tz.u_in_nom * ku
            u_out = tz.u_out_nom * ko
            D = 1.0 - u_in / u_out
            if not 0.0 < D < 1.0:
                continue
            I_dc = p_in / u_in
            dI_limit = tz.r_i * I_dc
            lam = u_in * D / f_sw
            L_req = lam / dI_limit
            label = f"Uin={u_in:.3f} V; Uout={u_out:.3f} V"
            cases.append({
                "label": label, "u_in_V": u_in, "u_out_V": u_out,
                "D": D, "u_L_on_V": u_in, "u_L_off_V": u_in - u_out,
                "volt_second_V": u_in * D + (u_in - u_out) * (1.0 - D),
                "I_dc_A": I_dc, "dI_limit_A": dI_limit,
                "lambda_plus_Vs": lam, "L_req_H": L_req,
            })
    return cases


def compute_mode(tz: TZ, f_sw: float) -> Mode:
    """Рассчитать номинальный режим и огибающую крайних сочетаний."""

    cases = _operating_cases(tz, f_sw)
    if not cases:
        raise ValueError("нет допустимых сочетаний напряжений")
    p_in = tz.p_out_nom / tz.eta
    D = 1.0 - tz.u_in_nom / tz.u_out_nom
    I_dc = p_in / tz.u_in_nom
    dI = tz.r_i * I_dc
    lam = tz.u_in_nom * D / f_sw
    L_req_nom = lam / dI
    I_max = I_dc + dI / 2.0
    I_min = I_dc - dI / 2.0
    I_ac = dI / (2.0 * math.sqrt(3.0))
    I_rms = math.sqrt(I_dc ** 2 + I_ac ** 2)
    case_L = max(cases, key=lambda x: x["L_req_H"])
    case_I = max(cases, key=lambda x: x["I_dc_A"])
    lambda_max = max(x["lambda_plus_Vs"] for x in cases)
    L_req = case_L["L_req_H"]
    L_design_nom = L_req / (1.0 - tz.tol_L)
    L_design_max = L_design_nom * (1.0 + tz.tol_L)
    magnetic = []
    for case in cases:
        d_i = case["lambda_plus_Vs"] / L_design_max
        peak = case["I_dc_A"] * (1.0 + tz.tol_i_load) + d_i / 2.0
        magnetic.append((L_design_max * peak, peak, case))
    psi, I_peak_design, _case_psi = max(magnetic, key=lambda x: x[0])
    W = 0.5 * L_design_max * I_peak_design ** 2

    # По методике знаменатель содержит полный действующий ток, включая I_DC.
    T = 1.0 / f_sw
    slope_on = dI / (D * T)
    slope_off = dI / ((1.0 - D) * T)
    slope_rms = math.sqrt(D * slope_on ** 2 + (1.0 - D) * slope_off ** 2)
    f_eff = slope_rms / (2.0 * math.pi * I_rms)
    vs_error = tz.u_in_nom * D + (tz.u_in_nom - tz.u_out_nom) * (1.0 - D)
    return Mode(
        f_sw=f_sw, D_ideal=D, D=D, p_in=p_in, I_dc=I_dc,
        dI_pp=dI, I_max=I_max, I_min=I_min, I_rms=I_rms,
        I_ac_rms=I_ac, L_req=L_req, lam_plus=lam, psi_max=psi,
        W_max=W, f_eff=f_eff, u_in=tz.u_in_nom, u_out=tz.u_out_nom,
        volt_second_error=vs_error, lambda_max=lambda_max,
        I_dc_max=case_I["I_dc_A"], I_peak_design=I_peak_design,
        case_L=case_L["label"], case_I=case_I["label"], cases=cases,
    )


@functools.lru_cache(maxsize=32)
def _harmonic_shape(D_rounded: float, n_h: int, n_pts: int = 2048) -> Tuple[float, ...]:
    """СКЗ-коэффициенты Фурье несимметричной треугольной пульсации."""

    D = D_rounded
    samples = []
    for k in range(n_pts):
        x = (k + 0.5) / n_pts
        y = -0.5 + x / D if x < D else 0.5 - (x - D) / (1.0 - D)
        samples.append(y)
    result = []
    for h in range(1, n_h + 1):
        a = 2.0 / n_pts * sum(y * math.cos(2.0 * math.pi * h * (k + 0.5) / n_pts) for k, y in enumerate(samples))
        b = 2.0 / n_pts * sum(y * math.sin(2.0 * math.pi * h * (k + 0.5) / n_pts) for k, y in enumerate(samples))
        result.append(math.hypot(a, b) / math.sqrt(2.0))
    return tuple(result)


def harmonic_currents(mode: Mode, n_h: int = 80) -> List[Tuple[float, float]]:
    shape = _harmonic_shape(round(mode.D, 12), n_h)
    return [(mode.f_sw * h, mode.dI_pp * value) for h, value in enumerate(shape, 1)]


def fringing_factor(g: float, A_g: float, G: float, q: float) -> float:
    """Коэффициент выпучивания для одного физического участка зазора."""

    if g <= 0.0:
        return 1.0
    if A_g <= 0.0 or G <= 0.0:
        raise ValueError("для расчёта выпучивания требуются A_g и G")
    ratio = 2.0 * G / g
    if ratio <= 1.0:
        raise ValueError("формула выпучивания неприменима при 2G/g <= 1")
    return 1.0 + q * g / math.sqrt(A_g) * math.log(ratio)


def gap_for_AL(A_L: float, core: Core, q: float, n_gaps: int = 1,
               tol: float = 1e-3, it_max: int = 200,
               A_L0: Optional[float] = None,
               G_gap: Optional[float] = None) -> Tuple[float, float, int]:
    """Суммарный физический зазор по A_L; критерий решения относительный.

    Решается уравнение ``g = C·F_f(g/n_gaps)``. Бисекция используется вместо
    неустойчивой простой итерации, но вычисляет тот же корень методики.
    """

    G = core.G_gap if G_gap is None else G_gap
    if core.A_g is None or G is None or G <= 0.0:
        raise ValueError(f"для {core.name} в базе отсутствует физическая площадь A_g")
    if n_gaps < 1:
        raise ValueError("число участков зазора должно быть положительным")
    al0 = core.A_L0 if A_L0 is None else A_L0
    inv = 1.0 / A_L - 1.0 / al0
    if inv <= 0.0:
        return 0.0, 1.0, 0
    constant = MU0 * core.A_g * inv
    upper = 2.0 * G * n_gaps * (1.0 - 1e-9)
    if constant >= upper:
        raise ValueError("требуемый зазор вне области применимости 2G/g > 1")

    def residual(g_total: float) -> float:
        factor = fringing_factor(g_total / n_gaps, core.A_g, G, q)
        return g_total - constant * factor

    lower = max(constant * 1e-9, 1e-15)
    f_lower = residual(lower)
    f_upper = residual(upper)
    if f_lower * f_upper > 0.0:
        raise ValueError("уравнение зазора не имеет физического корня")
    for it in range(1, it_max + 1):
        middle = 0.5 * (lower + upper)
        f_middle = residual(middle)
        if abs(upper - lower) / max(abs(middle), 1e-15) <= tol:
            factor = fringing_factor(middle / n_gaps, core.A_g, G, q)
            return middle, factor, it
        if f_lower * f_middle <= 0.0:
            upper, f_upper = middle, f_middle
        else:
            lower, f_lower = middle, f_middle
    raise RuntimeError(f"решение зазора не сошлось за {it_max} шагов")


def AL_from_gap(g: float, core: Core, q: float, n_gaps: int = 1,
                A_L0: Optional[float] = None,
                G_gap: Optional[float] = None) -> float:
    G = core.G_gap if G_gap is None else G_gap
    if core.A_g is None or G is None or G <= 0.0:
        raise ValueError(f"для {core.name} в базе отсутствует A_g")
    al0 = core.A_L0 if A_L0 is None else A_L0
    if g <= 0.0:
        return al0
    F = fringing_factor(g / n_gaps, core.A_g, G, q)
    return 1.0 / (g / (MU0 * core.A_g * F) + 1.0 / al0)


def reluctance_ratio(A_L: float, core: Core, A_L0: Optional[float] = None) -> float:
    al0 = core.A_L0 if A_L0 is None else A_L0
    return al0 / A_L - 1.0


def rho_cu(t_c: float) -> float:
    return RHO_CU_20 * (1.0 + ALPHA_CU * (t_c - 20.0))


def skin_depth(f: float, t_c: float) -> float:
    return math.sqrt(rho_cu(t_c) / (math.pi * f * MU0)) if f > 0.0 else float("inf")


def litz_FR(litz: Litz, f: float, t_c: float, n_turns: int, b_window: float) -> float:
    """Предварительная 1D-оценка F_R; поле зазора сюда не входит."""

    if f <= 0.0:
        return 1.0
    delta = skin_depth(f, t_c)
    xi = litz.d_strand / (2.0 * delta)
    f_skin = 1.0 + xi ** 4 / 48.0
    if b_window <= 0.0:
        return f_skin
    omega = 2.0 * math.pi * f
    n_str = litz.n_strands * litz.n_parallel
    prox = (math.pi ** 2 * omega ** 2 * MU0 ** 2 * n_turns ** 2 * n_str ** 2
            * litz.d_strand ** 6) / (768.0 * rho_cu(t_c) ** 2 * b_window ** 2)
    return f_skin + prox


def winding_resistance_dc(litz: Litz, n_turns: int, l_turn: float, t_c: float) -> float:
    return rho_cu(t_c) * n_turns * l_turn / litz.S_cu


def copper_loss(litz: Litz, n_turns: int, l_turn: float, mode: Mode,
                t_c: float, b_window: float) -> Tuple[float, float, float, Dict]:
    r_dc = winding_resistance_dc(litz, n_turns, l_turn, t_c)
    p_dc = mode.I_dc ** 2 * r_dc
    p_ac = 0.0
    details = []
    harmonics = harmonic_currents(mode)
    for f_h, i_h in harmonics:
        f_r = litz_FR(litz, f_h, t_c, n_turns, b_window)
        p_h = i_h ** 2 * r_dc * f_r
        p_ac += p_h
        if len(details) < 12:
            details.append({"f_Hz": f_h, "I_rms_A": i_h, "F_R": f_r,
                            "R_ac_Ohm": r_dc * f_r, "P_W": p_h})
    spectrum_rms = math.sqrt(sum(i_h ** 2 for _, i_h in harmonics))
    convergence = spectrum_rms / mode.I_ac_rms if mode.I_ac_rms > 0.0 else 1.0
    return p_dc, p_ac, r_dc, {
        "harmonics": details,
        "harmonic_count": len(harmonics),
        "spectrum_rms_ratio": convergence,
    }


@functools.lru_cache(maxsize=32)
def _cos_integral(alpha_rounded: float, n: int = 20000) -> float:
    step = 2.0 * math.pi / n
    return sum(abs(math.cos((j + 0.5) * step)) ** alpha_rounded for j in range(n)) * step


def igse_ki(mat: Material) -> float:
    """Полная нормировка iGSE к исходному уравнению Штейнмеца."""

    integral = _cos_integral(round(mat.alpha, 12))
    denom = ((2.0 * math.pi) ** (mat.alpha - 1.0)
             * 2.0 ** (mat.beta - mat.alpha) * integral)
    return mat.k_st / denom


def core_loss_igse(mat: Material, core: Core, mode: Mode, dB_pp: float) -> float:
    if dB_pp <= 0.0:
        return 0.0
    D = min(max(mode.D, 1e-9), 1.0 - 1e-9)
    T = 1.0 / mode.f_sw
    term = (D * (dB_pp / (D * T)) ** mat.alpha
            + (1.0 - D) * (dB_pp / ((1.0 - D) * T)) ** mat.alpha)
    return igse_ki(mat) * dB_pp ** (mat.beta - mat.alpha) * term * core.V_e


def self_capacitance(n_turns: int, l_turn: float, d_out: float,
                     n_layers: float = 1.0, eps_r: float = 3.2) -> float:
    """Предварительная сосредоточенная оценка; требует измерения прототипа."""

    if n_turns < 2:
        return 0.0
    eps0 = 8.8541878128e-12
    n_l = max(2.0, n_turns / max(1.0, n_layers))
    c_tt = eps0 * eps_r * math.pi * l_turn / math.log(1.0 + math.pi / 2.0)
    c_layer = c_tt / (n_l - 1.0)
    if n_layers <= 1.0:
        return c_layer
    c_ll = eps0 * eps_r * l_turn * n_l
    return c_layer / n_layers + (4.0 / 3.0) * c_ll / (n_layers - 1.0) ** 2


def resonance_frequency(L: float, C: float) -> float:
    return 1.0 / (2.0 * math.pi * math.sqrt(L * C)) if L > 0.0 and C > 0.0 else float("inf")


def C_self_max(L: float, f_treb_max: float, k_f: float) -> float:
    return 1.0 / ((2.0 * math.pi * k_f * f_treb_max) ** 2 * L)


def impedance_attenuation(L: float, C: float, f: float, Z_s: float = 50.0,
                          Z_l: float = 50.0, R: float = 0.0) -> float:
    """Комплексная модель последовательного дросселя с параллельной C_self."""

    w = 2.0 * math.pi * f
    z_lr = complex(R, w * L)
    if C > 0.0:
        y = 1.0 / z_lr + complex(0.0, w * C)
        z = 1.0 / y if abs(y) > 1e-30 else complex(1e30, 0.0)
    else:
        z = z_lr
    return 20.0 * math.log10(abs(1.0 + z / (Z_s + Z_l)))


def thermal_resistance(core: Core) -> float:
    if core.family in ("E", "EE", "EI") and core.outer_width > 0.0:
        # Консервативно учитывается только наружная поверхность описывающего
        # параллелепипеда; окна и контакт с основанием не кредитуются.
        area = 2.0 * (core.outer_width * core.depth
                      + core.outer_width * core.set_height
                      + core.depth * core.set_height)
    else:
        d_out = max(core.d_bore * 1.15,
                    core.d_bore + 0.15 * 2.0 * (core.d_bore - core.d_center))
        h_out = core.h_window + 0.038
        area = math.pi * d_out * h_out + math.pi * d_out ** 2 / 2.0
    return 1.0 / (12.0 * area)


def solve_thermal(tz: TZ, core: Core, mat: Material, litz: Litz, n_turns: int,
                  l_turn: float, mode: Mode, dB_pp: float, b_window: float,
                  it_max: int = 60) -> Dict:
    r_th = thermal_resistance(core)
    t_w = tz.t_amb + 30.0
    t_c = tz.t_amb + 25.0
    p_prev = 0.0
    thermal_runaway = False
    for it in range(1, it_max + 1):
        p_dc, p_ac, r_dc, detail = copper_loss(litz, n_turns, l_turn, mode, t_w, b_window)
        p_fe = core_loss_igse(mat, core, mode, dB_pp)
        p_total = p_dc + p_ac + p_fe
        dtheta = p_total * r_th
        t_c_new = tz.t_amb + dtheta
        t_w_new = t_c_new + 0.15 * dtheta
        if (not math.isfinite(t_w_new) or not math.isfinite(t_c_new)
                or t_w_new > 1000.0 or t_c_new > 1000.0):
            thermal_runaway = True
            t_w = min(t_w_new, 1000.0) if math.isfinite(t_w_new) else 1000.0
            t_c = min(t_c_new, 1000.0) if math.isfinite(t_c_new) else 1000.0
            p_total = min(p_total, 1.0e6) if math.isfinite(p_total) else 1.0e6
            dtheta = min(dtheta, 960.0) if math.isfinite(dtheta) else 960.0
            break
        ok_t = abs(t_w_new - t_w) < 1.0 and abs(t_c_new - t_c) < 1.0
        ok_p = p_prev > 0.0 and abs(p_total - p_prev) / max(p_total, 1e-12) < 0.01
        t_w, t_c, p_prev = t_w_new, t_c_new, p_total
        if ok_t and ok_p:
            break
    return {
        "R_th_K_W": r_th, "t_winding_C": t_w, "t_core_C": t_c,
        "P_cu_W": p_dc + p_ac, "P_dc_W": p_dc, "P_ac_W": p_ac,
        "P_fe_W": p_fe, "P_total_W": p_total, "R_dc_Ohm": r_dc,
        "iterations": it, "dtheta_K": dtheta, "harmonics": detail["harmonics"],
        "harmonic_count": detail["harmonic_count"],
        "spectrum_rms_ratio": detail["spectrum_rms_ratio"],
        "status": "thermal_runaway" if thermal_runaway else "preliminary",
        "thermal_runaway": thermal_runaway, "dc_bias_map_used": False,
        "gap_field_copper_loss_included": False,
        "I_rms_A": mode.I_rms,
    }


@dataclass
class Candidate:
    core: Core
    mat: Material
    litz: Litz
    mode: Mode
    n_turns: int
    part_number: str
    A_L_req: float
    A_L_actual: float
    gap: float
    gap_catalog: Optional[float]
    F_fringe: float
    gap_iters: int
    L_nom: float
    L_min: float
    L_max: float
    B_max_nom: float
    B_max_wc: float
    B_allow: float
    B_ac_pk: float
    dB_pp: float
    k_cu: float
    k_zan: float
    n_layers: float
    l_turn: float
    b_winding: float
    k_R: float
    C_self: float
    f_res: float
    C_self_max: float
    thermal: Dict
    r_gap: float = 0.0
    h_wind: float = 0.0
    n_gaps: int = 1
    A_L_tolerance: float = 0.0
    construction: str = "custom_gap"
    gap_min: float = 0.0
    gap_max: float = 0.0
    F_fringe_min: float = 1.0
    F_fringe_max: float = 1.0
    q_fringe: float = 0.0
    G_gap_model: float = 0.0
    winding_layout: Dict = field(default_factory=dict)
    magnetic_corner: Dict = field(default_factory=dict)
    margins: Dict = field(default_factory=dict)


def winding_geometry(tz: TZ, core: Core, litz: Litz, n_turns: int,
                     gap_keepout_half: float) -> Dict:
    """Проверить дискретную укладку отдельных параллельных кабелей.

    Обмотка разделена на два осевых банка по сторонам единственного зазора.
    В каждом витке параллельные кабели занимают целое число осевых и
    радиальных позиций; эквивалентный диаметр ``sqrt(n_parallel)`` не
    используется.
    """

    d = litz.d_outer
    spacing = tz.turn_spacing_ratio * d
    side_margin = tz.side_margin_fraction * core.h_window
    bank_height = core.h_window / 2.0 - side_margin - gap_keepout_half
    radial_available = core.radial_window * (1.0 - 2.0 * tz.side_margin_fraction)
    if bank_height <= d or radial_available <= d:
        raise ValueError("нет места для обмотки после конструктивных отступов")

    layouts: List[Dict] = []
    for n_axial in range(1, litz.n_parallel + 1):
        n_radial = math.ceil(litz.n_parallel / n_axial)
        group_axial = n_axial * d + (n_axial - 1) * spacing
        turn_pitch = group_axial + spacing
        turns_per_bank = math.floor((bank_height + spacing) / turn_pitch)
        turns_per_layer = 2 * turns_per_bank
        if turns_per_layer < 1:
            continue
        n_layers = math.ceil(n_turns / turns_per_layer)
        group_radial = n_radial * d + (n_radial - 1) * spacing
        b_winding = (n_layers * group_radial
                     + max(0, n_layers - 1) * tz.interlayer_insulation)
        bend_radius = tz.bend_radius_ratio * d
        if b_winding > radial_available or bend_radius > core.h_window / 2.0:
            continue
        l_turn = core.l_N_base + math.pi * b_winding
        layouts.append({
            "parallel_axial": n_axial,
            "parallel_radial": n_radial,
            "turns_per_bank_per_layer": turns_per_bank,
            "turns_per_layer": turns_per_layer,
            "n_layers": n_layers,
            "group_axial_m": group_axial,
            "group_radial_m": group_radial,
            "turn_pitch_m": turn_pitch,
            "turn_spacing_m": spacing,
            "interlayer_insulation_m": tz.interlayer_insulation,
            "side_margin_m": side_margin,
            "gap_edge_clearance_m": tz.gap_clearance,
            "gap_keepout_half_m": gap_keepout_half,
            "bank_height_m": bank_height,
            "h_wind_m": 2.0 * bank_height,
            "radial_available_m": radial_available,
            "b_winding_m": b_winding,
            "bend_radius_min_m": bend_radius,
            "l_turn_m": l_turn,
        })
    if not layouts:
        raise ValueError("параллельные кабели не укладываются в окно")
    return min(layouts, key=lambda x: (x["b_winding_m"], x["l_turn_m"],
                                       x["parallel_radial"]))


def radial_space(core: Core) -> float:
    return core.radial_window


def _worst_peak_current(mode: Mode, L_min: float, load_tol: float) -> Tuple[float, Dict]:
    values = []
    for case in mode.cases:
        d_i = case["lambda_plus_Vs"] / L_min
        peak = case["I_dc_A"] * (1.0 + load_tol) + d_i / 2.0
        values.append((peak, case, d_i))
    peak, case, d_i = max(values, key=lambda x: x[0])
    return peak, {**case, "dI_actual_A": d_i, "I_peak_design_A": peak}


def _worst_magnetic_corner(mode: Mode, L_min: float, L_max: float,
                           load_tol: float, n_turns: int,
                           A_min: float) -> Tuple[float, Dict]:
    values = []
    for inductance, label in ((L_min, "L_min"), (L_max, "L_max")):
        for case in mode.cases:
            d_i = case["lambda_plus_Vs"] / inductance
            peak = case["I_dc_A"] * (1.0 + load_tol) + d_i / 2.0
            flux_linkage = inductance * peak
            B = flux_linkage / (n_turns * A_min)
            values.append((B, {**case, "L_case_H": inductance,
                               "L_tolerance_case": label,
                               "dI_actual_A": d_i,
                               "I_peak_design_A": peak,
                               "flux_linkage_Wb_turn": flux_linkage}))
    return max(values, key=lambda x: x[0])


def _mode_at_case(mode: Mode, case: Dict, inductance: float,
                  load_factor: float) -> Mode:
    d_i = case["lambda_plus_Vs"] / inductance
    i_dc = case["I_dc_A"] * load_factor
    i_ac = d_i / (2.0 * math.sqrt(3.0))
    i_rms = math.sqrt(i_dc ** 2 + i_ac ** 2)
    D = case["D"]
    period = 1.0 / mode.f_sw
    slope_on = d_i / (D * period)
    slope_off = d_i / ((1.0 - D) * period)
    slope_rms = math.sqrt(D * slope_on ** 2 + (1.0 - D) * slope_off ** 2)
    f_eff = slope_rms / (2.0 * math.pi * i_rms)
    return replace(
        mode, D=D, u_in=case["u_in_V"], u_out=case["u_out_V"],
        I_dc=i_dc, dI_pp=d_i, I_min=i_dc - d_i / 2.0,
        I_max=i_dc + d_i / 2.0, I_ac_rms=i_ac, I_rms=i_rms,
        lam_plus=case["lambda_plus_Vs"], f_eff=f_eff,
    )


def evaluate_candidate(tz: TZ, core: Core, mat: Material, litz: Litz, mode: Mode,
                       n_turns: int, part_number: str = "",
                       gap_catalog: Optional[float] = None,
                       A_L_catalog: Optional[float] = None,
                       n_gaps: int = 1,
                       A_L_tolerance: Optional[float] = None) -> Candidate:
    """Полный аналитический расчёт варианта."""

    L_target = mode.L_req / (1.0 - tz.tol_L)
    A_L_req = L_target / n_turns ** 2
    A_L0 = core.A_L0_of(mat.name)
    if A_L0 <= 0.0:
        raise ValueError(f"нет A_L0 для {core.name}/{mat.name}")

    q_bounds = core.q_fringe_bounds if min(core.q_fringe_bounds) > 0.0 else (0.85, 0.95)
    G_bounds = core.G_gap_bounds if min(core.G_gap_bounds) > 0.0 else (core.G_gap, core.G_gap)
    q_model = sum(q_bounds) / 2.0
    G_model = sum(G_bounds) / 2.0

    if A_L_catalog is None:
        gap, fringe, gap_iters = gap_for_AL(
            A_L_req, core, q_model, n_gaps, A_L0=A_L0, G_gap=G_model)
        A_L_actual = AL_from_gap(
            gap, core, q_model, n_gaps, A_L0, G_gap=G_model)
        bounded = [gap_for_AL(A_L_req, core, q, n_gaps,
                              A_L0=A_L0, G_gap=G)[:2]
                   for q in q_bounds for G in G_bounds]
        gap_min = min(x[0] for x in bounded)
        gap_max = max(x[0] for x in bounded)
        fringe_min = min(x[1] for x in bounded)
        fringe_max = max(x[1] for x in bounded)
        al_tol = tz.tol_L
        construction = "custom_gap"
        L_nom = A_L_actual * n_turns ** 2
    else:
        A_L_actual = A_L_catalog
        al_tol = tz.tol_L if A_L_tolerance is None else A_L_tolerance
        gap = gap_catalog or 0.0
        fringe = (fringing_factor(gap / n_gaps, core.A_g, G_model, q_model)
                   if gap > 0.0 and core.A_g and core.G_gap else 1.0)
        gap_min = gap_max = gap
        fringe_min = fringe_max = fringe
        gap_iters = 0
        construction = "catalog_gap"
        L_nom = A_L_actual * n_turns ** 2

    L_min = L_nom * (1.0 - al_tol)
    L_max = L_nom * (1.0 + al_tol)
    B_wc, magnetic_corner = _worst_magnetic_corner(
        mode, L_min, L_max, tz.tol_i_load, n_turns, core.A_min)
    d_i_nom = mode.lam_plus / L_nom
    i_peak_nom = mode.I_dc + d_i_nom / 2.0
    B_nom = L_nom * i_peak_nom / (n_turns * core.A_min)
    B_allow = tz.k_B_prelim * mat.B_S(tz.t_core_max)
    dB_pp = mode.lambda_max / (n_turns * core.A_e)
    B_ac_pk = dB_pp / 2.0

    r_gap = tz.gap_clearance
    gap_keepout_half = gap_max / (2.0 * n_gaps) + r_gap
    layout = winding_geometry(tz, core, litz, n_turns, gap_keepout_half)
    l_turn = layout["l_turn_m"]
    b_winding = layout["b_winding_m"]
    n_layers = float(layout["n_layers"])
    h_wind = layout["h_wind_m"]
    axial_fraction = h_wind / core.h_window
    radial_fraction = layout["radial_available_m"] / core.radial_window
    A_N_eff = core.A_N * axial_fraction * radial_fraction
    k_cu = n_turns * litz.S_cu / A_N_eff
    k_zan = n_turns * litz.S_out / A_N_eff
    k_R = reluctance_ratio(A_L_actual, core, A_L0)
    # При постоянной мощности I_DC монотонно максимален при U_in,min.
    # В заданном диапазоне U_in > U_out/2, поэтому lambda=u_in·(1-u_in/u_out)/f
    # также максимальна при U_in,min и U_out,max. Один и тот же угол является
    # худшим как для потерь в меди, так и для размаха B.
    thermal_case = max(mode.cases,
                       key=lambda x: (x["I_dc_A"], x["lambda_plus_Vs"]))
    corner_mode = _mode_at_case(mode, thermal_case, L_min, 1.0 + tz.tol_i_load)
    dB_case = thermal_case["lambda_plus_Vs"] / (n_turns * core.A_e)
    thermal = solve_thermal(tz, core, mat, litz, n_turns, l_turn,
                            corner_mode, dB_case, h_wind)
    thermal["operating_case"] = thermal_case["label"]
    thermal["case_selection"] = "max_I_dc_and_max_lambda_in_enumerated_voltage_corners"
    thermal["L_case_H"] = L_min
    thermal["load_factor"] = 1.0 + tz.tol_i_load
    thermal["dB_pp_T"] = dB_case
    C_self = self_capacitance(n_turns, l_turn, litz.d_outer, n_layers)
    f_res = resonance_frequency(L_max, C_self)
    C_max = C_self_max(L_max, tz.f_treb_max(mode.f_sw), tz.k_f_res)
    cand = Candidate(
        core=core, mat=mat, litz=litz, mode=mode, n_turns=n_turns,
        part_number=part_number or f"{core.name} (зазор на заказ)",
        A_L_req=A_L_req, A_L_actual=A_L_actual, gap=gap,
        gap_catalog=gap_catalog, F_fringe=fringe, gap_iters=gap_iters,
        L_nom=L_nom, L_min=L_min, L_max=L_max, B_max_nom=B_nom,
        B_max_wc=B_wc, B_allow=B_allow, B_ac_pk=B_ac_pk, dB_pp=dB_pp,
        k_cu=k_cu, k_zan=k_zan, n_layers=n_layers, l_turn=l_turn,
        b_winding=b_winding, k_R=k_R, C_self=C_self, f_res=f_res,
        C_self_max=C_max, thermal=thermal, r_gap=r_gap, h_wind=h_wind,
        n_gaps=n_gaps, A_L_tolerance=al_tol, construction=construction,
        gap_min=gap_min, gap_max=gap_max,
        F_fringe_min=fringe_min, F_fringe_max=fringe_max,
        q_fringe=q_model, G_gap_model=G_model,
        winding_layout=layout, magnetic_corner=magnetic_corner,
    )
    cand.margins = check_constraints(tz, cand)
    return cand


def _criterion(name: str, value: Optional[float], limit: Optional[float], unit: str,
               cmp: str, ok: Optional[bool], status: str = "calculated") -> Dict:
    margin = None
    if value is not None and limit not in (None, 0.0):
        margin = ((value / limit - 1.0) if cmp == ">=" else (1.0 - value / limit)) * 100.0
    return {"name": name, "value": value, "limit": limit, "unit": unit,
            "margin_pct": margin, "ok": ok, "cmp": cmp, "status": status}


def check_constraints(tz: TZ, c: Candidate) -> Dict:
    """Аналитические ограничения и отдельный реестр финальных проверок."""

    m: Dict[str, Dict] = {}
    m["L_nom_tol"] = _criterion("Минимальная индуктивность с допуском", c.L_min,
                                  c.mode.L_req, "Гн", ">=", c.L_min >= c.mode.L_req)
    m["L_diff"] = _criterion("Минимальная дифференциальная индуктивность", None,
                               c.mode.L_req, "Гн", ">=", None, "pending_fem_or_measurement")
    m["B_prelim"] = _criterion("Предварительная аналитическая индукция", c.B_max_wc,
                                 c.B_allow, "Тл", "<=", c.B_max_wc <= c.B_allow)
    m["B_fem"] = _criterion("Локальный максимум B с физическим радиусом кромки",
                              None, tz.k_B * c.mat.B_S(tz.t_core_max), "Тл", "<=",
                              None, "pending_converged_fem")
    m["t_winding"] = _criterion("Температура обмотки (предварительно)",
                                  c.thermal["t_winding_C"],
                                  min(tz.t_wind_max, c.litz.t_index), "°C", "<=",
                                  c.thermal["t_winding_C"] <= min(tz.t_wind_max, c.litz.t_index),
                                  "preliminary_thermal_model")
    m["t_core"] = _criterion("Температура сердечника (предварительно)",
                               c.thermal["t_core_C"], tz.t_core_max, "°C", "<=",
                               c.thermal["t_core_C"] <= tz.t_core_max,
                               "preliminary_thermal_model")
    current_density = c.thermal["I_rms_A"] / c.litz.S_cu
    m["current_density"] = _criterion(
        "Плотность тока после предварительной тепловой проверки",
        current_density, tz.j_final_max, "А/м²", "<=",
        current_density <= tz.j_final_max,
        "natural_convection_after_preliminary_thermal_check")
    m["k_cu"] = _criterion("Коэффициент заполнения окна медью", c.k_cu,
                             tz.k_cu_dop, "—", "<=", c.k_cu <= tz.k_cu_dop)
    m["k_zan"] = _criterion("Геометрическая занятость окна", c.k_zan,
                              tz.k_zan_dop, "—", "<=", c.k_zan <= tz.k_zan_dop)
    b_avail = radial_space(c.core) * 0.90
    m["b_radial"] = _criterion("Радиальная ширина обмотки", c.b_winding,
                                 b_avail, "м", "<=", c.b_winding <= b_avail)
    f_req = tz.k_f_res * tz.f_treb_max(c.mode.f_sw)
    m["f_res"] = _criterion("Первая собственная частота (оценка)", c.f_res,
                              f_req, "Гц", ">=", c.f_res >= f_req, "preliminary_model")
    m["k_R"] = _criterion("Отношение сопротивления зазора к сердечнику", c.k_R,
                             tz.k_reluctance_min, "—", ">=",
                             c.k_R >= tz.k_reluctance_min)
    m["harmonics"] = _criterion("Полнота спектра тока",
                                   c.thermal["spectrum_rms_ratio"], 0.999,
                                   "—", ">=",
                                   c.thermal["spectrum_rms_ratio"] >= 0.999,
                                   "calculated_80_harmonics")
    m["gap_field_loss"] = _criterion(
        "Дополнительные потери меди в поле зазора", None, None, "Вт", "<=",
        None, "pending_converged_fem")
    m["EMC"] = _criterion("Запас ЭМС во всей нормируемой полосе", None,
                            tz.M_EMC, "дБ", ">=", None, "pending_measurement")
    counted = [m[k] for k in ("L_nom_tol", "B_prelim", "t_winding", "t_core",
                              "current_density",
                              "k_cu", "k_zan", "b_radial", "f_res", "k_R",
                              "harmonics")]
    m["_analytical_ok"] = all(bool(x["ok"]) for x in counted)
    m["_all_ok"] = False
    m["_final_verified"] = False
    return m


def prescreen(tz: TZ, core: Core, mat: Material, litz: Litz, mode: Mode,
              n_turns: int, A_L: float, al_tol: Optional[float] = None) -> bool:
    tol = tz.tol_L if al_tol is None else al_tol
    L_nom = A_L * n_turns ** 2
    L_min = L_nom * (1.0 - tol)
    L_max = L_nom * (1.0 + tol)
    if L_min < mode.L_req:
        return False
    if L_nom > mode.L_req * 2.5:
        return False
    B_wc, _ = _worst_magnetic_corner(
        mode, L_min, L_max, tz.tol_i_load, n_turns, core.A_min)
    if B_wc > tz.k_B_prelim * mat.B_S(tz.t_core_max):
        return False
    if n_turns * litz.S_cu / core.A_N > tz.k_cu_dop:
        return False
    if n_turns * litz.S_out / core.A_N > tz.k_zan_dop:
        return False
    try:
        layout = winding_geometry(tz, core, litz, n_turns, tz.gap_clearance)
    except ValueError:
        return False
    A_N_eff = (core.A_N * layout["h_wind_m"] / core.h_window
               * layout["radial_available_m"] / core.radial_window)
    if n_turns * litz.S_cu / A_N_eff > tz.k_cu_dop:
        return False
    if n_turns * litz.S_out / A_N_eff > tz.k_zan_dop:
        return False
    return (reluctance_ratio(A_L, core, core.A_L0_of(mat.name))
            >= tz.k_reluctance_min)


def enumerate_candidates(tz: TZ, mode: Mode, cores: Dict[str, Core],
                         mats: Dict[str, Material], litzes: Dict[str, Litz],
                         n_par_range: Tuple[int, ...] = tuple(range(1, 13))) -> Tuple[List[Candidate], int]:
    out: List[Candidate] = []
    n_seen = 0
    for core in cores.values():
        for mat in mats.values():
            if not (mat.f_min <= mode.f_sw <= mat.f_max) or core.A_L0_of(mat.name) <= 0.0:
                continue
            n_b = math.ceil(mode.psi_max / (core.A_min * tz.k_B_prelim * mat.B_S(tz.t_core_max)))
            for base in litzes.values():
                for n_par in n_par_range:
                    litz = Litz(**{**asdict(base), "n_parallel": n_par})
                    n_w = math.floor(tz.k_zan_dop * core.A_N / litz.S_out)
                    if n_w < n_b:
                        continue
                    for n in range(max(1, n_b), n_w + 1):
                        for pn, (al, gap, al_tol) in core.gapped.items():
                            if core.gapped_material.get(pn) not in ("", mat.name):
                                continue
                            n_seen += 1
                            if prescreen(tz, core, mat, litz, mode, n, al, al_tol):
                                try:
                                    out.append(evaluate_candidate(tz, core, mat, litz, mode, n,
                                                 pn, gap, al, 1, al_tol))
                                except ValueError:
                                    pass
                        if core.A_g is not None:
                            al = mode.L_req / (1.0 - tz.tol_L) / n ** 2
                            n_seen += 1
                            if prescreen(tz, core, mat, litz, mode, n, al, tz.tol_L):
                                for n_gaps in tz.n_gaps_list:
                                    try:
                                        out.append(evaluate_candidate(tz, core, mat, litz, mode, n,
                                                     f"{core.name} (зазор на заказ)", n_gaps=n_gaps))
                                    except ValueError:
                                        pass
    return out, n_seen


def _dominates(a: Candidate, b: Candidate) -> bool:
    av = (a.thermal["P_total_W"], a.core.mass, a.C_self)
    bv = (b.thermal["P_total_W"], b.core.mass, b.C_self)
    return all(x <= y for x, y in zip(av, bv)) and any(x < y for x, y in zip(av, bv))


def pareto_select(cands: List[Candidate], loss_window: float = 0.02,
                  preferred_families: Tuple[str, ...] = ("EQ", "ETD", "PM", "PQ", "RM", "EER")
                  ) -> Tuple[Optional[Candidate], List[Candidate]]:
    feasible = [c for c in cands if c.margins["_analytical_ok"]]
    if not feasible:
        return None, []
    preferred = [c for c in feasible if c.core.family in preferred_families]
    # ТЗ требует использовать прямоугольный E только в последнюю очередь.
    # Поэтому E участвует в сравнении, но попадает в оптимизацию лишь при
    # отсутствии аналитически допустимого кандидата предпочтительного семейства.
    selection_pool = preferred or feasible
    # Инкрементальное построение фронта исключает квадратичное сравнение всех
    # десятков тысяч вариантов. Размер текущего фронта остаётся малым.
    ordered = sorted(selection_pool, key=lambda c: (c.thermal["P_total_W"],
                                               c.core.mass, c.C_self))
    front: List[Candidate] = []
    for candidate in ordered:
        cv = (candidate.thermal["P_total_W"], candidate.core.mass,
              candidate.C_self)
        if any(_dominates(other, candidate) or
               (other.thermal["P_total_W"], other.core.mass, other.C_self) == cv
               for other in front):
            continue
        front = [other for other in front if not _dominates(candidate, other)]
        front.append(candidate)
    p_min = min(c.thermal["P_total_W"] for c in selection_pool)
    window = [c for c in front if c.thermal["P_total_W"] <= p_min * (1.0 + loss_window)]
    if not window:
        window = [min(front, key=lambda c: c.thermal["P_total_W"])]

    def score(c: Candidate) -> Tuple[float, float]:
        margin = min(c.margins["B_prelim"]["margin_pct"], c.margins["L_nom_tol"]["margin_pct"])
        return margin, -c.thermal["P_total_W"]

    return max(window, key=score), front


def candidate_to_dict(c: Candidate, tz: Optional[TZ] = None) -> Dict:
    worst_peak, worst_case = _worst_peak_current(c.mode, c.L_min, 0.0)
    gap_model_al = None
    if c.gap > 0.0 and c.core.A_g is not None and c.F_fringe > 0.0:
        al0 = c.core.A_L0_of(c.mat.name)
        gap_model_al = 1.0 / (
            c.gap / (MU0 * c.core.A_g * c.F_fringe) + 1.0 / al0
        )
    return {
        "core": {
            "key": c.core.db_key, "name": c.core.name, "family": c.core.family,
            "shape": c.core.shape, "part_number": c.part_number,
            "A_e_mm2": c.core.A_e * 1e6, "A_min_mm2": c.core.A_min * 1e6,
            "A_g_mm2": c.core.A_g * 1e6 if c.core.A_g is not None else None,
            "A_g_source": c.core.A_g_source, "gap_surface": c.core.gap_surface,
            "G_gap_mm": c.G_gap_model * 1e3,
            "G_gap_bounds_mm": [x * 1e3 for x in c.core.G_gap_bounds],
            "q_fringe_bounds": list(c.core.q_fringe_bounds),
            "l_e_mm": c.core.l_e * 1e3, "V_e_mm3": c.core.V_e * 1e9,
            "A_L0_nH": c.core.A_L0_of(c.mat.name) * 1e9,
            "part_ungapped": c.core.part_ungapped.get(c.mat.name),
            "mass_kg": c.core.mass, "A_N_mm2": c.core.A_N * 1e6,
            "l_N_mm": c.core.l_N * 1e3, "h_window_mm": c.core.h_window * 1e3,
            "outer_width_mm": c.core.outer_width * 1e3,
            "set_height_mm": c.core.set_height * 1e3,
            "depth_mm": c.core.depth * 1e3,
            "d_center_mm": c.core.d_center * 1e3,
            "d_bore_mm": c.core.d_bore * 1e3,
            "radial_window_mm": c.core.radial_window * 1e3,
            "datasheet": c.core.datasheet,
        },
        "material": {
            "name": c.mat.name, "B_S_100_T": c.mat.B_S_100,
            "mu_i": c.mat.mu_i, "datasheet": c.mat.datasheet,
            "steinmetz_fit_limitation": c.mat.fit_limitation,
        },
        "wire": {
            "key": c.litz.db_key, "designation": c.litz.designation,
            "n_strands": c.litz.n_strands, "d_strand_mm": c.litz.d_strand * 1e3,
            "n_parallel": c.litz.n_parallel, "S_cu_mm2": c.litz.S_cu * 1e6,
            "d_outer_mm": c.litz.d_outer * 1e3, "std": c.litz.std,
            "t_index_C": c.litz.t_index, "price": c.litz.price,
            "price_unit": c.litz.price_unit, "url": c.litz.url,
        },
        "mode": {
            "f_sw_kHz": c.mode.f_sw / 1e3, "D": c.mode.D,
            "D_ideal": c.mode.D_ideal, "p_in_W": c.mode.p_in,
            "u_in_V": c.mode.u_in, "u_out_V": c.mode.u_out,
            "volt_second_error_V": c.mode.volt_second_error,
            "I_dc_A": c.mode.I_dc, "dI_pp_A": c.mode.dI_pp,
            "I_max_A": c.mode.I_max, "I_min_A": c.mode.I_min,
            "I_rms_A": c.mode.I_rms, "I_ac_rms_A": c.mode.I_ac_rms,
            "L_req_uH": c.mode.L_req * 1e6, "lam_plus_mVs": c.mode.lam_plus * 1e3,
            "lambda_max_mVs": c.mode.lambda_max * 1e3,
            "psi_max_mWb": c.mode.psi_max * 1e3, "W_max_mJ": c.mode.W_max * 1e3,
            "f_eff_kHz": c.mode.f_eff / 1e3, "case_L": c.mode.case_L,
            "case_I": c.mode.case_I, "cases": c.mode.cases,
            "electrical_model": "ideal_boost_preliminary_without_semiconductor_or_Rdc_voltage_drop",
        },
        "design": {
            "N": c.n_turns, "construction": c.construction,
            "A_L_req_nH": c.A_L_req * 1e9, "A_L_actual_nH": c.A_L_actual * 1e9,
            "A_L_tolerance_pct": c.A_L_tolerance * 100.0,
            "A_L_gap_model_nH": gap_model_al * 1e9 if gap_model_al is not None else None,
            "L_gap_model_uH": (gap_model_al * c.n_turns ** 2 * 1e6
                               if gap_model_al is not None else None),
            "gap_model_delta_pct": (100.0 * (c.A_L_actual / gap_model_al - 1.0)
                                    if gap_model_al is not None else None),
            "gap_mm": c.gap * 1e3,
            "gap_model_min_mm": c.gap_min * 1e3,
            "gap_model_max_mm": c.gap_max * 1e3,
            "gap_specification": "изготовить по целевому A_L; размер g является расчётной оценкой",
            "gap_catalog_mm": c.gap_catalog * 1e3 if c.gap_catalog is not None else None,
            "F_fringe": c.F_fringe,
            "F_fringe_min": c.F_fringe_min,
            "F_fringe_max": c.F_fringe_max,
            "q_fringe_model": c.q_fringe,
            "G_gap_model_mm": c.G_gap_model * 1e3,
            "gap_iters": c.gap_iters,
            "L_nom_uH": c.L_nom * 1e6, "L_min_uH": c.L_min * 1e6,
            "L_max_uH": c.L_max * 1e6, "k_R": c.k_R,
            "B_max_nom_mT": c.B_max_nom * 1e3, "B_max_wc_mT": c.B_max_wc * 1e3,
            "B_allow_mT": c.B_allow * 1e3, "B_ac_pk_mT": c.B_ac_pk * 1e3,
            "dB_pp_mT": c.dB_pp * 1e3, "I_peak_worst_no_load_tol_A": worst_peak,
            "worst_case": worst_case, "magnetic_worst_case": c.magnetic_corner,
            "k_cu": c.k_cu, "k_zan": c.k_zan,
            "current_density_A_mm2": c.thermal["I_rms_A"] / c.litz.S_cu / 1e6,
            "current_density_limit_A_mm2": (tz.j_final_max if tz else 3.0e6) / 1e6,
            "required_copper_area_prelim_mm2": (
                c.thermal["I_rms_A"] / (tz.j_prelim if tz else 2.5e6) * 1e6),
            "n_layers": c.n_layers, "l_turn_mm": c.l_turn * 1e3,
            "b_winding_mm": c.b_winding * 1e3,
            "wire_length_m": c.n_turns * c.l_turn,
            "wire_length_total_m": c.n_turns * c.l_turn * c.litz.n_parallel,
            "n_gaps": c.n_gaps, "gap_per_section_mm": c.gap / c.n_gaps * 1e3,
            "r_gap_mm": c.r_gap * 1e3, "h_wind_mm": c.h_wind * 1e3,
            "winding_layout": {
                (key[:-2] + "_mm" if key.endswith("_m") else key):
                (value * 1e3 if key.endswith("_m") else value)
                for key, value in c.winding_layout.items()
            },
            "C_self_pF": c.C_self * 1e12, "f_res_MHz": c.f_res / 1e6,
            "C_self_max_pF": c.C_self_max * 1e12,
        },
        "emc": {
            "status": "pending_measurement",
            "A_Z_model_dB": {f"{f / 1e3:.0f}kHz": impedance_attenuation(
                c.L_min, c.C_self, f, R=c.thermal["R_dc_Ohm"])
                for f in (150e3, 500e3, 1e6, 5e6, 10e6, 30e6)},
        },
        "losses": {k: v for k, v in c.thermal.items() if k != "harmonics"},
        "harmonics": c.thermal["harmonics"],
        "margins": c.margins,
        "verification": {
            "analytical_pass": c.margins["_analytical_ok"],
            "final_verified": False,
            "pending": ["tune custom gap by measured A_L", "L_diff(I)",
                        "FEM B with physical edge radius", "FEM copper loss near gap",
                        "thermal prototype", "self-resonance measurement", "EMC measurement"],
        },
    }


def turn_window_screening(tz: TZ, mode: Mode, cores: Dict[str, Core],
                          materials: Dict[str, Material]) -> List[Dict]:
    """Численный предварительный отсев типоразмеров по N_B и N_w."""

    material = max(
        (m for m in materials.values() if m.f_min <= mode.f_sw <= m.f_max),
        key=lambda m: m.B_S(tz.t_core_max))
    b_prelim = tz.k_B_prelim * material.B_S(tz.t_core_max)
    worst_i_rms = max(math.sqrt(
        (case["I_dc_A"] * (1.0 + tz.tol_i_load)) ** 2
        + case["dI_limit_A"] ** 2 / 12.0)
        for case in mode.cases)
    s_cu = worst_i_rms / tz.j_prelim
    s_slot = s_cu / tz.k_zan_dop
    rows: List[Dict] = []
    names = set()
    for core in cores.values():
        names.add(core.name)
        rows.append({"core": core.name, "family": core.family,
                     "A_min_mm2": core.A_min * 1e6,
                     "A_N_mm2": core.A_N * 1e6,
                     "source": core.datasheet,
                     "full_enumeration": True})
    for item in (_load_json("cores.json").get("screened_out", {}).get("candidates") or []):
        if item["name"] not in names:
            rows.append({"core": item["name"], "family": item["family"],
                         "A_min_mm2": item["A_min_mm2"],
                         "A_N_mm2": item["A_N_mm2"],
                         "source": item["source"],
                         "full_enumeration": False})
    for row in rows:
        n_b = math.ceil(mode.psi_max / (row["A_min_mm2"] * 1e-6 * b_prelim))
        n_w = math.floor(row["A_N_mm2"] * 1e-6 / s_slot)
        row.update({
            "A_min_A_N_mm4": row["A_min_mm2"] * row["A_N_mm2"],
            "N_by_induction": n_b, "N_by_window": n_w,
            "ok": n_w >= n_b,
            "verdict": ("проходит предварительный отбор" if n_w >= n_b else
                        f"окно вмещает {n_w} витков против {n_b} требуемых по индукции"),
        })
    rows.append({"_criteria": {
        "material": material.name, "B_prelim_mT": b_prelim * 1e3,
        "psi_max_mWb": mode.psi_max * 1e3,
        "N_A_min_required_mm2": mode.psi_max / b_prelim * 1e6,
        "I_rms_worst_A": worst_i_rms,
        "S_cu_per_turn_mm2": s_cu * 1e6,
        "S_slot_per_turn_mm2": s_slot * 1e6,
        "J_dop_A_mm2": tz.j_prelim / 1e6,
        "k_zan_dop": tz.k_zan_dop,
    }})
    return rows


def area_product_screening(tz: TZ, mode: Mode, cores: Dict[str, Core],
                           materials: Dict[str, Material]) -> List[Dict]:
    """Предварительный фильтр A_e·A_w по размерно однородной формуле."""

    material = max(
        (m for m in materials.values() if m.f_min <= mode.f_sw <= m.f_max),
        key=lambda m: m.B_S(tz.t_core_max))
    b_m = tz.k_B_prelim * material.B_S(tz.t_core_max)
    i_rms = math.sqrt(mode.I_dc_max ** 2
                      + (tz.r_i * mode.I_dc_max) ** 2 / 12.0)
    k_peak = mode.I_peak_design / i_rms
    ap_req = 2.0 * mode.W_max / (
        k_peak * tz.k_w_prelim * b_m * tz.j_prelim)
    rows = [{
        "core": core.name, "family": core.family,
        "A_e_mm2": core.A_e * 1e6, "A_w_mm2": core.A_N * 1e6,
        "Ap_catalog_mm4": core.A_e * core.A_N * 1e12,
        "Ap_required_mm4": ap_req * 1e12,
        "ok": core.A_e * core.A_N >= ap_req,
        "custom_gap_possible": core.A_g is not None,
        "catalog_gap_count": len(core.gapped),
    } for core in cores.values()]
    rows.append({"_criteria": {
        "material": material.name, "B_prelim_mT": b_m * 1e3,
        "k_peak": k_peak, "k_w": tz.k_w_prelim,
        "J_A_mm2": tz.j_prelim / 1e6,
        "W_max_mJ": mode.W_max * 1e3,
        "Ap_required_mm4": ap_req * 1e12,
    }})
    return rows


def _failure_summary(candidates: List[Candidate]) -> Tuple[Optional[Candidate], List[Dict]]:
    if not candidates:
        return None, []
    def key(candidate: Candidate) -> Tuple[int, float, float]:
        failed = [value for value in candidate.margins.values()
                  if isinstance(value, dict) and value.get("ok") is False]
        violation = sum(max(0.0, -(value.get("margin_pct") or 0.0)) for value in failed)
        return len(failed), violation, candidate.thermal["P_total_W"]
    nearest = min(candidates, key=key)
    failed_rows = [value for value in nearest.margins.values()
                   if isinstance(value, dict) and value.get("ok") is False]
    return nearest, failed_rows


def core_material_comparison(cores: Dict[str, Core], materials: Dict[str, Material],
                             candidates: List[Candidate], mode: Mode,
                             tz: Optional[TZ] = None) -> List[Dict]:
    def limit_text(item: Dict) -> str:
        value, limit, unit = item["value"], item["limit"], item["unit"]
        if unit == "А/м²":
            value, limit, unit = value / 1e6, limit / 1e6, "А/мм²"
        elif unit == "Гн":
            value, limit, unit = value * 1e6, limit * 1e6, "мкГн"
        elif unit == "м":
            value, limit, unit = value * 1e3, limit * 1e3, "мм"
        return f"{item['name']}: {value:.4g} {unit} при пределе {limit:.4g} {unit}"

    rows: List[Dict] = []
    for core in cores.values():
        for material in materials.values():
            subset = [candidate for candidate in candidates
                      if candidate.core.db_key == core.db_key and candidate.mat.name == material.name]
            feasible = [candidate for candidate in subset if candidate.margins["_analytical_ok"]]
            best = min(feasible, key=lambda x: x.thermal["P_total_W"]) if feasible else None
            nearest, failed = _failure_summary(subset)
            if not (material.f_min <= mode.f_sw <= material.f_max):
                reason = "частота вне паспортного диапазона материала"
            elif core.A_L0_of(material.name) <= 0.0:
                reason = "нет паспортного A_L0 для сочетания сердечник–материал"
            elif not subset:
                reason = "нет рассчитанного варианта после предварительного отсева"
            elif not feasible:
                reason = "; ".join(limit_text(item) for item in failed
                                   if item.get("value") is not None
                                   and item.get("limit") is not None)
            else:
                reason = "аналитические ограничения выполнены"
            rows.append({
                "core": core.name, "family": core.family, "material": material.name,
                "n_evaluated": len(subset), "n_feasible": len(feasible),
                "status": "analytical_pass" if best else "rejected",
                "reason": reason,
                "best": candidate_to_dict(best, tz) if best else None,
                "nearest_rejected": candidate_to_dict(nearest, tz) if nearest and not best else None,
            })
    return rows


def material_comparison_for_selected(best: Candidate, tz: TZ,
                                     materials: Dict[str, Material]) -> Dict:
    rows: Dict[str, Dict] = {}
    for material in materials.values():
        row: Dict = {"in_range": material.f_min <= best.mode.f_sw <= material.f_max,
                     "f_range_kHz": [material.f_min / 1e3, material.f_max / 1e3]}
        if not row["in_range"]:
            row["status"] = "частота вне паспортного диапазона"
        elif best.core.A_L0_of(material.name) <= 0.0:
            row["status"] = "материал не выпускается в выбранном типоразмере"
        else:
            try:
                candidate = evaluate_candidate(tz, best.core, material, best.litz,
                                               best.mode, best.n_turns, n_gaps=1)
                row.update({"B_allow_mT": candidate.B_allow * 1e3,
                            "B_max_wc_mT": candidate.B_max_wc * 1e3,
                            "P_fe_W": candidate.thermal["P_fe_W"],
                            "P_total_W": candidate.thermal["P_total_W"],
                            "analytical_ok": candidate.margins["_analytical_ok"]})
            except ValueError as exc:
                row["status"] = str(exc)
        rows[material.name] = row
    return rows


def fmt(value: float, digits: int = 3) -> str:
    return f"{value:.{digits}f}".replace(".", ",")


def frequency_key(frequency_hz: float) -> str:
    """Сформировать устойчивый JSON-ключ без округления дробной частоты."""
    value = f"{frequency_hz / 1e3:.6f}".rstrip("0").rstrip(".")
    return f"{value.replace('.', 'p')}kHz"


def main() -> None:
    tz = load_tz()
    cores = core_library()
    materials = material_library()
    litzes = litz_library()
    combined = {
        "meta": {
            "schema_version": "1.0",
            "status": "analytical_preliminary",
            "final_verification": False,
            "project": dict(PROJECT_CONFIG.get("project", {})),
            "config": PROJECT_CONFIG,
            "topology": PROJECT_CONFIG.get("project", {}).get(
                "single_topology", "single_boost_inductor_one_physical_gap"),
            "methodology": os.path.join(PROJECT_ROOT, "0_references",
                                        "Metodika_VCh_silovykh_drosseley_bez_rascheta.tex"),
            "database": DB_ROOT,
            "assumptions": [
                f"P_out={tz.p_out_nom:g} W имеет приоритет при расхождении с "
                f"U_out·I_out={tz.u_out_nom * tz.i_out_nom:g} W",
                "идеальная boost-модель напряжения; падения на ключе, диоде и Rdc не включены",
                "один физический зазор расположен на центральном стержне",
                "зазор заказывается по целевому A_L; размер g уточняется по МКЭ и измерению",
                "отступ меди от ближайшей кромки зазора 5 мм принят конструктивно до МКЭ потерь",
            ],
        },
        "tz": asdict(tz),
        "materials": {
            name: {
                "name": material.name, "mu_i": material.mu_i,
                "B_S_25_T": material.B_S_25, "B_S_100_T": material.B_S_100,
                "f_min_Hz": material.f_min, "f_max_Hz": material.f_max,
                "k_st": material.k_st, "alpha": material.alpha,
                "beta": material.beta, "datasheet": material.datasheet,
                "fit_limitation": material.fit_limitation,
            } for name, material in materials.items()
        },
        "results": {},
    }
    for f_sw in tz.f_sw_list:
        mode = compute_mode(tz, f_sw)
        candidates, seen = enumerate_candidates(tz, mode, cores, materials, litzes)
        best, front = pareto_select(candidates, tz.loss_window,
                                    tz.preferred_core_families)
        feasible = [candidate for candidate in candidates if candidate.margins["_analytical_ok"]]
        preferred = [candidate for candidate in feasible
                     if candidate.core.family in tz.preferred_core_families]
        selection_pool = preferred or feasible
        p_min = min((candidate.thermal["P_total_W"] for candidate in selection_pool), default=None)
        n_loss_window = sum(
            candidate.thermal["P_total_W"] <= p_min * (1.0 + tz.loss_window)
            for candidate in selection_pool) if p_min is not None else 0
        screening = turn_window_screening(tz, mode, cores, materials)
        ap_screening = area_product_screening(tz, mode, cores, materials)
        comparison = core_material_comparison(cores, materials, candidates, mode, tz)
        key = frequency_key(f_sw)
        if best is None:
            print(f"{f_sw / 1e3:.0f} кГц: аналитически допустимых вариантов нет")
            combined["results"][key] = {
                "status": "no_analytical_solution",
                "n_seen": seen,
                "n_evaluated": len(candidates),
                "n_feasible": 0,
                "turn_window_screening": screening,
                "area_product_screening": ap_screening,
                "core_material_table": comparison,
            }
            continue
        path = os.path.join(HERE, f"results_{key}.json")
        selected = candidate_to_dict(best, tz)
        payload = {
            "meta": {"status": "analytical_preliminary", "database": DB_ROOT,
                     "final_verification": False,
                     "n_seen": seen, "n_evaluated": len(candidates),
                     "pareto_size": len(front)},
            "tz": asdict(tz), "selected": selected,
        }
        with open(path, "w", encoding="utf-8") as stream:
            json.dump(payload, stream, ensure_ascii=False, indent=2)
        combined["results"][key] = {
            "status": "analytical_solution",
            "n_seen": seen,
            "n_evaluated": len(candidates),
            "pareto_size": len(front),
            "n_feasible": len(feasible),
            "n_loss_window": n_loss_window,
            "selection": {
                "policy": "предпочтительные EQ/ETD/PM/PQ/RM/EER; E только при отсутствии допустимого предпочтительного кандидата",
                "preferred_feasible": len(preferred),
                "fallback_E_used": not bool(preferred),
                "loss_window_pct": tz.loss_window * 100.0,
            },
            "quantities": {
                "inductors": 1, "core_sets": 1,
                "core_halves_per_set": 2, "core_halves_total": 2,
            },
            "turn_window_screening": screening,
            "area_product_screening": ap_screening,
            "core_material_table": comparison,
            "material_comparison": material_comparison_for_selected(best, tz, materials),
            "selected": selected,
        }
        print(f"{f_sw / 1e3:.0f} кГц: {best.core.name}/{best.mat.name}, "
              f"N={best.n_turns}, g={best.gap * 1e3:.3f} мм, "
              f"L={best.L_nom * 1e6:.2f} мкГн -> {path}")
    for name in ("results_single_gap.json", "results.json"):
        path = os.path.join(HERE, name)
        with open(path, "w", encoding="utf-8") as stream:
            json.dump(combined, stream, ensure_ascii=False, indent=2)
    print(f"сводный результат -> {os.path.join(HERE, 'results_single_gap.json')}")


if __name__ == "__main__":
    main()
