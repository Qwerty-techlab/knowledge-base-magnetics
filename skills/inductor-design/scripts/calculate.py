#!/usr/bin/env python3
"""Создать проект из минимального ТЗ и выполнить полный расчёт одним запуском."""
from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

import prepare_config


SCRIPT_ROOT = Path(__file__).resolve().parent
SKILL_ROOT = SCRIPT_ROOT.parent
DEFAULT_KNOWLEDGE_BASE = SKILL_ROOT.parents[1]


def run(arguments: list[str]) -> None:
    subprocess.run([sys.executable, *arguments], check=True)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--tz", required=True, type=Path,
                        help="минимальный JSON-файл технического задания")
    parser.add_argument("--output", required=True, type=Path,
                        help="новый каталог проекта")
    parser.add_argument("--knowledge-base", type=Path,
                        default=DEFAULT_KNOWLEDGE_BASE,
                        help="каталог knowledge_base")
    parser.add_argument("--prepare-only", action="store_true",
                        help="создать проект и конфигурацию без расчёта")
    args = parser.parse_args()

    tz_path = args.tz.resolve()
    output = args.output.resolve()
    knowledge_base = args.knowledge_base.resolve()
    if output.exists():
        raise FileExistsError(
            f"каталог результата уже существует: {output}; "
            "для пересчёта используйте run_pipeline.py"
        )

    data = prepare_config.validate_minimal_tz(prepare_config.load_json(tz_path))
    topology = data["topology"]
    run([
        str(SCRIPT_ROOT / "create_project.py"), str(output),
        "--name", data["project_name"],
        "--knowledge-base", str(knowledge_base),
        "--topology", topology,
    ])
    config_path = prepare_config.configure_project(data, output)
    print(f"конфигурация ТЗ: {config_path}")
    if args.prepare_only:
        print("проект подготовлен без запуска расчёта")
        return
    run([str(SCRIPT_ROOT / "run_pipeline.py"), str(output)])


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    main()
