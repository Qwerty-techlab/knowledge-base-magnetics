#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
make_bibliography.py — генерация BIBLIOGRAPHY.md из bibliography.json.

Дополнительно:
  * дописывает библиографические поля в metadata.json каждой статьи;
  * сверяет bibliography.json с фактическим содержимым articles/
    и сообщает о расхождениях.

Использование:
    python make_bibliography.py            сгенерировать и синхронизировать
    python make_bibliography.py --check    только проверка, без записи
"""

from __future__ import annotations

import argparse
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
BIB_JSON = os.path.join(ROOT, "bibliography.json")
ARTICLES = os.path.join(ROOT, "articles")
OUT_MD = os.path.join(ROOT, "BIBLIOGRAPHY.md")

TOPIC_TITLES = {
    "01_interleaved_boost": "Interleaved boost и многофазные преобразователи",
    "02_basic_boost_pfc": "Базовый boost, CCM PFC, выбор режима",
    "03_inductor_design": "Проектирование дросселя: потери, зазор, обмотка",
    "04_litz_wire": "Литцендрат",
    "05_emc": "ЭМС, паразитные ёмкости, собственный резонанс",
    "06_textbooks_ru": "Отечественные учебные пособия и методики",
}


def scan_articles() -> dict[str, dict]:
    """Фактическое содержимое articles/: slug -> сведения о файлах."""
    found = {}
    if not os.path.isdir(ARTICLES):
        return found
    for topic in sorted(os.listdir(ARTICLES)):
        tdir = os.path.join(ARTICLES, topic)
        if not os.path.isdir(tdir):
            continue
        for slug in sorted(os.listdir(tdir)):
            sdir = os.path.join(tdir, slug)
            # Папки, начинающиеся с «_», — служебные (методики, исходники),
            # в библиографию не входят.
            if not os.path.isdir(sdir) or slug.startswith("_"):
                continue
            files = set(os.listdir(sdir))
            info = {"topic": topic, "dir": sdir,
                    "has_pdf": "source.pdf" in files,
                    "has_parsed": "parsed.md" in files,
                    "has_meta": "metadata.json" in files,
                    "n_pages": None, "quality": None}
            if info["has_meta"]:
                try:
                    with open(os.path.join(sdir, "metadata.json"),
                              encoding="utf-8") as fh:
                        m = json.load(fh)
                    info["n_pages"] = m.get("n_pages_parsed")
                    info["quality"] = m.get("extraction_quality")
                except (OSError, json.JSONDecodeError):
                    pass
            found[slug] = info
    return found


def sync_metadata(slug: str, entry: dict, info: dict) -> None:
    """Дописывает библиографические поля в metadata.json статьи."""
    path = os.path.join(info["dir"], "metadata.json")
    try:
        with open(path, encoding="utf-8") as fh:
            meta = json.load(fh)
    except (OSError, json.JSONDecodeError):
        meta = {}

    meta["bib_authors"] = entry.get("authors")
    meta["bib_title"] = entry.get("title")
    meta["bib_venue"] = entry.get("venue")
    meta["bib_year"] = entry.get("year")
    meta["bib_doi"] = entry.get("doi")
    meta["bib_title_source"] = entry.get("title_source")
    meta["topic"] = entry.get("topic")
    meta["keywords_ru"] = entry.get("keywords_ru", [])
    meta["use_in_methodology"] = entry.get("application")
    if entry.get("duplicate_note"):
        meta["duplicate_note"] = entry["duplicate_note"]

    with open(path, "w", encoding="utf-8") as fh:
        json.dump(meta, fh, ensure_ascii=False, indent=2)


def cite(entry: dict) -> str:
    """Библиографическая строка."""
    parts = []
    if entry.get("authors"):
        parts.append(entry["authors"])
    if entry.get("title"):
        parts.append(f"*{entry['title']}*")
    if entry.get("venue"):
        parts.append(entry["venue"])
    if entry.get("year"):
        parts.append(str(entry["year"]))
    line = ", ".join(parts) + "."
    if entry.get("doi"):
        line += f" DOI: [{entry['doi']}](https://doi.org/{entry['doi']})"
    return line


def render(bib: dict, found: dict) -> str:
    entries = bib["entries"]
    meta = bib["_meta"]
    n_doi = sum(1 for e in entries.values() if e.get("doi"))
    n_unverified = sum(1 for e in entries.values()
                       if e.get("title_source") == "derived_from_filename")

    out = [
        "# Библиография базы знаний",
        "",
        "Файл сгенерирован автоматически из `bibliography.json` скриптом",
        "`skills/make_bibliography.py`. **Правьте `bibliography.json`, не этот файл.**",
        "",
        f"Обновлено: {meta['updated']}. Записей: {len(entries)}, "
        f"из них с DOI: {n_doi}.",
        "",
        f"> {n_unverified} записей помечены `derived_from_filename` — заголовок "
        "восстановлен по имени файла,",
        "> точная библиографическая запись не выверена. Перед цитированием в отчёте "
        "сверяйте с PDF.",
        "",
        "У каждой статьи в её папке лежат: `source.pdf` (исходник, **не** в git), "
        "`parsed.md` (извлечённый",
        "текст — читайте его, а не PDF) и `metadata.json` (метаданные и оценка "
        "качества извлечения).",
        "",
        "---",
        "",
    ]

    for topic, title in TOPIC_TITLES.items():
        items = {s: e for s, e in entries.items() if e.get("topic") == topic}
        if not items:
            continue
        out += [f"## {title}", "", f"Папка: `articles/{topic}/`", ""]
        for i, (slug, entry) in enumerate(sorted(items.items()), start=1):
            info = found.get(slug, {})
            pages = info.get("n_pages")
            pg = f", {pages} стр." if pages else ""
            flag = ""
            if entry.get("title_source") == "derived_from_filename":
                flag = "  ⚠ запись не выверена"
            if info.get("quality") and info["quality"] != "хорошо":
                flag += f"  ⚠ {info['quality']}"

            out.append(f"**{i}. {cite(entry)}**{flag}")
            out.append("")
            out.append(f"- Папка: `{topic}/{slug}/`{pg}")
            if entry.get("application"):
                out.append(f"- Применение: {entry['application']}")
            if entry.get("keywords_ru"):
                out.append(f"- Ключевые слова: {', '.join(entry['keywords_ru'])}")
            if entry.get("duplicate_note"):
                out.append(f"- Примечание: {entry['duplicate_note']}")
            out.append("")
        out.append("---")
        out.append("")

    return "\n".join(out)


def main() -> int:
    ap = argparse.ArgumentParser(
        description="Генерация BIBLIOGRAPHY.md из bibliography.json.")
    ap.add_argument("--check", action="store_true",
                    help="только проверить согласованность, ничего не писать")
    args = ap.parse_args()

    with open(BIB_JSON, encoding="utf-8") as fh:
        bib = json.load(fh)
    entries = bib["entries"]
    found = scan_articles()

    # Сверка библиографии с файловой системой
    missing_dir = sorted(set(entries) - set(found))
    orphan_dir = sorted(set(found) - set(entries))
    wrong_topic = [s for s in set(entries) & set(found)
                   if entries[s].get("topic") != found[s]["topic"]]
    no_parsed = sorted(s for s, i in found.items() if not i["has_parsed"])

    print(f"Записей в bibliography.json: {len(entries)}")
    print(f"Папок статей в articles/:    {len(found)}")

    problems = 0
    if missing_dir:
        problems += len(missing_dir)
        print(f"\nЕСТЬ В БИБЛИОГРАФИИ, НЕТ ПАПКИ ({len(missing_dir)}):")
        for s in missing_dir:
            print("  ", s)
    if orphan_dir:
        problems += len(orphan_dir)
        print(f"\nЕСТЬ ПАПКА, НЕТ В БИБЛИОГРАФИИ ({len(orphan_dir)}):")
        for s in orphan_dir:
            print(f"   {found[s]['topic']}/{s}")
    if wrong_topic:
        problems += len(wrong_topic)
        print(f"\nРАСХОЖДЕНИЕ ТЕМЫ ({len(wrong_topic)}):")
        for s in wrong_topic:
            print(f"   {s}: json={entries[s].get('topic')} fs={found[s]['topic']}")
    if no_parsed:
        print(f"\nБЕЗ parsed.md ({len(no_parsed)}) — запустите parse_pdf.py:")
        for s in no_parsed:
            print("  ", s)

    if not problems:
        print("\nБиблиография согласована с файловой системой.")

    if args.check:
        return 1 if problems else 0

    n_sync = 0
    for slug, entry in entries.items():
        if slug in found and found[slug]["has_meta"]:
            sync_metadata(slug, entry, found[slug])
            n_sync += 1

    with open(OUT_MD, "w", encoding="utf-8") as fh:
        fh.write(render(bib, found))

    print(f"\nmetadata.json синхронизировано: {n_sync}")
    print(f"BIBLIOGRAPHY.md записан: {OUT_MD}")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
