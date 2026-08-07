#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
parse_pdf.py — извлечение текста из PDF в Markdown для базы знаний.

Назначение: один раз превратить PDF в текст, чтобы агент читал `parsed.md`
и не тратил токены на распознавание PDF при каждом обращении.

Использование:
    python parse_pdf.py <файл.pdf>                    один файл рядом с ним
    python parse_pdf.py <папка>                       все PDF в папке (рекурсивно)
    python parse_pdf.py <папка> --layout              сохранять раскладку колонок
    python parse_pdf.py <папка> --force               перезаписать существующие parsed.md
    python parse_pdf.py <папка> --max-pages 40        ограничить число страниц

Результат рядом с каждым PDF:
    parsed.md      — текст с разметкой страниц
    metadata.json  — метаданные PDF + статистика извлечения

Требования: PyMuPDF (fitz). Резервный вариант — pypdf.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from datetime import datetime, timezone

ENGINE = None
try:
    import fitz  # PyMuPDF
    ENGINE = "pymupdf"
except ImportError:
    try:
        import pypdf
        ENGINE = "pypdf"
    except ImportError:
        pass


# ────────────────────────── нормализация текста ──────────────────────────

# Лигатуры и типографские символы, ломающие поиск по тексту
_REPLACEMENTS = {
    "ﬀ": "ff", "ﬁ": "fi", "ﬂ": "fl", "ﬃ": "ffi",
    "ﬄ": "ffl", "ﬅ": "st", "ﬆ": "st",
    "‘": "'", "’": "'", "“": '"', "”": '"',
    "–": "-", "—": "-", "−": "-", " ": " ",
    "­": "",  # soft hyphen
}


def normalize(text: str) -> str:
    """Приводит извлечённый текст к пригодному для поиска виду."""
    for src, dst in _REPLACEMENTS.items():
        text = text.replace(src, dst)
    # склейка слов, разорванных переносом в конце строки
    text = re.sub(r"(\w)-\n(\w)", r"\1\2", text)
    # схлопывание трёх и более пустых строк
    text = re.sub(r"\n{3,}", "\n\n", text)
    # хвостовые пробелы
    text = re.sub(r"[ \t]+\n", "\n", text)
    return text.strip()


def slugify(name: str) -> str:
    """Имя файла → безопасный slug для имени папки."""
    name = os.path.splitext(name)[0]
    name = re.sub(r"[^\w\s.-]", "", name, flags=re.UNICODE)
    name = re.sub(r"[\s.]+", "_", name.strip())
    return name.strip("_")[:120]


# ────────────────────────── извлечение ──────────────────────────

def extract_pymupdf(path: str, layout: bool, max_pages: int | None):
    """Извлечение через PyMuPDF. Возвращает (страницы, метаданные)."""
    doc = fitz.open(path)
    mode = "text" if not layout else "blocks"
    pages, n = [], len(doc)
    limit = min(n, max_pages) if max_pages else n

    for i in range(limit):
        page = doc[i]
        if mode == "text":
            raw = page.get_text("text")
        else:
            blocks = sorted(page.get_text("blocks"), key=lambda b: (round(b[1]), b[0]))
            raw = "\n".join(b[4] for b in blocks if b[4].strip())
        pages.append(normalize(raw))

    md = doc.metadata or {}
    meta = {
        "pdf_title": (md.get("title") or "").strip() or None,
        "pdf_author": (md.get("author") or "").strip() or None,
        "pdf_subject": (md.get("subject") or "").strip() or None,
        "pdf_keywords": (md.get("keywords") or "").strip() or None,
        "pdf_creator": (md.get("creator") or "").strip() or None,
        "pdf_creation_date": (md.get("creationDate") or "").strip() or None,
        "n_pages_total": n,
        "n_pages_parsed": limit,
        "is_encrypted": bool(doc.is_encrypted),
    }
    doc.close()
    return pages, meta


def extract_pypdf(path: str, max_pages: int | None):
    """Резервное извлечение через pypdf."""
    reader = pypdf.PdfReader(path)
    n = len(reader.pages)
    limit = min(n, max_pages) if max_pages else n
    pages = [normalize(reader.pages[i].extract_text() or "") for i in range(limit)]

    info = reader.metadata or {}
    meta = {
        "pdf_title": (info.get("/Title") or "") or None,
        "pdf_author": (info.get("/Author") or "") or None,
        "pdf_subject": (info.get("/Subject") or "") or None,
        "pdf_keywords": (info.get("/Keywords") or "") or None,
        "pdf_creator": (info.get("/Creator") or "") or None,
        "pdf_creation_date": str(info.get("/CreationDate") or "") or None,
        "n_pages_total": n,
        "n_pages_parsed": limit,
        "is_encrypted": bool(reader.is_encrypted),
    }
    return pages, meta


# ────────────────────────── запись результата ──────────────────────────

def write_markdown(out_path: str, src_name: str, pages: list[str], meta: dict) -> int:
    """Пишет parsed.md с маркерами страниц. Возвращает число символов."""
    head = [
        f"# {meta.get('pdf_title') or os.path.splitext(src_name)[0]}",
        "",
        f"> Автоматически извлечено из `{src_name}` скриптом `parse_pdf.py`",
        f"> Движок: {ENGINE}. Страниц: {meta['n_pages_parsed']} из {meta['n_pages_total']}.",
        f"> Дата извлечения: {meta['parsed_at']}",
        "",
        "Текст не редактировался. Формулы и таблицы могут быть искажены —",
        "при сомнении сверяться с исходным PDF.",
        "",
        "---",
        "",
    ]
    body = []
    for i, text in enumerate(pages, start=1):
        body.append(f"## [стр. {i}]")
        body.append("")
        body.append(text if text else "_(страница без извлекаемого текста: скан или графика)_")
        body.append("")

    content = "\n".join(head + body)
    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write(content)
    return len(content)


def process_pdf(pdf_path: str, layout: bool, max_pages: int | None, force: bool) -> dict:
    """Обрабатывает один PDF. Возвращает сводку."""
    folder = os.path.dirname(pdf_path)
    name = os.path.basename(pdf_path)
    md_path = os.path.join(folder, "parsed.md")
    meta_path = os.path.join(folder, "metadata.json")

    if os.path.exists(md_path) and not force:
        return {"file": name, "status": "skip", "reason": "parsed.md уже существует"}

    try:
        if ENGINE == "pymupdf":
            pages, meta = extract_pymupdf(pdf_path, layout, max_pages)
        elif ENGINE == "pypdf":
            pages, meta = extract_pypdf(pdf_path, max_pages)
        else:
            return {"file": name, "status": "fail", "reason": "нет PyMuPDF и pypdf"}
    except Exception as exc:
        return {"file": name, "status": "fail", "reason": f"{type(exc).__name__}: {exc}"}

    meta["parsed_at"] = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    meta["engine"] = ENGINE
    meta["source_pdf"] = name
    meta["source_size_kb"] = round(os.path.getsize(pdf_path) / 1024, 1)

    n_chars = write_markdown(md_path, name, pages, meta)
    n_empty = sum(1 for p in pages if not p.strip())

    meta["n_chars_extracted"] = n_chars
    meta["n_pages_empty"] = n_empty
    meta["extraction_quality"] = (
        "плохо: вероятно скан без OCR" if n_empty > len(pages) * 0.5
        else "неполно: часть страниц без текста" if n_empty
        else "хорошо"
    )

    # Поля для ручного заполнения — агент дописывает их при разборе статьи
    meta.setdefault("bib_authors", None)
    meta.setdefault("bib_year", None)
    meta.setdefault("bib_venue", None)
    meta.setdefault("bib_doi", None)
    meta.setdefault("topic", None)
    meta.setdefault("keywords_ru", [])
    meta.setdefault("use_in_methodology", None)

    with open(meta_path, "w", encoding="utf-8") as fh:
        json.dump(meta, fh, ensure_ascii=False, indent=2)

    return {
        "file": name,
        "status": "ok",
        "pages": meta["n_pages_parsed"],
        "chars": n_chars,
        "empty": n_empty,
        "quality": meta["extraction_quality"],
    }


# ────────────────────────── CLI ──────────────────────────

def main() -> int:
    ap = argparse.ArgumentParser(
        description="Извлечение текста из PDF в parsed.md рядом с исходником.")
    ap.add_argument("target", help="путь к PDF или к папке с PDF")
    ap.add_argument("--layout", action="store_true",
                    help="сохранять раскладку блоков (для двухколоночных статей)")
    ap.add_argument("--force", action="store_true",
                    help="перезаписать существующие parsed.md")
    ap.add_argument("--max-pages", type=int, default=None,
                    help="ограничить число обрабатываемых страниц")
    args = ap.parse_args()

    if ENGINE is None:
        print("ОШИБКА: нужен PyMuPDF или pypdf.  pip install pymupdf", file=sys.stderr)
        return 2

    target = os.path.abspath(args.target)
    if not os.path.exists(target):
        print(f"ОШИБКА: путь не найден: {target}", file=sys.stderr)
        return 2

    if os.path.isfile(target):
        pdfs = [target]
    else:
        pdfs = []
        for root, _dirs, files in os.walk(target):
            pdfs.extend(os.path.join(root, f) for f in files
                        if f.lower().endswith(".pdf"))
        pdfs.sort()

    if not pdfs:
        print("PDF-файлов не найдено.")
        return 0

    print(f"Движок: {ENGINE}.  Файлов к обработке: {len(pdfs)}\n")

    stats = {"ok": 0, "skip": 0, "fail": 0}
    problems = []

    for i, pdf in enumerate(pdfs, start=1):
        res = process_pdf(pdf, args.layout, args.max_pages, args.force)
        stats[res["status"]] += 1
        # Для схемы «папка статьи / source.pdf» имя файла неинформативно —
        # показываем имя папки.
        label = (os.path.basename(os.path.dirname(pdf))
                 if res["file"].lower() == "source.pdf" else res["file"])
        short = label[:58]

        if res["status"] == "ok":
            flag = "" if res["quality"] == "хорошо" else f"  <- {res['quality']}"
            print(f"[{i:>3}/{len(pdfs)}] ok   {short:<60} "
                  f"{res['pages']:>3} стр. {res['chars']:>7} симв.{flag}")
            if res["quality"] != "хорошо":
                problems.append((res["file"], res["quality"]))
        elif res["status"] == "skip":
            print(f"[{i:>3}/{len(pdfs)}] skip {short:<60} {res['reason']}")
        else:
            print(f"[{i:>3}/{len(pdfs)}] FAIL {short:<60} {res['reason']}")
            problems.append((res["file"], res["reason"]))

    print(f"\nИтог: обработано {stats['ok']}, пропущено {stats['skip']}, "
          f"ошибок {stats['fail']}")

    if problems:
        print("\nТребуют внимания:")
        for name, why in problems:
            print(f"  - {name}: {why}")

    return 1 if stats["fail"] else 0


if __name__ == "__main__":
    sys.exit(main())
