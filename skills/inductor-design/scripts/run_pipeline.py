#!/usr/bin/env python3
"""Выполнить расчёт, рисунки, отчёт и валидацию проекта."""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path


SCRIPT_ROOT = Path(__file__).resolve().parent


def run(project: Path, relative_script: str) -> None:
    script = project / relative_script
    if not script.is_file():
        raise FileNotFoundError(f"не найден этап конвейера: {script}")
    print(f"\n[{relative_script}]")
    subprocess.run([sys.executable, str(script)], cwd=project, check=True)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project", type=Path)
    parser.add_argument("--only", choices=("single", "interleaved", "both"),
                        default=None, help="переопределить включённые варианты")
    args = parser.parse_args()
    project = args.project.resolve()
    config_path = project / "2_input_files" / "design_config.json"
    with config_path.open(encoding="utf-8") as stream:
        config = json.load(stream)

    single = config.get("single", {}).get("enabled", False)
    interleaved = config.get("interleaved", {}).get("enabled", False)
    if args.only:
        single = args.only in ("single", "both")
        interleaved = args.only in ("interleaved", "both")
    if not single and not interleaved:
        raise ValueError("в конфигурации не включён ни один расчётный вариант")

    if single:
        run(project, "3_calc/inductor_design.py")
        run(project, "3_calc/make_drawings.py")
        run(project, "3_calc/make_report.py")
    if interleaved:
        run(project, "5_interleaved/interleaved_design.py")
        run(project, "5_interleaved/make_drawings_3ph.py")
        run(project, "5_interleaved/make_report_3ph.py")

    run(project, "3_calc/test_methodology.py")

    validator_args = [sys.executable, str(SCRIPT_ROOT / "validate_project.py"),
                      str(project)]
    if args.only:
        validator_args.extend(("--only", args.only))
    subprocess.run(validator_args, check=True)


if __name__ == "__main__":
    main()
