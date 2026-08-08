#!/usr/bin/env python3
"""Создать автономный проект расчёта из эталонного шаблона."""
from __future__ import annotations

import argparse
import json
import shutil
from pathlib import Path


SKILL_ROOT = Path(__file__).resolve().parents[1]
TEMPLATE = SKILL_ROOT / "assets" / "project_template"
DEFAULT_KNOWLEDGE_BASE = SKILL_ROOT.parents[1]
REQUIRED_TEMPLATE_FILES = (
    "0_references/Metodika_VCh_silovykh_drosseley_bez_rascheta.tex",
    "2_input_files/design_config.json",
    "2_input_files/prompt.txt",
    "3_calc/inductor_design.py",
    "3_calc/make_drawings.py",
    "3_calc/make_report.py",
    "3_calc/report_style.py",
    "3_calc/test_methodology.py",
    "5_interleaved/interleaved_design.py",
    "5_interleaved/make_drawings_3ph.py",
    "5_interleaved/make_report_3ph.py",
)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("target", type=Path, help="новый каталог проекта")
    parser.add_argument("--name", default=None, help="имя проекта в конфигурации")
    parser.add_argument("--knowledge-base", type=Path, default=DEFAULT_KNOWLEDGE_BASE,
                        help="каталог knowledge_base")
    parser.add_argument("--topology", choices=("single", "interleaved", "both"),
                        default="both", help="включённые расчётные варианты")
    args = parser.parse_args()

    target = args.target.resolve()
    if target.exists():
        raise FileExistsError(f"целевой каталог уже существует: {target}")
    if not TEMPLATE.is_dir():
        raise FileNotFoundError(f"не найден шаблон проекта: {TEMPLATE}")
    missing_template_files = [
        relative for relative in REQUIRED_TEMPLATE_FILES
        if not (TEMPLATE / relative).is_file()
    ]
    if missing_template_files:
        missing = ", ".join(missing_template_files)
        raise FileNotFoundError(f"шаблон проекта неполон, отсутствуют файлы: {missing}")
    knowledge_base = args.knowledge_base.resolve()
    for required in ("components_db/cores.json",
                     "components_db/ferrite_materials.json",
                     "components_db/litz_wire.json"):
        if not (knowledge_base / required).is_file():
            raise FileNotFoundError(f"в базе отсутствует {required}: {knowledge_base}")

    shutil.copytree(TEMPLATE, target)
    config_path = target / "2_input_files" / "design_config.json"
    with config_path.open(encoding="utf-8") as stream:
        config = json.load(stream)
    config["knowledge_base_path"] = str(knowledge_base)
    config["project"]["name"] = args.name or target.name
    config["single"]["enabled"] = args.topology in ("single", "both")
    config["interleaved"]["enabled"] = args.topology in ("interleaved", "both")
    with config_path.open("w", encoding="utf-8") as stream:
        json.dump(config, stream, ensure_ascii=False, indent=2)
        stream.write("\n")
    print(f"проект создан: {target}")
    print(f"конфигурация: {config_path}")


if __name__ == "__main__":
    main()
