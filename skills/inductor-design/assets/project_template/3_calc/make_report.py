# -*- coding: utf-8 -*-
"""Генератор пояснительной записки для одиночного boost-дросселя.

Источник численных результатов — ``results_single_gap.json``. Полный
численный обзор вариантов магнитопроводов и материалов воспроизводится теми
же функциями перебора из ``inductor_design.py`` без изменения расчётного
скрипта или базы компонентов. Документ сохраняет структуру резервного отчёта,
но описывает только актуальную конструкцию с одним физическим зазором.
"""
from __future__ import annotations

import importlib.util
import json
import math
import re
from datetime import date
from pathlib import Path
from typing import Any, Dict, Iterable, List, Tuple

from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK, WD_TAB_ALIGNMENT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
JSON_PATH = HERE / "results_single_gap.json"
OUT_DIR = ROOT / "1_output_files"
OUT_PATH = OUT_DIR / "Расчёт_дросселя_boost.docx"
IMG_DIR = OUT_DIR / "img"
STYLE_MODULE = HERE / "report_style.py"


def _load_backup_helpers():
    """Загрузить только проверенные функции оформления резервного отчёта."""
    if not STYLE_MODULE.exists():
        raise FileNotFoundError(f"не найден модуль оформления: {STYLE_MODULE}")
    spec = importlib.util.spec_from_file_location("single_report_style", STYLE_MODULE)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"не удалось загрузить модуль оформления: {STYLE_MODULE}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


STYLE = _load_backup_helpers()
h1 = STYLE.h1
h2 = STYLE.h2
para = STYLE.para
table_caption = STYLE.table_caption
add_table = STYLE.add_table
add_figure = STYLE.add_figure

FONT = "Times New Roman"
SZ_MAIN = Pt(14)
FREQS: Tuple[Tuple[str, str], ...] = ()
REFS: Dict[str, int] = {}
PENDING_TRANSLATIONS = {
    "tune custom gap by measured A_L": "доводка зазора по измеренному A_L",
    "L_diff(I)": "измерение или МКЭ дифференциальной индуктивности L_diff(I)",
    "FEM B with physical edge radius":
        "МКЭ локальной индукции B с физическим радиусом кромки",
    "FEM copper loss near gap": "МКЭ добавочных потерь меди у зазора",
    "thermal prototype": "тепловые испытания прототипа",
    "self-resonance measurement": "измерение первого собственного резонанса",
    "EMC measurement": "измерение электромагнитной совместимости",
}


def setup_document():
    """Создать документ в стиле Backup и исправить его OOXML-поля."""
    doc = STYLE.setup_document()
    zoom = doc.settings.element.find(qn("w:zoom"))
    if zoom is not None and zoom.get(qn("w:percent")) is None:
        zoom.set(qn("w:percent"), "100")

    for section in doc.sections:
        footer = section.footer
        p = footer.paragraphs[0] if footer.paragraphs else footer.add_paragraph()
        p.clear()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.first_line_indent = Cm(0)
        run = p.add_run()
        run.font.name = FONT
        run.font.size = SZ_MAIN
        begin = OxmlElement("w:fldChar")
        begin.set(qn("w:fldCharType"), "begin")
        instruction = OxmlElement("w:instrText")
        instruction.set(qn("xml:space"), "preserve")
        instruction.text = " PAGE "
        separate = OxmlElement("w:fldChar")
        separate.set(qn("w:fldCharType"), "separate")
        end = OxmlElement("w:fldChar")
        end.set(qn("w:fldCharType"), "end")
        run._r.extend((begin, instruction, separate, end))
    return doc


def fmt(value: Any, digits: int = 2) -> str:
    """Форматировать число с десятичной запятой."""
    if value is None:
        return "—"
    if isinstance(value, bool):
        return "да" if value else "нет"
    if isinstance(value, int):
        return str(value)
    try:
        result = f"{float(value):.{digits}f}"
    except (TypeError, ValueError):
        return str(value)
    return result.replace(".", ",")


def frequency_label(frequency_hz: float) -> str:
    value = f"{frequency_hz / 1e3:.6f}".rstrip("0").rstrip(".")
    return value.replace(".", ",") + " кГц"


def report_text(value: Any) -> str:
    """Привести диагностический текст расчёта к обозначениям отчёта."""
    text = str(value or "—")
    text = re.sub(r"(?<=\d)\.(?=\d)", ",", text)
    for source, target in (
        ("°C", "°С"), ("A/mm²", "А/мм²"), ("A/mm2", "А/мм²"),
        ("uH", "мкГн"), ("µH", "мкГн"), ("mT", "мТл"),
    ):
        text = text.replace(source, target)
    return text


def pending_text(items: Iterable[str]) -> str:
    """Перевести служебные обозначения незакрытых проверок."""
    return "; ".join(PENDING_TRANSLATIONS.get(item, item) for item in items)


def eq(doc, number: List[int], expression: str) -> int:
    """Добавить формулу с центральным выражением и номером справа."""
    n = number[0]
    p = doc.add_paragraph()
    p.paragraph_format.first_line_indent = Cm(0)
    p.paragraph_format.space_before = Pt(6)
    p.paragraph_format.space_after = Pt(6)
    p.paragraph_format.tab_stops.add_tab_stop(Cm(8.2), WD_TAB_ALIGNMENT.CENTER)
    p.paragraph_format.tab_stops.add_tab_stop(Cm(17.0), WD_TAB_ALIGNMENT.RIGHT)
    p.alignment = WD_ALIGN_PARAGRAPH.LEFT
    p.add_run("\t")
    r = p.add_run(expression)
    r.font.name = FONT
    r.font.size = SZ_MAIN
    r.italic = True
    p.add_run("\t")
    r = p.add_run(f"({n})")
    r.font.name = FONT
    r.font.size = SZ_MAIN
    number[0] += 1
    return n


def substitution(doc, text: str) -> None:
    p = para(doc, text, indent=False, align=WD_ALIGN_PARAGRAPH.CENTER)
    p.paragraph_format.space_after = Pt(6)


def where(doc, definitions: Iterable[str]) -> None:
    """Добавить пояснения символов отдельными строками."""
    items = list(definitions)
    for index, item in enumerate(items):
        ending = "." if index == len(items) - 1 else ";"
        prefix = "где " if index == 0 else "      "
        p = para(doc, prefix + item + ending, indent=False,
                 align=WD_ALIGN_PARAGRAPH.LEFT)
        p.paragraph_format.left_indent = Cm(1.25)


def captioned_table(doc, tn: List[int], title: str, header: List[str],
                    rows: List[List[Any]], widths: List[float] | None = None,
                    ref: str | None = None):
    if ref:
        REFS[ref] = tn[0]
    table_caption(doc, tn[0], title)
    table = add_table(doc, header, rows, widths=widths)
    tn[0] += 1
    return table


def require_path(data: Dict[str, Any], path: Tuple[str, ...]) -> Any:
    cur: Any = data
    for key in path:
        if not isinstance(cur, dict) or key not in cur:
            raise KeyError("results_single_gap.json: отсутствует поле " + ".".join(path))
        cur = cur[key]
    return cur


def load_results() -> Dict[str, Any]:
    if not JSON_PATH.exists():
        raise FileNotFoundError(f"не найден файл результатов: {JSON_PATH}")
    with JSON_PATH.open(encoding="utf-8") as stream:
        data = json.load(stream)
    for path in (("meta",), ("tz",), ("results",)):
        require_path(data, path)
    if not data["results"]:
        raise ValueError("results_single_gap.json: отсутствуют частотные варианты")
    global FREQS
    frequency_rows = []
    for f_key, item in data["results"].items():
        require_path(item, ("selected",))
        f_hz = item.get("f_sw_Hz")
        if f_hz is None:
            f_hz = item["selected"]["mode"]["f_sw_kHz"] * 1e3
        frequency_rows.append((float(f_hz), f_key, frequency_label(float(f_hz))))
    FREQS = tuple((key, label) for _, key, label in sorted(frequency_rows))
    for f_key, _ in FREQS:
        for field_name in ("n_seen", "n_evaluated", "n_feasible", "pareto_size",
                           "n_loss_window", "selection", "area_product_screening",
                           "turn_window_screening", "core_material_table",
                           "material_comparison"):
            require_path(data["results"][f_key], (field_name,))
        selected = data["results"][f_key]["selected"]
        for group in ("core", "material", "wire", "mode", "design",
                      "emc", "losses", "harmonics", "margins", "verification"):
            require_path(selected, (group,))
        if selected["design"].get("n_gaps") != 1:
            raise ValueError(f"{f_key}: отчёт допускает только один физический зазор")
    return data


def build_screening(data: Dict[str, Any]) -> Dict[str, Any]:
    """Получить готовые таблицы отбора только из results_single_gap.json."""
    return {
        "materials": data["materials"],
        "frequencies": {
            f_key: {
                "seen": data["results"][f_key]["n_seen"],
                "evaluated": data["results"][f_key]["n_evaluated"],
                "feasible": data["results"][f_key]["n_feasible"],
                "pareto": data["results"][f_key]["pareto_size"],
                "loss_window": data["results"][f_key]["n_loss_window"],
                "selection": data["results"][f_key]["selection"],
                "area_product": data["results"][f_key]["area_product_screening"],
                "turn_window": data["results"][f_key]["turn_window_screening"],
                "core_material": data["results"][f_key]["core_material_table"],
                "material_comparison": data["results"][f_key]["material_comparison"],
            }
            for f_key, _ in FREQS
        },
    }


def title_page(doc, tz: Dict[str, Any]) -> None:
    for _ in range(3):
        para(doc, "")
    p = para(doc, "РАСЧЁТ ДРОССЕЛЯ ПОВЫШАЮЩЕГО (BOOST) ПРЕОБРАЗОВАТЕЛЯ",
             indent=False, align=WD_ALIGN_PARAGRAPH.CENTER)
    p.runs[0].bold = True
    p.runs[0].font.size = Pt(16)
    para(doc, "")
    para(doc, "Пояснительная записка", indent=False,
         align=WD_ALIGN_PARAGRAPH.CENTER)
    for _ in range(2):
        para(doc, "")
    frequencies = "; ".join(frequency_label(value).removesuffix(" кГц")
                            for value in tz["f_sw_list"])
    para(doc, f"Выходная мощность {fmt(tz['p_out_nom'], 0)} Вт, "
              f"{fmt(tz['u_in_nom'], 0)} В / {fmt(tz['u_out_nom'], 0)} В, "
              f"частоты {frequencies} кГц", indent=False,
         align=WD_ALIGN_PARAGRAPH.CENTER)
    for _ in range(7):
        para(doc, "")
    para(doc, "Аналитический предварительный расчёт конструкции с одним "
              "физическим зазором. Окончательный статус присваивается после "
              "МКЭ, тепловых и ЭМС-испытаний.", indent=False,
         align=WD_ALIGN_PARAGRAPH.CENTER)
    for _ in range(4):
        para(doc, "")
    para(doc, str(date.today().year), indent=False,
         align=WD_ALIGN_PARAGRAPH.CENTER)
    doc.add_paragraph().add_run().add_break(WD_BREAK.PAGE)


def sec_input(doc, data, tn):
    tz = data["tz"]
    h1(doc, "1 Исходные данные, режимы и допуски")
    para(doc, "Исходные данные приняты по техническому заданию. Коэффициенты "
              "и ограничения приведены с указанием их назначения; отсутствие "
              "заданного запаса u_B означает, что численная погрешность должна быть "
              "получена из исследования сеточной сходимости МКЭ, а не назначена заранее.")
    rows = [
        ["Входное напряжение U_вх", fmt(tz["u_in_nom"], 0), "В", "ТЗ"],
        ["Выходное напряжение U_вых", fmt(tz["u_out_nom"], 0), "В", "ТЗ"],
        ["Выходной ток I_вых", fmt(tz["i_out_nom"], 0), "А", "ТЗ"],
        ["Выходная мощность P_вых", fmt(tz["p_out_nom"], 0), "Вт", "ТЗ"],
        ["КПД преобразователя η", fmt(tz["eta"] * 100, 0), "%", "ТЗ"],
        ["Частота коммутации f", "; ".join(label.replace(" кГц", "")
                                            for _, label in FREQS), "кГц", "ТЗ"],
        ["Размах пульсации тока r_I", fmt(tz["r_i"] * 100, 0), "%", "ТЗ"],
        ["Допуск U_вх и U_вых", "±" + fmt(tz["tol_u_in"] * 100, 0), "%", "ТЗ"],
        ["Перегрузка по току", "+" + fmt(tz["tol_i_load"] * 100, 0), "%", "ТЗ"],
        ["Допуск индуктивности", "±" + fmt(tz["tol_L"] * 100, 0), "%", "методика"],
        ["Температура среды", fmt(tz["t_amb"], 0), "°С", "ТЗ"],
        ["Предел температуры обмотки", fmt(tz["t_wind_max"], 0), "°С", "методика"],
        ["Предел температуры сердечника", fmt(tz["t_core_max"], 0), "°С", "методика"],
        ["Предварительный коэффициент k_B,пред", fmt(tz["k_B_prelim"], 2), "—", "методика"],
        ["Финальный коэффициент k_B", fmt(tz["k_B"], 2), "—", "методика + МКЭ"],
        ["Численный запас u_B", (fmt(tz["u_B_num"] * 1e3, 0)
                                  if tz.get("u_B_num") is not None else "не задан"),
         "мТл", "по сеточной сходимости"],
        ["Допустимое заполнение медью k_м,доп", fmt(tz["k_cu_dop"], 2), "—", "методика"],
        ["Допустимая занятость окна k_зан,доп", fmt(tz["k_zan_dop"], 2), "—", "методика"],
        ["Число физических зазоров", str(tz["n_gaps_list"][0]), "—", "актуальная конструкция"],
    ]
    captioned_table(doc, tn, "Исходные данные, допуски и их источники",
                    ["Величина", "Значение", "Ед.", "Источник"], rows,
                    [8.8, 3.0, 1.8, 3.2], "input")
    h2(doc, "1.1 Замечание по исходным данным")
    p_ui = tz["u_out_nom"] * tz["i_out_nom"]
    if math.isclose(p_ui, tz["p_out_nom"], rel_tol=1e-9, abs_tol=1e-6):
        para(doc, f"Произведение U_вых · I_вых = {fmt(tz['u_out_nom'], 0)} · "
                  f"{fmt(tz['i_out_nom'], 0)} = {fmt(p_ui, 0)} Вт совпадает с "
                  "заданной выходной мощностью; противоречие исходных данных отсутствует.")
    else:
        para(doc, f"Произведение U_вых · I_вых = {fmt(tz['u_out_nom'], 0)} · "
                  f"{fmt(tz['i_out_nom'], 0)} = {fmt(p_ui, 0)} Вт отличается от "
                  f"заданной мощности {fmt(tz['p_out_nom'], 0)} Вт. В расчёте "
                  f"приоритет имеет мощность {fmt(tz['p_out_nom'], 0)} Вт как более "
                  "тяжёлое условие по входному току; это допущение явно записывают "
                  "в разделе принятых допущений.")


def sec_mode(doc, data, tn, fn, en):
    tz, results = data["tz"], data["results"]
    first = results[FREQS[0][0]]["selected"]["mode"]
    h1(doc, "2 Электрический режим дросселя")
    para(doc, "Расчёт выполнен для идеализированной схемы boost без падений "
              "на ключе, диоде и активном сопротивлении. Наихудшая требуемая "
              "индуктивность выбрана по девяти сочетаниям допусков напряжений.")
    eq(doc, en, "D = 1 − U_вх / U_вых")
    where(doc, ["D — коэффициент заполнения импульсов",
                "U_вх — входное напряжение, В",
                "U_вых — выходное напряжение, В"])
    substitution(doc, f"D = 1 − {fmt(tz['u_in_nom'], 2)} / "
                 f"{fmt(tz['u_out_nom'], 2)} = {fmt(first['D'], 4)}.")
    eq(doc, en, "P_вх = P_вых / η")
    where(doc, ["P_вх — входная мощность, Вт",
                "P_вых — выходная мощность, Вт",
                "η — коэффициент полезного действия"])
    substitution(doc, f"P_вх = {fmt(tz['p_out_nom'], 2)} / "
                 f"{fmt(tz['eta'], 4)} = {fmt(first['p_in_W'], 2)} Вт.")
    eq(doc, en, "I_DC = P_вх / U_вх")
    where(doc, ["I_DC — постоянная составляющая тока дросселя, А"])
    substitution(doc, f"I_DC = {fmt(first['p_in_W'], 2)} / "
                 f"{fmt(tz['u_in_nom'], 2)} = {fmt(first['I_dc_A'], 2)} А.")
    eq(doc, en, "ΔI_пп = r_I · I_DC")
    where(doc, ["ΔI_пп — допустимый размах пульсации тока, А",
                "r_I — относительный размах пульсации тока"])
    substitution(doc, f"ΔI_пп = {fmt(tz['r_i'], 4)} · "
                 f"{fmt(first['I_dc_A'], 2)} = {fmt(first['dI_pp_A'], 3)} А.")
    eq(doc, en, "L_треб = max[U_вх · D / (f · ΔI_пп)]")
    where(doc, ["L_треб — требуемая индуктивность в наихудшем углу допусков, Гн",
                "f — частота коммутации, Гц"])

    labels = [
        ("Коэффициент заполнения D", "D", "—", 4),
        ("Входная мощность P_вх", "p_in_W", "Вт", 2),
        ("Постоянный ток I_DC", "I_dc_A", "А", 2),
        ("Максимальный ток I_max", "I_max_A", "А", 2),
        ("Среднеквадратичный ток I_скз", "I_rms_A", "А", 2),
        ("Размах пульсации ΔI_пп", "dI_pp_A", "А", 3),
        ("Переменная составляющая I_ac,скз", "I_ac_rms_A", "А", 3),
        ("Требуемая индуктивность L_треб", "L_req_uH", "мкГн", 3),
        ("Максимальная потокосцепление Ψ_max", "psi_max_mWb", "мВб", 4),
        ("Максимальная энергия W_max", "W_max_mJ", "мДж", 2),
        ("Наихудший угол для L", "case_L", "—", None),
        ("Наихудший угол для I", "case_I", "—", None),
    ]
    rows = []
    for label, key, unit, digits in labels:
        values = []
        for f_key, _ in FREQS:
            value = results[f_key]["selected"]["mode"][key]
            values.append(fmt(value, digits) if digits is not None else str(value))
        rows.append([label, *values, unit])
    frequency_text = ", ".join(label for _, label in FREQS)
    middle_width = max(2.2, 8.5 / len(FREQS))
    captioned_table(doc, tn, f"Электрический режим при частотах {frequency_text}",
                    ["Величина", *[label for _, label in FREQS], "Ед."], rows,
                    [6.4, *([middle_width] * len(FREQS)), 1.8], "mode")

    h2(doc, "2.1 Формы напряжения и тока, гармонический состав")
    para(doc, "Ток имеет треугольную переменную составляющую. Потери в меди "
              "суммируются по 80 гармоникам; в таблицах приведены первые восемь.")
    for f_key, f_label in FREQS:
        selected = results[f_key]["selected"]
        rows = [[fmt(item["f_Hz"] / 1e3, 0), fmt(item["I_rms_A"], 4),
                 fmt(item["F_R"], 3), fmt(item["R_ac_Ohm"] * 1e3, 4),
                 fmt(item["P_W"], 5)]
                for item in selected["harmonics"][:8]]
        captioned_table(doc, tn, f"Гармоники тока и потери, f = {f_label}",
                        ["f_h, кГц", "I_h,скз, А", "F_R", "R_ac, мОм", "P_h, Вт"],
                        rows, [2.8, 3.3, 2.3, 3.5, 3.5])
        add_figure(doc, str(IMG_DIR / f"waveform_{f_key}.png"),
                   f"Напряжение и ток дросселя, f = {f_label}", fn)


def sec_core(doc, data, screening, tn):
    results = data["results"]
    selected_pairs = sorted({
        (results[f_key]["selected"]["core"]["name"],
         results[f_key]["selected"]["material"]["name"])
        for f_key, _ in FREQS
    })
    selected_text = "; ".join(f"{core}, материал {material}"
                              for core, material in selected_pairs)
    h1(doc, "3 Выбор магнитопровода, материала и провода")
    para(doc, "Для каждого сочетания сердечника, материала, литцендрата, "
              "числа параллельных проводов и числа витков выполнен полный "
              "аналитический перебор для типоразмеров с достаточными паспортными "
              "данными. Выбранное сочетание: " + selected_text + ".")
    policies = [screening["frequencies"][key]["selection"] for key, _ in FREQS]
    policy = policies[0]
    fallback_labels = [label for (key, label), item in zip(FREQS, policies)
                       if item.get("fallback_E_used")]
    if fallback_labels:
        selection_comment = ("Резервное семейство E применено только для вариантов "
                             + ", ".join(fallback_labels)
                             + ", где полный перебор не дал допустимого кандидата "
                               "предпочтительного семейства.")
    else:
        selection_comment = ("Во всех частотных вариантах выбран допустимый кандидат "
                             "предпочтительного семейства; резервное семейство E не применено.")
    para(doc, "Политика выбора: " + policy["policy"] + ". " + selection_comment +
              " Решение отражает фактический численный отбор, а не заранее заданную марку.")

    rows = []
    for f_key, f_label in FREQS:
        item = screening["frequencies"][f_key]
        rows.append([f_label, str(item["seen"]), str(item["evaluated"]),
                     str(item["feasible"]), str(item["pareto"]),
                     str(item["loss_window"])])
    captioned_table(doc, tn, "Объём численного перебора вариантов",
                    ["Частота", "Просмотрено", "Рассчитано", "Допустимо",
                     "Фронт Парето", "В окне потерь"],
                    rows, [2.4, 2.8, 2.8, 2.8, 3.2, 3.2], "enumeration")

    rows = []
    for f_key, f_label in FREQS:
        for item in screening["frequencies"][f_key]["area_product"]:
            if "core" not in item:
                continue
            rows.append([
                f_label, item["core"], item["family"],
                fmt(item["A_e_mm2"], 0), fmt(item["A_w_mm2"], 1),
                fmt(item["Ap_catalog_mm4"], 0),
                fmt(item["Ap_required_mm4"], 0),
                "да" if item["ok"] else "нет",
                "на заказ" if item["custom_gap_possible"]
                else (f"каталог: {item['catalog_gap_count']}" if item["catalog_gap_count"] else "нет"),
            ])
    captioned_table(doc, tn, "Предварительный отбор по произведению площадей A_e·A_w",
                    ["f", "Типоразмер", "Сем.", "A_e, мм²", "A_w, мм²",
                     "A_p, мм⁴", "A_p,треб, мм⁴", "Проходит", "Зазор"], rows,
                    [1.5, 2.8, 1.2, 1.7, 1.7, 2.1, 2.3, 1.6, 2.0],
                    "area_product")
    para(doc, "Отбор A_e·A_w является размерно однородным предварительным "
              "фильтром. Положительный результат не означает, что выполнены "
              "тепловые, токовые и конструктивные ограничения.")

    rows = []
    for f_key, f_label in FREQS:
        for item in screening["frequencies"][f_key]["turn_window"]:
            if "core" not in item:
                continue
            rows.append([
                f_label, item["core"], item["family"],
                fmt(item["A_min_mm2"], 0), fmt(item["A_N_mm2"], 1),
                str(item["N_by_induction"]), str(item["N_by_window"]),
                "да" if item["full_enumeration"] else "нет",
                report_text(item["verdict"]),
            ])
    captioned_table(doc, tn, "Проверка числа витков по индукции и окну",
                    ["f", "Типоразмер", "Сем.", "A_min, мм²", "A_N, мм²",
                     "N_B", "N_w", "Полный перебор", "Причина/результат"], rows,
                    [1.4, 2.6, 1.1, 1.7, 1.7, 1.2, 1.2, 2.0, 4.3],
                    "turn_window")
    para(doc, "Таблица включает семейства EQ, ETD, PM, PQ, RM, EER и E. "
              "Для позиций без полного набора паспортных данных показан только "
              "благоприятный предварительный тест; они не участвуют в полном переборе.")

    rows = []
    for f_key, f_label in FREQS:
        selected = results[f_key]["selected"]
        for item in screening["frequencies"][f_key]["core_material"]:
            best = item.get("best")
            p_min = best.get("losses", {}).get("P_total_W") if best else None
            chosen = (item["core"] == selected["core"]["name"] and
                      item["material"] == selected["material"]["name"])
            reason = report_text(("выбран; " if chosen else "") + item["reason"])
            rows.append([
                f_label, item["core"], item["material"],
                str(item["n_evaluated"]), str(item["n_feasible"]),
                fmt(p_min, 3),
                "допустим" if item["status"] == "analytical_pass" else "отклонён",
                reason,
            ])
    captioned_table(doc, tn, "Полное численное сравнение сочетаний сердечник–материал",
                    ["f", "Типоразмер", "Мат.", "Рассч.", "Доп.", "P_min, Вт",
                     "Статус", "Причина"], rows,
                    [1.3, 2.4, 1.2, 1.3, 1.2, 1.6, 1.7, 6.1], "core_choice")
    para(doc, "Критерий выбора — максимальный минимальный аналитический запас "
              "среди решений в окне потерь, после чего учитываются масса и "
              "собственная ёмкость. Причины нулевого числа решений приведены "
              "не как качественные предположения, а по фактическому маршруту перебора.")

    materials = screening["materials"]
    rows = []
    for material in materials.values():
        pv = (material["k_st"] * (100e3 ** material["alpha"])
              * (0.1 ** material["beta"]) / 1e3)
        rows.append([material["name"], fmt(material["mu_i"], 0),
                     fmt(material["B_S_100_T"] * 1e3, 0),
                     f"{fmt(material['f_min_Hz'] / 1e3, 0)}…"
                     f"{fmt(material['f_max_Hz'] / 1e3, 0)}",
                     fmt(pv, 1), material["datasheet"],
                     material["fit_limitation"]])
    captioned_table(doc, tn, "Параметры рассмотренных магнитных материалов",
                    ["Марка", "μ_i", "B_S(100 °С), мТл", "Диапазон, кГц",
                     "P_V*, кВт/м³", "Источник", "Ограничение аппроксимации"], rows,
                    [1.3, 1.2, 2.2, 2.2, 2.2, 3.0, 5.0], "materials")
    para(doc, "* P_V вычислено по параметрам Штейнмеца базы в общей точке "
              "100 кГц и 100 мТл. Аппроксимация предварительная и не заменяет "
              "проверку по паспортной карте потерь при постоянном подмагничивании.")

    rows = []
    for f_key, f_label in FREQS:
        chosen = results[f_key]["selected"]["material"]["name"]
        for name, item in screening["frequencies"][f_key]["material_comparison"].items():
            if "status" in item:
                result_text = item["status"]
            else:
                result_text = ("проходит аналитику" if item.get("analytical_ok")
                               else "не проходит аналитику")
            if name == chosen:
                result_text = "выбран; " + result_text
            rows.append([
                f_label, name,
                "да" if item.get("in_range") else "нет",
                fmt(item.get("B_allow_mT"), 2), fmt(item.get("B_max_wc_mT"), 2),
                fmt(item.get("P_fe_W"), 4), fmt(item.get("P_total_W"), 3),
                result_text,
            ])
    captioned_table(doc, tn, "Сравнение материалов в выбранной геометрии",
                    ["f", "Марка", "В диапазоне", "B_доп, мТл", "B_wc, мТл",
                     "P_Fe, Вт", "P_Σ, Вт", "Результат"], rows,
                    [1.5, 1.4, 1.8, 2.0, 2.0, 1.8, 1.8, 4.1], "material_choice")

    rows = []
    for f_key, f_label in FREQS:
        core = results[f_key]["selected"]["core"]
        rows.extend([
            [f_label, "Типоразмер", core["name"]],
            [f_label, "Каталожное обозначение без зазора", core["part_ungapped"]],
            [f_label, "A_e / A_min / A_g", f"{fmt(core['A_e_mm2'], 0)} / "
             f"{fmt(core['A_min_mm2'], 0)} / {fmt(core['A_g_mm2'], 0)} мм²"],
            [f_label, "l_e / V_e", f"{fmt(core['l_e_mm'], 0)} мм / "
             f"{fmt(core['V_e_mm3'], 0)} мм³"],
            [f_label, "A_N / l_N", f"{fmt(core['A_N_mm2'], 0)} мм² / "
             f"{fmt(core['l_N_mm'], 1)} мм"],
            [f_label, "Источник A_g", core["A_g_source"]],
            [f_label, "Паспорт", core["datasheet"]],
        ])
    captioned_table(doc, tn, "Параметры выбранного магнитопровода",
                    ["f", "Параметр", "Значение"], rows,
                    [2.0, 6.0, 8.4], "selected_core")

    for f_key, f_label in FREQS:
        wire = results[f_key]["selected"]["wire"]
        rows = [
            ["Наименование", wire["designation"]],
            ["Число жил × диаметр жилы", f"{wire['n_strands']} × {fmt(wire['d_strand_mm'], 3)} мм"],
            ["Число параллельных проводов", str(wire["n_parallel"])],
            ["Суммарная площадь меди витка", fmt(wire["S_cu_mm2"], 3) + " мм²"],
            ["Наружный диаметр одного провода", fmt(wire["d_outer_mm"], 2) + " мм"],
            ["Температурный индекс", fmt(wire["t_index_C"], 0) + " °С"],
            ["Нормативный документ", wire["std"]],
            ["Цена", f"{fmt(wire['price'], 0)} {wire['price_unit']}"],
            ["Ссылка поставщика", wire["url"]],
        ]
        captioned_table(doc, tn, f"Провод обмотки, вариант f = {f_label}",
                        ["Параметр", "Значение"], rows, [7.2, 9.2],
                        "wire" if f_key == FREQS[0][0] else None)


def sec_magnetic(doc, data, tn, en):
    tz, results = data["tz"], data["results"]
    reference_core = results[FREQS[0][0]]["selected"]["core"]
    h1(doc, "4 Расчёт числа витков, зазора, индукции и энергии")
    para(doc, "В расчёте используется один физический зазор на центральном "
              f"стержне. Площадь зазора A_g = "
              f"{fmt(reference_core['A_g_mm2'], 0)} мм² взята из геометрии "
              f"контактной поверхности {reference_core['name']} и не "
              "подменяется эффективной площадью магнитопровода A_e. Источник: "
              f"{reference_core['A_g_source']}.")
    eq(doc, en, "B_доп,пред = k_B,пред · B_S(100 °С)")
    where(doc, ["B_доп,пред — предварительно допустимая индукция, Тл",
                "k_B,пред — коэффициент использования индукции насыщения",
                "B_S(100 °С) — индукция насыщения при 100 °С, Тл"])
    substitution(doc, "B_доп,пред = 0,60 · 0,390 = 0,234 Тл.")
    eq(doc, en, "N_B = ceil[Ψ_max / (A_min · B_доп,пред)]")
    where(doc, ["N_B — минимальное число витков по насыщению",
                "Ψ_max — максимальное потокосцепление, Вб",
                "A_min — минимальная площадь сечения сердечника, м²"])
    eq(doc, en, "A_L,треб = L_ном / N²")
    where(doc, ["A_L,треб — требуемый индуктивностный коэффициент, Гн/вит²",
                "L_ном — номинальная индуктивность, Гн",
                "N — число витков"])
    eq(doc, en, "F_f = 1 + q · g / √A_g · ln(2G / g)")
    where(doc, ["F_f — коэффициент выпучивания поля одного зазора",
                "q — коэффициент геометрической модели",
                "g — полный физический зазор, м",
                "A_g — площадь контактной поверхности зазора, м²",
                "G — характерный размер поверхности зазора, м"])
    eq(doc, en, "A_L = [g / (μ₀ · A_g · F_f) + 1 / A_L0]⁻¹")
    where(doc, ["μ₀ — магнитная постоянная, Гн/м",
                "A_L0 — индуктивностный коэффициент без зазора, Гн/вит²"])
    eq(doc, en, "B_max = Ψ_max / (N · A_min)")
    where(doc, ["B_max — максимальная средняя индукция, Тл"])
    eq(doc, en, "W_max = L · I_max² / 2")
    where(doc, ["W_max — максимальная запасённая энергия, Дж",
                "I_max — максимальный ток, А"])

    rows = []
    gap_rows = []
    for f_key, f_label in FREQS:
        selected = results[f_key]["selected"]
        mode, design, core = selected["mode"], selected["design"], selected["core"]
        n_b = math.ceil(mode["psi_max_mWb"] * 1e-3 /
                        (core["A_min_mm2"] * 1e-6 * design["B_allow_mT"] * 1e-3))
        rows.append([
            f_label, str(n_b), str(design["N"]), fmt(design["A_L_req_nH"], 2),
            fmt(design["A_L_actual_nH"], 2), fmt(design["gap_mm"], 3),
            fmt(design["F_fringe"], 4), fmt(design["L_nom_uH"], 3),
            fmt(design["B_max_wc_mT"], 2), fmt(mode["W_max_mJ"], 2),
        ])
        substitution(doc, f"{f_label}: N_B = {n_b}; принято N = {design['N']}; "
                     f"A_L,треб = {fmt(design['L_nom_uH'], 3)} / {design['N']}² = "
                     f"{fmt(design['A_L_req_nH'], 2)} нГн/вит²; решение уравнения "
                     f"даёт g = {fmt(design['gap_mm'], 3)} мм и F_f = "
                     f"{fmt(design['F_fringe'], 4)}.")
        gap_rows.append([
            f_label, "1", fmt(design["A_L_actual_nH"], 2),
            fmt(design["gap_mm"], 3),
            f"{fmt(design['gap_model_min_mm'], 3)}…{fmt(design['gap_model_max_mm'], 3)}",
            design["gap_specification"],
        ])
    captioned_table(doc, tn, "Магнитный расчёт для одного физического зазора",
                    ["f", "N_B", "N", "A_L,треб", "A_L", "g, мм", "F_f",
                     "L_ном, мкГн", "B_wc, мТл", "W_max, мДж"], rows,
                    [1.6, 1.3, 1.1, 1.8, 1.8, 1.7, 1.5, 2.1, 2.0, 2.0], "magnetic")
    captioned_table(doc, tn, "Задание изготовителю на один физический зазор",
                    ["f", "Зазоров", "Целевой A_L, нГн/вит²", "Оценка g, мм",
                     "Диапазон модели g, мм", "Указание"], gap_rows,
                    [1.8, 1.6, 3.0, 2.4, 3.1, 4.5], "gap")
    para(doc, "Размер g является оценкой аналитической модели. Изготовителю "
              "задают целевой A_L; зазор доводят по измерению A_L. Локальный "
              "максимум B и добавочные потери меди у кромок должны быть "
              "подтверждены МКЭ с физическим радиусом кромки и сеточной сходимостью.")


def sec_winding(doc, data, tn, fn, en):
    results = data["results"]
    h1(doc, "5 Укладка обмотки и расчёт заполнения окна")
    eq(doc, en, "k_м = N · S_м / A_ок,эф;   k_зан = N · S_нар / A_ок,эф")
    where(doc, ["k_м — коэффициент заполнения эффективного окна медью",
                "S_м — суммарная площадь меди параллельных проводов одного витка, м²",
                "k_зан — коэффициент геометрической занятости окна",
                "S_нар — наружная площадь параллельных проводов одного витка, м²",
                "A_ок,эф — эффективная часть окна, доступная выбранной укладке, м²"])
    rows = []
    for f_key, f_label in FREQS:
        selected = results[f_key]["selected"]
        design, wire = selected["design"], selected["wire"]
        layout = design["winding_layout"]
        a_eff = design["N"] * wire["S_cu_mm2"] / design["k_cu"]
        rows.append([
            f_label, str(design["N"]), str(wire["n_parallel"]),
            fmt(design["n_layers"], 0), str(layout["turns_per_layer"]),
            fmt(layout["h_wind_mm"], 2), fmt(design["b_winding_mm"], 2),
            fmt(a_eff, 1), fmt(design["k_cu"], 4), fmt(design["k_zan"], 4),
            fmt(design["r_gap_mm"], 1),
        ])
        substitution(doc, f"{f_label}: k_м = {design['N']} · "
                     f"{fmt(wire['S_cu_mm2'], 3)} / {fmt(a_eff, 1)} = "
                     f"{fmt(design['k_cu'], 4)}.")
    captioned_table(doc, tn, "Геометрия укладки и заполнение окна",
                    ["f", "N", "Паралл.", "Слоёв", "Вит./слой", "h_обм, мм",
                     "b_обм, мм", "A_ок,эф, мм²", "k_м", "k_зан", "Отступ, мм"],
                    rows, [1.5, 1.0, 1.5, 1.3, 1.8, 1.8, 1.8, 2.2, 1.5, 1.5, 2.0],
                    "winding")
    para(doc, "Отступ меди 5 мм от ближайшей кромки зазора является "
              "конструктивным предварительным значением. Его достаточность "
              "проверяется по распределению поля и добавочным потерям в МКЭ.")
    for f_key, f_label in FREQS:
        add_figure(doc, str(IMG_DIR / f"winding_{f_key}.png"),
                   f"Осевое сечение и укладка обмотки, f = {f_label}", fn)


def sec_losses(doc, data, tn, en):
    results = data["results"]
    h1(doc, "6 Потери по компонентам и температурный расчёт")
    para(doc, "Температуры получены сосредоточенной тепловой моделью с "
              "итерацией сопротивления меди. Карта потерь при постоянном "
              "подмагничивании и потери меди в поле зазора не учтены, поэтому "
              "значения имеют предварительный статус.")
    eq(doc, en, "ρ(T) = ρ₂₀ · [1 + α_ρ · (T − 20 °С)]")
    where(doc, ["ρ(T) — удельное сопротивление меди при температуре T, Ом·м",
                "ρ₂₀ — удельное сопротивление меди при 20 °С, Ом·м",
                "α_ρ — температурный коэффициент сопротивления меди, 1/К"])
    eq(doc, en, "P_DC = I_скз² · R_DC;   P_AC = Σ(I_h,скз² · R_AC,h);   P_м = P_DC + P_AC")
    where(doc, ["P_DC — потери от постоянной и низкочастотной составляющей, Вт",
                "R_DC — активное сопротивление обмотки, Ом",
                "P_AC — сумма потерь по гармоникам, Вт",
                "R_AC,h — активное сопротивление на гармонике h, Ом",
                "P_м — суммарные потери в меди, Вт"])
    eq(doc, en, "P_Fe = k_i · |dB/dt|^α · (ΔB)^(β−α) · V_e")
    where(doc, ["P_Fe — потери в магнитопроводе по iGSE, Вт",
                "k_i — нормированный коэффициент iGSE",
                "ΔB — размах переменной индукции, Тл",
                "α, β — показатели Штейнмеца",
                "V_e — эффективный объём магнитопровода, м³"])
    rows = []
    for f_key, f_label in FREQS:
        loss = results[f_key]["selected"]["losses"]
        i_loss = math.sqrt(loss["P_dc_W"] / loss["R_dc_Ohm"])
        rows.append([
            f_label, fmt(i_loss, 2), fmt(loss["R_dc_Ohm"] * 1e3, 4),
            fmt(loss["P_dc_W"], 3), fmt(loss["P_ac_W"], 4),
            fmt(loss["P_cu_W"], 3), fmt(loss["P_fe_W"], 4),
            fmt(loss["P_total_W"], 3), fmt(loss["R_th_K_W"], 3),
            fmt(loss["t_winding_C"], 1), fmt(loss["t_core_C"], 1),
        ])
        substitution(doc, f"{f_label}: P_DC = {fmt(i_loss, 2)}² · "
                     f"{fmt(loss['R_dc_Ohm'], 6)} = {fmt(loss['P_dc_W'], 3)} Вт; "
                     f"P_Σ = {fmt(loss['P_dc_W'], 3)} + {fmt(loss['P_ac_W'], 4)} + "
                     f"{fmt(loss['P_fe_W'], 4)} = {fmt(loss['P_total_W'], 3)} Вт.")
    captioned_table(doc, tn, "Потери и предварительные температуры",
                    ["f", "I_расч, А", "R_DC, мОм", "P_DC, Вт", "P_AC, Вт",
                     "P_м, Вт", "P_Fe, Вт", "P_Σ, Вт", "R_th, К/Вт",
                     "T_обм, °С", "T_серд, °С"], rows,
                    [1.5, 1.8, 1.9, 1.8, 1.8, 1.8, 1.8, 1.8, 1.9, 2.0, 2.1],
                    "losses")


def sec_parasitics(doc, data, tn, fn, en):
    tz, results = data["tz"], data["results"]
    h1(doc, "7 Собственная ёмкость, первый резонанс и импеданс")
    eq(doc, en, "C_соб,max = 1 / [(2π · k_f · f_треб,max)² · L]")
    where(doc, ["C_соб,max — максимально допустимая собственная ёмкость, Ф",
                "k_f — требуемый запас по первому резонансу",
                "f_треб,max — верхняя требуемая частота модели, Гц"])
    eq(doc, en, "f_рез = 1 / [2π · √(L · C_соб)]")
    where(doc, ["f_рез — оценка первой собственной частоты, Гц",
                "C_соб — расчётная собственная ёмкость обмотки, Ф"])
    rows = []
    for f_key, f_label in FREQS:
        design = results[f_key]["selected"]["design"]
        f_req = tz["f_treb_ratio"] * results[f_key]["selected"]["mode"]["f_sw_kHz"]
        rows.append([f_label, fmt(design["L_nom_uH"], 3),
                     fmt(design["C_self_pF"], 3), fmt(design["C_self_max_pF"], 2),
                     fmt(f_req, 0), fmt(design["f_res_MHz"], 3),
                     fmt(design["f_res_MHz"] * 1e3 / f_req, 2), "предварительно"])
        substitution(doc, f"{f_label}: f_рез = 1 / [2π · √("
                     f"{fmt(design['L_nom_uH'], 3)} мкГн · "
                     f"{fmt(design['C_self_pF'], 3)} пФ)] = "
                     f"{fmt(design['f_res_MHz'], 3)} МГц.")
    captioned_table(doc, tn, "Паразитные параметры и первый резонанс",
                    ["f", "L, мкГн", "C_соб, пФ", "C_max, пФ", "f_треб,max, кГц",
                     "f_рез, МГц", "f_рез/f_треб", "Статус"], rows,
                    [1.7, 2.0, 2.0, 2.0, 2.5, 2.2, 2.2, 2.6], "parasitics")
    add_figure(doc, str(IMG_DIR / "impedance.png"),
               "Расчётный модуль импеданса с учётом собственной ёмкости", fn)


def sec_emc(doc, data, tn, en):
    results = data["results"]
    h1(doc, "8 Электромагнитная совместимость")
    para(doc, "Расчёт импеданса характеризует только дифференциальное "
              "последовательное звено в эквивалентной системе 50 Ом. Он не "
              "является подтверждением соответствия нормам кондуктивных помех.")
    eq(doc, en, "A_Z = 20 · lg|1 + Z_L / (Z_s + Z_н)|")
    where(doc, ["A_Z — модельное вносимое затухание, дБ",
                "Z_L — комплексный импеданс дросселя, Ом",
                "Z_s — сопротивление источника, Ом",
                "Z_н — сопротивление нагрузки, Ом"])
    freqs = ("150kHz", "500kHz", "1000kHz", "5000kHz", "10000kHz", "30000kHz")
    rows = []
    for f_name in freqs:
        values = [fmt(results[key]["selected"]["emc"]["A_Z_model_dB"][f_name], 2)
                  for key, _ in FREQS]
        rows.append([f_name.replace("kHz", " кГц"), *values, "модель 50 Ом"])
    middle_width = max(2.2, 8.0 / len(FREQS))
    captioned_table(doc, tn, "Модельное вносимое затухание",
                    ["Частота", *[f"Вариант {label}, дБ" for _, label in FREQS], "Статус"],
                    rows, [2.5, *([middle_width] * len(FREQS)), 3.5], "emc")
    h2(doc, "8.1 Конструктивные меры и обязательная проверка")
    para(doc, "Единственный зазор расположен на центральном стержне; медь "
              "отнесена от ближайшей кромки на 5 мм. Для E-сердечника внешнее "
              "поле не экранируется замкнутой оболочкой, поэтому до выпуска "
              "конструкторской документации обязательны МКЭ поля зазора, "
              "оценка наведённого напряжения в соседних проводниках и измерение "
              "помех с эквивалентом сети. Поля stray_field в JSON отсутствуют; "
              "численные значения внешнего поля в отчёт не выдумываются.")


def _criterion_display(item: Dict[str, Any]) -> Tuple[str, str, str, str, str]:
    value, limit, unit = item.get("value"), item.get("limit"), item.get("unit", "—")
    scale, shown_unit, digits = 1.0, unit, 3
    if unit == "Гн":
        scale, shown_unit, digits = 1e6, "мкГн", 3
    elif unit == "Тл":
        scale, shown_unit, digits = 1e3, "мТл", 2
    elif unit == "м":
        scale, shown_unit, digits = 1e3, "мм", 2
    elif unit == "Гц":
        scale, shown_unit, digits = 1e-6, "МГц", 3
    elif unit == "А/м²":
        scale, shown_unit, digits = 1e-6, "А/мм²", 3
    value_text = fmt(value * scale, digits) if value is not None else "не определено"
    limit_text = fmt(limit * scale, digits) if limit is not None else "—"
    margin_text = (fmt(item.get("margin_pct"), 2) if item.get("margin_pct") is not None
                   else "—")
    if item.get("ok") is True:
        verdict = "да"
    elif item.get("ok") is False:
        verdict = "нет"
    else:
        verdict = "ожидает проверки"
    status_map = {
        "calculated": "рассчитано",
        "preliminary_thermal_model": "предварительная тепловая модель",
        "preliminary_model": "предварительная модель",
        "pending_fem_or_measurement": "ожидает МКЭ/измерения",
        "pending_converged_fem": "ожидает МКЭ со сходимостью",
        "pending_measurement": "ожидает измерения",
        "natural_convection_after_preliminary_thermal_check":
            "естественная конвекция, предварительная тепловая проверка",
        "calculated_80_harmonics": "рассчитано по 80 гармоникам",
    }
    status = status_map.get(item.get("status", ""), item.get("status", ""))
    return value_text, limit_text, shown_unit, margin_text, verdict + "; " + status


def sec_margins(doc, data, tn):
    h1(doc, "9 Запасы по обязательным ограничениям")
    para(doc, "Аналитические критерии отделены от критериев, требующих МКЭ "
              "или испытаний. До завершения этих проверок окончательное "
              "соответствие конструкции не устанавливают.")
    for index, (f_key, f_label) in enumerate(FREQS):
        if index:
            doc.add_paragraph().add_run().add_break(WD_BREAK.PAGE)
        margins = data["results"][f_key]["selected"]["margins"]
        rows = []
        for key, item in margins.items():
            if key.startswith("_"):
                continue
            value, limit, unit, margin, state = _criterion_display(item)
            rows.append([item["name"], value, item.get("cmp", "—"), limit,
                         unit, margin, state])
        captioned_table(doc, tn, f"Запасы и незакрытые критерии, f = {f_label}",
                        ["Критерий", "Значение", "Условие", "Предел", "Ед.",
                         "Запас, %", "Результат и статус"], rows,
                        [5.0, 2.2, 1.5, 2.0, 1.4, 2.0, 4.3],
                        f"margins_{index + 1}")


def sec_choice(doc, data, tn):
    results = data["results"]
    h1(doc, "10 Сравнение вариантов и рекомендация по частоте")
    metrics = [
        ("Требуемая индуктивность", "design", "L_min_uH", "мкГн", 3),
        ("Номинальная индуктивность", "design", "L_nom_uH", "мкГн", 3),
        ("Число витков", "design", "N", "—", 0),
        ("Один физический зазор", "design", "gap_mm", "мм", 3),
        ("Параллельных проводов", "wire", "n_parallel", "—", 0),
        ("Суммарная длина провода", "design", "wire_length_total_m", "м", 2),
        ("Предварительная B_wc", "design", "B_max_wc_mT", "мТл", 2),
        ("Заполнение медью k_м", "design", "k_cu", "—", 4),
        ("Геометрическая занятость k_зан", "design", "k_zan", "—", 4),
        ("Потери в меди", "losses", "P_cu_W", "Вт", 3),
        ("Потери в сердечнике", "losses", "P_fe_W", "Вт", 4),
        ("Суммарные потери", "losses", "P_total_W", "Вт", 3),
        ("Температура обмотки", "losses", "t_winding_C", "°С", 1),
        ("Первый резонанс", "design", "f_res_MHz", "МГц", 3),
    ]
    rows = []
    for label, group, key, unit, digits in metrics:
        values = [fmt(results[f_key]["selected"][group][key], digits)
                  for f_key, _ in FREQS]
        rows.append([label, *values, unit])
    middle_width = max(2.2, 8.5 / len(FREQS))
    captioned_table(doc, tn, "Сравнение частотных вариантов",
                    ["Параметр", *[label for _, label in FREQS], "Ед."], rows,
                    [6.4, *([middle_width] * len(FREQS)), 1.8], "frequency_choice")
    ranked = sorted(((results[key]["selected"]["losses"]["P_total_W"], label)
                     for key, label in FREQS))
    loss_text = "; ".join(f"{label}: {fmt(loss, 3)} Вт" for loss, label in ranked)
    para(doc, "По потерям только дросселя минимальное расчётное значение имеет "
              f"вариант {ranked[0][1]} ({fmt(ranked[0][0], 3)} Вт). Полный ряд: "
              f"{loss_text}. Расчёт не содержит коммутационных потерь "
              "полупроводников и результатов ЭМС, поэтому это приоритет для МКЭ "
              "и макетной проверки, а не окончательный выбор частоты.")


def sec_summary(doc, data, tn):
    h1(doc, "11 Итоговые данные конструкции")
    for f_key, f_label in FREQS:
        selected = data["results"][f_key]["selected"]
        core, mat, wire = selected["core"], selected["material"], selected["wire"]
        design, loss = selected["design"], selected["losses"]
        rows = [
            ["Статус", "аналитическая предварительная конструкция"],
            ["Магнитопровод", core["name"]],
            ["Комплект без зазора", core["part_ungapped"]],
            ["Материал", mat["name"]],
            ["Исполнение зазора", "один физический зазор центрального стержня"],
            ["Целевой A_L", fmt(design["A_L_actual_nH"], 2) + " нГн/вит²"],
            ["Оценка зазора g", fmt(design["gap_mm"], 3) + " мм"],
            ["Диапазон модели g", f"{fmt(design['gap_model_min_mm'], 3)}…"
             f"{fmt(design['gap_model_max_mm'], 3)} мм"],
            ["Число витков", str(design["N"])],
            ["Провод", wire["designation"]],
            ["Число слоёв", fmt(design["n_layers"], 0)],
            ["Отступ меди от кромки", fmt(design["r_gap_mm"], 1) + " мм"],
            ["Длина одного провода", fmt(design["wire_length_m"], 2) + " м"],
            ["Общая длина провода", fmt(design["wire_length_total_m"], 2) + " м"],
            ["L_ном / L_min / L_max", f"{fmt(design['L_nom_uH'], 3)} / "
             f"{fmt(design['L_min_uH'], 3)} / {fmt(design['L_max_uH'], 3)} мкГн"],
            ["B_wc / B_доп,пред", f"{fmt(design['B_max_wc_mT'], 2)} / "
             f"{fmt(design['B_allow_mT'], 2)} мТл"],
            ["k_м / k_зан", f"{fmt(design['k_cu'], 4)} / {fmt(design['k_zan'], 4)}"],
            ["P_Σ", fmt(loss["P_total_W"], 3) + " Вт"],
            ["T_обм / T_серд", f"{fmt(loss['t_winding_C'], 1)} / "
             f"{fmt(loss['t_core_C'], 1)} °С"],
            ["C_соб / f_рез", f"{fmt(design['C_self_pF'], 3)} пФ / "
             f"{fmt(design['f_res_MHz'], 3)} МГц"],
            ["Незакрытые проверки", pending_text(selected["verification"]["pending"])],
        ]
        captioned_table(doc, tn, f"Итоговая конструкция, вариант f = {f_label}",
                        ["Параметр", "Значение"], rows, [6.8, 9.6],
                        f"summary_{FREQS.index((f_key, f_label)) + 1}")
    para(doc, "Зазор изготавливают по целевому A_L с последующей доводкой по "
              "измерению. Указанный размер g нельзя использовать как готовый "
              "производственный допуск без согласования технологии шлифования и МКЭ.")


def sec_conclusions(doc, data):
    h1(doc, "12 Выводы")
    q = data["results"][FREQS[0][0]]["quantities"]
    designs = [(label, data["results"][key]["selected"])
               for key, label in FREQS]
    frequency_text = ", ".join(label for label, _ in designs)
    selection_items = [
        f"Для {label} выбран {selected['core']['name']}, материал "
        f"{selected['material']['name']}, {selected['design']['N']} витков и "
        f"один расчётный зазор {fmt(selected['design']['gap_mm'], 3)} мм "
        "по целевому A_L."
        for label, selected in designs
    ]
    fallback = [(label, data["results"][key]["selection"])
                for key, label in FREQS
                if data["results"][key]["selection"].get("fallback_E_used")]
    if fallback:
        family_item = ("Резервный сердечник семейства E применён для вариантов "
                       + ", ".join(label for label, _ in fallback)
                       + ": полный численный перебор не дал допустимого кандидата "
                         "семейств EQ, ETD, PM, PQ, RM и EER. Для остальных "
                         "вариантов резервное семейство не применялось.")
    else:
        family_item = ("Во всех частотных вариантах выбран сердечник одного из "
                       "предпочтительных семейств EQ, ETD, PM, PQ, RM и EER; "
                       "резервное семейство E не потребовалось.")
    losses_text = "; ".join(
        f"{label}: {fmt(selected['losses']['P_total_W'], 3)} Вт"
        for label, selected in designs)
    items = [
        f"Рассчитан один дроссель повышающего преобразователя мощностью "
        f"{fmt(data['tz']['p_out_nom'] / 1e3, 3)} кВт "
        f"для частотных вариантов {frequency_text}. Магнитопровод содержит один "
        "физический зазор центрального стержня.",
        *selection_items,
        family_item,
        f"На один дроссель требуется {q['core_sets']} комплект магнитопровода, "
        f"то есть {q['core_halves_total']} половинки. Частотные варианты "
        "являются альтернативными и не суммируются в одной спецификации.",
        "Выбранные конструкции проходят рассчитанные аналитические ограничения, но "
        "окончательное соответствие устанавливают после МКЭ и испытаний.",
        "Предварительные потери по вариантам: " + losses_text + ".",
        "Требуются МКЭ локальной индукции с физическим радиусом кромки и исследованием сеточной сходимости, а также расчёт добавочных потерь меди в поле зазора.",
        "Требуется подтверждение дифференциальной индуктивности L_diff(I) при рабочем токе и доводка зазора по измеренному A_L.",
        "Предварительные температуры должны быть проверены тепловым испытанием макета в наихудшем режиме.",
        "Расчёт собственной ёмкости и резонанса должен быть подтверждён измерением импеданса готовой обмотки.",
        "Окончательный выбор частоты выполняют после учёта потерь всего преобразователя и измерения ЭМС; финальная рекомендация до этих работ не выдаётся.",
    ]
    for index, text in enumerate(items, 1):
        p = para(doc, f"{index}) {text}")
        p.paragraph_format.space_after = Pt(6)


def sec_scope(doc, data, tn):
    h1(doc, "13 Состав отчёта и вынесенные за пределы расчёта работы")
    margin_refs = ", ".join(str(REFS[f"margins_{index + 1}"])
                            for index in range(len(FREQS)))
    rows = [
        ["1 Исходные данные, режимы и допуски", f"табл. {REFS['input']}", "выполнено"],
        ["2 Источник паспортных величин",
         f"табл. {REFS['area_product']}, {REFS['turn_window']}, "
         f"{REFS['core_choice']}, {REFS['materials']}, {REFS['wire']}",
         "выполнено"],
        ["3 Формы u_L(t), i(t) и гармонический состав", "разд. 2.1", "выполнено"],
        ["4 Витки, один физический зазор, индукция, энергия", f"табл. {REFS['magnetic']}, {REFS['gap']}", "аналитически выполнено"],
        ["5 Чертёж укладки и заполнение окна", f"табл. {REFS['winding']}", "выполнено"],
        ["6 Потери по компонентам и гармоникам", f"табл. {REFS['losses']}", "предварительно"],
        ["7 МКЭ с исследованием сеточной сходимости", "—", "ожидает выполнения"],
        ["8 Температурное поле в наихудшем режиме", "разд. 6", "сосредоточенная модель; поле не выполнено"],
        ["9 Z(f) и первый резонанс", f"табл. {REFS['parasitics']}", "модель; ожидает измерения"],
        ["10 Синфазный ток и внешнее магнитное поле", "разд. 8.1", "ожидает МКЭ/измерения"],
        ["11 Запасы по обязательным ограничениям", f"табл. {margin_refs}", "расчётные и pending разделены"],
        ["12 Программа и протокол испытаний образца", "—", "вне объёма аналитического расчёта"],
    ]
    captioned_table(doc, tn, "Соответствие обязательному составу отчёта по методике",
                    ["Обязательный пункт", "Раздел", "Состояние"], rows,
                    [8.9, 3.1, 4.4], "scope")
    pending = sorted(set(item for f_key, _ in FREQS
                         for item in data["results"][f_key]["selected"]
                         ["verification"]["pending"]))
    para(doc, "До присвоения окончательного статуса необходимо выполнить: "
              f"{pending_text(pending)}. Отчёт не разрешает серийное "
              "изготовление без этих проверок.")


def sec_sources(doc, data):
    h1(doc, "Список использованных источников")
    core_sources = sorted({data["results"][key]["selected"]["core"]["datasheet"]
                           for key, _ in FREQS})
    sources = [
        "Методика проектирования высокочастотных силовых дросселей — Metodika_VCh_silovykh_drosseley_bez_rascheta.tex, актуальная редакция проекта.",
        "ГОСТ Р 2.105—2019. Единая система конструкторской документации. Общие требования к текстовым документам.",
        "ГОСТ 8.417—2002. Государственная система обеспечения единства измерений. Единицы величин.",
        "ГОСТ 30805.22—2013 (CISPR 22:2006). Радиопомехи индустриальные. Нормы и методы измерений.",
        "Texas Instruments. SLVA372D. Basic Calculation of a Boost Converter's Power Stage.",
        *[f"{source} — геометрия и магнитные параметры выбранного магнитопровода."
          for source in core_sources],
        *[f"{material['datasheet']} — данные материала {material['name']}."
          for material in data["materials"].values()],
        "Sullivan C. R. Optimal Choice for Number of Strands in a Litz-Wire Transformer Winding // IEEE Transactions on Power Electronics, 1999.",
        "Massarini A., Kazimierczuk M. K. Self-Capacitance of Inductors // IEEE Transactions on Power Electronics, 1997.",
        "Venkatachalam K. et al. Accurate Prediction of Ferrite Core Loss with Nonsinusoidal Waveforms Using Only Steinmetz Parameters // IEEE COMPEL, 2002.",
        "ООО «Кабель-Гарант». Каталог литцендрата в нейлоне; ссылка на конкретную позицию приведена в таблицах провода.",
    ]
    for index, source in enumerate(sources, 1):
        p = para(doc, f"{index}. {source}")
        p.paragraph_format.space_after = Pt(6)


def main() -> None:
    data = load_results()
    screening = build_screening(data)
    tn, fn, en = [1], [1], [1]
    doc = setup_document()
    title_page(doc, data["tz"])
    sec_input(doc, data, tn)
    sec_mode(doc, data, tn, fn, en)
    sec_core(doc, data, screening, tn)
    sec_magnetic(doc, data, tn, en)
    sec_winding(doc, data, tn, fn, en)
    sec_losses(doc, data, tn, en)
    sec_parasitics(doc, data, tn, fn, en)
    sec_emc(doc, data, tn, en)
    sec_margins(doc, data, tn)
    sec_choice(doc, data, tn)
    sec_summary(doc, data, tn)
    sec_conclusions(doc, data)
    sec_scope(doc, data, tn)
    sec_sources(doc, data)
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    doc.save(OUT_PATH)
    print(f"отчёт сохранён: {OUT_PATH}")
    print(f"таблиц: {tn[0] - 1}; рисунков: {fn[0] - 1}; формул: {en[0] - 1}")


if __name__ == "__main__":
    main()
