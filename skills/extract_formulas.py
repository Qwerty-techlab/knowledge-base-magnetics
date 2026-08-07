# -*- coding: utf-8 -*-
"""Извлечение формул из PDF в виде картинок высокого разрешения.

Зачем: parse_pdf.py снимает только текстовый слой, а в нём формула разрушается
(дробные черты и радикалы -- векторная графика, знак интеграла приходит как "Z"
или "R", группировка степеней теряется). Поэтому формулы вырезаются как
изображения и читаются глазами по требованию -- это единственный достоверный путь.

Метод не опирается на имена шрифтов: у LaTeX-статей математика набрана CMMI/CMSY,
у IEEE -- обычным Times-Italic, и по шрифту она неотличима от курсива в тексте.
Опора -- геометрия: номер уравнения (N) у правого края колонки задаёт полосу,
полоса вырезается на всю ширину колонки.

Использование:
    python extract_formulas.py <папка_статьи>            # одна статья
    python extract_formulas.py --all                     # вся база
    python extract_formulas.py --all --dpi 400 --force
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

try:
    import fitz  # PyMuPDF
except ImportError:
    sys.exit("Нужен PyMuPDF: pip install pymupdf")

BASE = Path(__file__).resolve().parent.parent
ARTICLES = BASE / "articles"

EQNUM_RE = re.compile(r"^\(\s?(\d{1,3}[a-z]?)\s?\)$")
EQNUM_ANY_RE = re.compile(r"\((\d{1,3}[a-z]?)\)")
MATH_CHARS = set(
    "∫∑∏√±∓×÷≈≅≡≠≤≥≪≫∈∉∀∃∂∇∞∝·⋅∘⊥∥→←↔⇒⇔∆‖⟨⟩"
    "αβγδεζηθικλμνξπρστυφχψωΓΔΘΛΞΠΣΦΨΩ"
)
ITALIC_BIT = 2

# Геометрия полосы
PAD_X = 4.0       # запас по горизонтали, pt
PAD_Y = 3.0       # запас по вертикали, pt
BAND_TOL = 2.0    # допуск на перекрытие по вертикали, pt
MAX_BAND_H = 200  # выше -- это уже не формула, а колонка текста


def block_text(block) -> str:
    out = []
    for line in block.get("lines", []):
        for span in line.get("spans", []):
            out.append(span.get("text") or "".join(c["c"] for c in span.get("chars", [])))
    return "".join(out)


def detect_columns(blocks, page_rect):
    """Определить колонки по широким текстовым блокам. Возврат: [(x0, x1), ...]."""
    mid = (page_rect.x0 + page_rect.x1) / 2.0
    left, right, full = [], [], []
    for b in blocks:
        x0, _, x1, _ = b["bbox"]
        if (x1 - x0) < 40 or len(block_text(b).strip()) < 25:
            continue
        if x1 <= mid + 8:
            left.append((x0, x1))
        elif x0 >= mid - 8:
            right.append((x0, x1))
        else:
            full.append((x0, x1))
    cols = []
    for group in (left, right):
        if len(group) >= 2:
            cols.append((min(g[0] for g in group), max(g[1] for g in group)))
    if not cols:
        pool = left + right + full
        if pool:
            cols.append((min(p[0] for p in pool), max(p[1] for p in pool)))
        else:
            cols.append((page_rect.x0, page_rect.x1))
    return cols


def in_column(bbox, col):
    """Блок принадлежит колонке, если его центр внутри её границ."""
    cx = (bbox[0] + bbox[2]) / 2.0
    return col[0] - 10 <= cx <= col[1] + 10


def inside_image(bbox, img_boxes):
    """Блок целиком лежит внутри рисунка -> это подпись на схеме, не формула."""
    x0, y0, x1, y1 = bbox
    for ix0, iy0, ix1, iy1 in img_boxes:
        if x0 >= ix0 - 2 and y0 >= iy0 - 2 and x1 <= ix1 + 2 and y1 <= iy1 + 2:
            return True
    return False


def math_likeness(block, col):
    """Балл «блок похож на выключную формулу» -- для формул без номера."""
    text = block_text(block)
    stripped = text.strip()
    if not stripped or len(stripped) > 160:
        return 0.0
    n_vis = sum(1 for c in stripped if not c.isspace())
    if n_vis < 2:
        return 0.0
    n_italic = n_sizes = 0
    sizes, baselines = set(), set()
    for line in block.get("lines", []):
        for span in line.get("spans", []):
            step = max(0.25 * span["size"], 0.5)
            italic = bool(span["flags"] & ITALIC_BIT)
            for ch in span.get("chars", []):
                if ch["c"].isspace():
                    continue
                sizes.add(round(span["size"], 1))
                baselines.add(round(ch["origin"][1] / step))
                n_italic += 1 if italic else 0
    n_sizes = len(sizes)
    x0, y0, x1, y1 = block["bbox"]
    col_w = max(col[1] - col[0], 1.0)
    score = 0.0
    score += min(sum(1 for c in stripped if c in MATH_CHARS), 4) * 0.9
    if len(baselines) >= 3:
        score += 1.5
    elif len(baselines) == 2:
        score += 0.7
    if n_sizes >= 2:
        score += 0.9
    if n_italic / n_vis > 0.5:
        score += 1.1
    # выключная формула не занимает всю ширину колонки и заметно отступает
    if (x1 - x0) < 0.8 * col_w and (x0 - col[0]) > 0.06 * col_w:
        score += 1.0
    # многострочная конструкция малой ширины -- дробь
    if (y1 - y0) > 18 and (x1 - x0) < 0.6 * col_w:
        score += 1.0
    if "=" in stripped:
        score += 0.6
    return score


MATH_THRESHOLD = 3.2


def gather_band(col_blocks, seed):
    """Собрать вертикальную полосу вокруг блока-затравки.

    Формула в PDF разбита на отдельные блоки (числитель, дробная черта,
    знаменатель, пределы, номер). Их надо собрать в одну полосу: берём всё,
    что перекрывается по вертикали, и расширяем, пока полоса прирастает.
    """
    y0, y1 = seed["bbox"][1], seed["bbox"][3]
    members = [
        ob for ob in col_blocks
        if ob["bbox"][1] <= y1 + BAND_TOL and ob["bbox"][3] >= y0 - BAND_TOL
    ]
    if not members:
        members = [seed]
    for _ in range(4):
        ny0 = min(m["bbox"][1] for m in members)
        ny1 = max(m["bbox"][3] for m in members)
        if (ny1 - ny0) > MAX_BAND_H:
            break
        grown = [
            ob for ob in col_blocks
            if ob["bbox"][1] <= ny1 + BAND_TOL and ob["bbox"][3] >= ny0 - BAND_TOL
        ]
        if len(grown) == len(members):
            break
        members = grown
    by0 = min(m["bbox"][1] for m in members)
    by1 = max(m["bbox"][3] for m in members)
    if (by1 - by0) > MAX_BAND_H:  # полоса разрослась в колонку текста
        return y0 - 6, y1 + 6, [seed]
    return by0, by1, members


def build_bands(page):
    """Найти полосы с формулами. Возврат: [{'rect', 'eq', 'text', 'kind'}]."""
    raw = page.get_text("rawdict")
    blocks = [b for b in raw.get("blocks", []) if b.get("type") == 0]
    img_boxes = [b["bbox"] for b in raw.get("blocks", []) if b.get("type") != 0]
    if not blocks:
        return []
    cols = detect_columns(blocks, page.rect)
    bands = []

    for col in cols:
        col_blocks = [b for b in blocks if in_column(b["bbox"], col)]
        # 1) якоря -- номера уравнений у правого края колонки
        anchors = []
        for b in col_blocks:
            m = EQNUM_RE.match(block_text(b).strip())
            if m and b["bbox"][2] >= col[1] - 0.10 * (col[1] - col[0]):
                anchors.append((b, m.group(1)))
        used = set()
        for b, num in anchors:
            by0, by1, members = gather_band(col_blocks, b)
            for ob in members:
                used.add(id(ob))
            text = " ".join(block_text(ob).strip() for ob in members if block_text(ob).strip())
            bands.append({
                "rect": (col[0] - PAD_X, by0 - PAD_Y, col[1] + PAD_X, by1 + PAD_Y),
                "eq": num, "text": text, "kind": "numbered",
            })

        # 2) формулы без номера -- по «математичности» блока.
        # Полоса тоже на всю ширину колонки: иначе куски одной формулы
        # (числитель, знаменатель, левая часть) не склеиваются между собой.
        for b in col_blocks:
            if id(b) in used:
                continue
            txt = block_text(b).strip()
            n_vis = sum(1 for c in txt if not c.isspace())
            n_math = sum(1 for c in txt if c in MATH_CHARS)
            if n_vis < 4 or ("=" not in txt and n_math < 2):
                continue  # подписи на схемах, обрывки текста
            if inside_image(b["bbox"], img_boxes):
                continue  # надписи внутри рисунка
            if math_likeness(b, col) < MATH_THRESHOLD:
                continue
            by0, by1, members = gather_band(col_blocks, b)
            for ob in members:
                used.add(id(ob))
            full = " ".join(
                block_text(ob).strip() for ob in members if block_text(ob).strip()
            )
            bands.append({
                "rect": (col[0] - PAD_X, by0 - PAD_Y, col[1] + PAD_X, by1 + PAD_Y),
                "eq": None, "text": full or txt, "kind": "unnumbered",
            })

    # склейка перекрывающихся полос
    bands.sort(key=lambda d: (round(d["rect"][1], 1), d["rect"][0]))
    merged = []
    for band in bands:
        if merged:
            prev = merged[-1]
            same_col = abs(prev["rect"][0] - band["rect"][0]) < 30
            # зазор до 4 pt: строки одной выключной формулы стоят вплотную
            overlap = band["rect"][1] <= prev["rect"][3] + 4.0
            if same_col and overlap and (band["rect"][3] - prev["rect"][1]) <= MAX_BAND_H:
                prev["rect"] = (
                    min(prev["rect"][0], band["rect"][0]),
                    min(prev["rect"][1], band["rect"][1]),
                    max(prev["rect"][2], band["rect"][2]),
                    max(prev["rect"][3], band["rect"][3]),
                )
                prev["eq"] = prev["eq"] or band["eq"]
                prev["text"] = (prev["text"] + " " + band["text"]).strip()
                if band["kind"] == "numbered":
                    prev["kind"] = "numbered"
                continue
        merged.append(band)
    return merged


def render_band(page, rect, dpi):
    """Вырезать область страницы в PNG-байты."""
    clip = fitz.Rect(*rect) & page.rect
    if clip.is_empty or clip.width < 8 or clip.height < 5:
        return None, None
    pix = page.get_pixmap(dpi=dpi, clip=clip, colorspace=fitz.csGRAY)
    return pix.tobytes("png"), (pix.width, pix.height)


def process_article(art_dir: Path, dpi: int, max_pages: int, force: bool):
    pdf_path = art_dir / "source.pdf"
    if not pdf_path.exists():
        return {"article": art_dir.name, "status": "нет source.pdf", "n": 0}
    out_dir = art_dir / "formulas"
    index_path = out_dir / "index.json"
    if index_path.exists() and not force:
        try:
            n = len(json.loads(index_path.read_text(encoding="utf-8"))["formulas"])
        except Exception:
            n = 0
        return {"article": art_dir.name, "status": "уже есть", "n": n}

    doc = fitz.open(pdf_path)
    limit = doc.page_count if max_pages <= 0 else min(max_pages, doc.page_count)
    out_dir.mkdir(exist_ok=True)
    for old in out_dir.glob("eq_*.png"):
        old.unlink()

    records = []
    for pno in range(limit):
        page = doc[pno]
        for i, band in enumerate(build_bands(page), start=1):
            png, size = render_band(page, band["rect"], dpi)
            if png is None:
                continue
            name = f"eq_p{pno + 1:03d}_{i:02d}.png"
            (out_dir / name).write_bytes(png)
            # номера уравнений внутри полосы: одна полоса может нести две формулы
            nums = EQNUM_ANY_RE.findall(band["text"])
            records.append({
                "file": name,
                "page": pno + 1,
                "eq_number": band["eq"] or (nums[0] if nums else None),
                "eq_numbers": nums,
                "kind": band["kind"],
                "bbox_pt": [round(v, 1) for v in band["rect"]],
                "px": list(size),
                "text_layer": " ".join(band["text"].split())[:400],
            })
    doc.close()

    index = {
        "article": art_dir.name,
        "source": "source.pdf",
        "pages_scanned": limit,
        "dpi": dpi,
        "n_formulas": len(records),
        "warning": (
            "text_layer -- это то, что даёт текстовый слой PDF, он для формул "
            "НЕДОСТОВЕРЕН (нет дробных черт, знак интеграла приходит как Z или R). "
            "Достоверный источник -- PNG-файл; читать его глазами."
        ),
        "formulas": records,
    }
    index_path.write_text(
        json.dumps(index, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    write_index_md(out_dir, index)
    return {"article": art_dir.name, "status": "готово", "n": len(records)}


def write_index_md(out_dir: Path, index: dict):
    lines = [
        f"# Формулы: {index['article']}",
        "",
        f"Всего: {index['n_formulas']} | страниц просмотрено: {index['pages_scanned']}"
        f" | {index['dpi']} dpi",
        "",
        "> Текст в колонке «текстовый слой» приведён только для поиска. "
        "Для чтения самой формулы открывать PNG.",
        "",
        "| файл | стр. | № | текстовый слой (недостоверно) |",
        "|---|---|---|---|",
    ]
    for r in index["formulas"]:
        txt = r["text_layer"][:90].replace("|", "\\|")
        eq = r["eq_number"] or "-"
        lines.append(f"| `{r['file']}` | {r['page']} | {eq} | {txt} |")
    (out_dir / "INDEX.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


WARN_START = "<!-- FORMULA-WARNING -->"
WARN_END = "<!-- /FORMULA-WARNING -->"


def annotate_article(art_dir: Path):
    """Вписать предупреждение о формулах в parsed.md и счётчик в metadata.json."""
    index_path = art_dir / "formulas" / "index.json"
    if not index_path.exists():
        return False
    index = json.loads(index_path.read_text(encoding="utf-8"))
    n = index["n_formulas"]

    parsed = art_dir / "parsed.md"
    if parsed.exists():
        text = parsed.read_text(encoding="utf-8")
        block = (
            f"{WARN_START}\n"
            f"> **Формулы в этом файле недостоверны.** Текстовый слой PDF теряет "
            f"дробные черты, радикалы и группировку степеней; знак интеграла "
            f"приходит как `Z` или `R`, знак суммы -- как `P`. "
            f"Формул вырезано: **{n}**, читать их в `formulas/` "
            f"(картинки {index['dpi']} dpi, перечень в `formulas/INDEX.md`).\n"
            f"{WARN_END}\n"
        )
        if WARN_START in text:
            head, _, rest = text.partition(WARN_START)
            _, _, tail = rest.partition(WARN_END)
            text = head + block.rstrip("\n") + tail
        else:
            lines = text.split("\n")
            cut = 1 if lines and lines[0].startswith("# ") else 0
            text = "\n".join(lines[:cut]) + ("\n\n" if cut else "") + block + \
                "\n".join(lines[cut:])
        parsed.write_text(text, encoding="utf-8")

    meta_path = art_dir / "metadata.json"
    if meta_path.exists():
        meta = json.loads(meta_path.read_text(encoding="utf-8"))
        meta["formulas_extracted"] = n
        meta["formulas_dir"] = "formulas/"
        meta["formulas_note"] = (
            "Формулы в parsed.md разрушены текстовым слоем PDF; "
            "достоверный источник -- PNG в formulas/"
        )
        meta_path.write_text(
            json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8"
        )
    return True


def find_articles():
    for topic in sorted(ARTICLES.iterdir()):
        if not topic.is_dir() or topic.name.startswith("_"):
            continue
        for art in sorted(topic.iterdir()):
            if art.is_dir() and not art.name.startswith("_"):
                yield art


def main():
    ap = argparse.ArgumentParser(description="Вырезать формулы из PDF в PNG")
    ap.add_argument("path", nargs="?", help="папка статьи")
    ap.add_argument("--all", action="store_true", help="обработать всю базу")
    ap.add_argument("--dpi", type=int, default=300)
    ap.add_argument("--max-pages", type=int, default=0, help="0 = все страницы")
    ap.add_argument("--force", action="store_true", help="перезаписать")
    ap.add_argument("--annotate-only", action="store_true",
                    help="только вписать предупреждения, ничего не рендерить")
    args = ap.parse_args()

    if args.all:
        targets = list(find_articles())
    elif args.path:
        targets = [Path(args.path).resolve()]
    else:
        ap.error("укажите папку статьи или --all")

    if args.annotate_only:
        n_ok = sum(1 for art in targets if annotate_article(art))
        print(f"Предупреждения вписаны: {n_ok} из {len(targets)} статей")
        return

    total = 0
    for art in targets:
        res = process_article(art, args.dpi, args.max_pages, args.force)
        annotate_article(art)
        total += res["n"]
        print(f"  {res['status']:>10} | {res['n']:4d} | {res['article'][:58]}")
    print(f"\nИтого формул: {total} в {len(targets)} статьях")


if __name__ == "__main__":
    main()
