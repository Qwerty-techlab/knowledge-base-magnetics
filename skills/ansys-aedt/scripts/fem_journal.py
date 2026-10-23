#!/usr/bin/env python3
"""SQLite journal for the single-inductor FEM workflow.

The database is the concise handoff surface for future agents.  Every material
action, decision, assumption, solver run, issue, and produced artifact should be
recorded here as soon as it occurs.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sqlite3
from datetime import datetime
from pathlib import Path
from typing import Any


DEFAULT_DB = Path(__file__).resolve().parents[1] / "fem_journal.sqlite3"


SCHEMA = """
PRAGMA foreign_keys = ON;
PRAGMA journal_mode = WAL;

CREATE TABLE IF NOT EXISTS metadata (
    key TEXT PRIMARY KEY,
    value TEXT NOT NULL,
    updated_at TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS actions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ts TEXT NOT NULL,
    phase TEXT NOT NULL,
    action TEXT NOT NULL,
    tool TEXT,
    command TEXT,
    inputs_json TEXT,
    result_summary TEXT NOT NULL,
    status TEXT NOT NULL CHECK(status IN ('planned','started','ok','warning','failed','blocked','skipped')),
    duration_s REAL,
    artifact_path TEXT
);

CREATE TABLE IF NOT EXISTS decisions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ts TEXT NOT NULL,
    topic TEXT NOT NULL,
    decision TEXT NOT NULL,
    rationale TEXT NOT NULL,
    evidence TEXT
);

CREATE TABLE IF NOT EXISTS assumptions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ts TEXT NOT NULL,
    name TEXT NOT NULL,
    value TEXT NOT NULL,
    status TEXT NOT NULL CHECK(status IN ('unverified','verified','rejected','bounded')),
    source TEXT,
    impact TEXT
);

CREATE TABLE IF NOT EXISTS issues (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ts_opened TEXT NOT NULL,
    ts_closed TEXT,
    severity TEXT NOT NULL CHECK(severity IN ('info','low','medium','high','critical')),
    title TEXT NOT NULL,
    description TEXT NOT NULL,
    status TEXT NOT NULL CHECK(status IN ('open','investigating','resolved','accepted','blocked')),
    resolution TEXT
);

CREATE TABLE IF NOT EXISTS runs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ts_start TEXT NOT NULL,
    ts_end TEXT,
    solver TEXT NOT NULL,
    project TEXT,
    design TEXT,
    setup TEXT,
    case_name TEXT NOT NULL,
    mesh_level TEXT,
    status TEXT NOT NULL CHECK(status IN ('planned','running','ok','warning','failed','hung','cancelled')),
    duration_s REAL,
    input_json TEXT,
    metrics_json TEXT,
    log_path TEXT,
    notes TEXT
);

CREATE TABLE IF NOT EXISTS artifacts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ts TEXT NOT NULL,
    kind TEXT NOT NULL,
    path TEXT NOT NULL UNIQUE,
    sha256 TEXT,
    bytes INTEGER,
    run_id INTEGER REFERENCES runs(id),
    description TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS handoff (
    id INTEGER PRIMARY KEY CHECK(id = 1),
    updated_at TEXT NOT NULL,
    phase TEXT NOT NULL,
    status TEXT NOT NULL,
    next_step TEXT NOT NULL,
    blocker TEXT,
    summary TEXT NOT NULL
);

CREATE VIEW IF NOT EXISTS latest_actions AS
SELECT id, ts, phase, action, status, result_summary, artifact_path
FROM actions ORDER BY id DESC LIMIT 30;

CREATE VIEW IF NOT EXISTS open_issues AS
SELECT id, ts_opened, severity, title, status, description
FROM issues WHERE status IN ('open','investigating','blocked')
ORDER BY CASE severity
    WHEN 'critical' THEN 1 WHEN 'high' THEN 2 WHEN 'medium' THEN 3
    WHEN 'low' THEN 4 ELSE 5 END, id;
"""


def now() -> str:
    return datetime.now().astimezone().isoformat(timespec="seconds")


def json_text(value: str | None) -> str | None:
    if value is None or value == "":
        return None
    try:
        parsed: Any = json.loads(value)
    except json.JSONDecodeError as exc:
        raise SystemExit(f"Invalid JSON: {exc}") from exc
    return json.dumps(parsed, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def connect(path: Path) -> sqlite3.Connection:
    path.parent.mkdir(parents=True, exist_ok=True)
    con = sqlite3.connect(path)
    con.row_factory = sqlite3.Row
    con.execute("PRAGMA foreign_keys = ON")
    con.execute("PRAGMA busy_timeout = 5000")
    return con


def initialise(con: sqlite3.Connection) -> None:
    con.executescript(SCHEMA)
    stamp = now()
    metadata = {
        "schema_version": "1",
        "project": "drossel1 single-inductor FEM",
        "canonical_methodology": (
            "knowledge_base/articles/06_textbooks_ru/_methodology_source/"
            "Metodika_VCh_silovykh_drosseley_bez_rascheta.tex"
        ),
        "evidence_policy": (
            "Sources and analytical formulas are hypotheses until checked; "
            "converged FEM or measurements may correct the methodology."
        ),
    }
    for key, value in metadata.items():
        con.execute(
            "INSERT INTO metadata(key,value,updated_at) VALUES(?,?,?) "
            "ON CONFLICT(key) DO UPDATE SET value=excluded.value, updated_at=excluded.updated_at",
            (key, value, stamp),
        )
    con.commit()


def add_action(con: sqlite3.Connection, args: argparse.Namespace) -> int:
    cur = con.execute(
        """INSERT INTO actions
        (ts,phase,action,tool,command,inputs_json,result_summary,status,duration_s,artifact_path)
        VALUES(?,?,?,?,?,?,?,?,?,?)""",
        (
            now(), args.phase, args.action, args.tool, args.command,
            json_text(args.inputs), args.result, args.status, args.duration,
            args.artifact,
        ),
    )
    con.commit()
    return int(cur.lastrowid)


def add_decision(con: sqlite3.Connection, args: argparse.Namespace) -> int:
    cur = con.execute(
        "INSERT INTO decisions(ts,topic,decision,rationale,evidence) VALUES(?,?,?,?,?)",
        (now(), args.topic, args.decision, args.rationale, args.evidence),
    )
    con.commit()
    return int(cur.lastrowid)


def add_assumption(con: sqlite3.Connection, args: argparse.Namespace) -> int:
    cur = con.execute(
        """INSERT INTO assumptions(ts,name,value,status,source,impact)
        VALUES(?,?,?,?,?,?)""",
        (now(), args.name, args.value, args.status, args.source, args.impact),
    )
    con.commit()
    return int(cur.lastrowid)


def add_issue(con: sqlite3.Connection, args: argparse.Namespace) -> int:
    cur = con.execute(
        """INSERT INTO issues(ts_opened,severity,title,description,status)
        VALUES(?,?,?,?,?)""",
        (now(), args.severity, args.title, args.description, args.status),
    )
    con.commit()
    return int(cur.lastrowid)


def close_issue(con: sqlite3.Connection, args: argparse.Namespace) -> None:
    cur = con.execute(
        "UPDATE issues SET ts_closed=?, status=?, resolution=? WHERE id=?",
        (now(), args.status, args.resolution, args.id),
    )
    if cur.rowcount != 1:
        raise SystemExit(f"Issue {args.id} does not exist")
    con.commit()


def start_run(con: sqlite3.Connection, args: argparse.Namespace) -> int:
    cur = con.execute(
        """INSERT INTO runs
        (ts_start,solver,project,design,setup,case_name,mesh_level,status,input_json,log_path,notes)
        VALUES(?,?,?,?,?,?,?,?,?,?,?)""",
        (
            now(), args.solver, args.project, args.design, args.setup,
            args.case, args.mesh, "running", json_text(args.inputs),
            args.log, args.notes,
        ),
    )
    con.commit()
    return int(cur.lastrowid)


def end_run(con: sqlite3.Connection, args: argparse.Namespace) -> None:
    cur = con.execute(
        """UPDATE runs SET ts_end=?, status=?, duration_s=?, metrics_json=?, log_path=?, notes=?
        WHERE id=?""",
        (
            now(), args.status, args.duration, json_text(args.metrics),
            args.log, args.notes, args.id,
        ),
    )
    if cur.rowcount != 1:
        raise SystemExit(f"Run {args.id} does not exist")
    con.commit()


def hash_file(path: Path) -> tuple[str | None, int | None]:
    if not path.is_file():
        return None, None
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest(), path.stat().st_size


def add_artifact(con: sqlite3.Connection, args: argparse.Namespace) -> int:
    path = Path(args.path).resolve()
    sha256, size = hash_file(path)
    cur = con.execute(
        """INSERT INTO artifacts(ts,kind,path,sha256,bytes,run_id,description)
        VALUES(?,?,?,?,?,?,?)
        ON CONFLICT(path) DO UPDATE SET
          ts=excluded.ts, kind=excluded.kind, sha256=excluded.sha256,
          bytes=excluded.bytes, run_id=excluded.run_id,
          description=excluded.description""",
        (now(), args.kind, str(path), sha256, size, args.run_id, args.description),
    )
    con.commit()
    return int(cur.lastrowid or 0)


def set_handoff(con: sqlite3.Connection, args: argparse.Namespace) -> None:
    con.execute(
        """INSERT INTO handoff(id,updated_at,phase,status,next_step,blocker,summary)
        VALUES(1,?,?,?,?,?,?)
        ON CONFLICT(id) DO UPDATE SET
          updated_at=excluded.updated_at, phase=excluded.phase,
          status=excluded.status, next_step=excluded.next_step,
          blocker=excluded.blocker, summary=excluded.summary""",
        (now(), args.phase, args.status, args.next_step, args.blocker, args.summary),
    )
    con.commit()


def print_summary(con: sqlite3.Connection) -> None:
    handoff = con.execute("SELECT * FROM handoff WHERE id=1").fetchone()
    print("HANDOFF")
    print(json.dumps(dict(handoff) if handoff else {}, ensure_ascii=False, indent=2))
    print("\nOPEN ISSUES")
    issues = [dict(row) for row in con.execute("SELECT * FROM open_issues")]
    print(json.dumps(issues, ensure_ascii=False, indent=2))
    print("\nLATEST ACTIONS")
    actions = [dict(row) for row in con.execute("SELECT * FROM latest_actions")]
    print(json.dumps(actions, ensure_ascii=False, indent=2))


def parser() -> argparse.ArgumentParser:
    root = argparse.ArgumentParser(description=__doc__)
    root.add_argument("--db", type=Path, default=DEFAULT_DB)
    sub = root.add_subparsers(dest="cmd", required=True)

    sub.add_parser("init")

    action = sub.add_parser("action")
    action.add_argument("--phase", required=True)
    action.add_argument("--action", required=True)
    action.add_argument("--result", required=True)
    action.add_argument("--status", default="ok", choices=(
        "planned", "started", "ok", "warning", "failed", "blocked", "skipped"
    ))
    action.add_argument("--tool")
    action.add_argument("--command")
    action.add_argument("--inputs")
    action.add_argument("--duration", type=float)
    action.add_argument("--artifact")

    decision = sub.add_parser("decision")
    decision.add_argument("--topic", required=True)
    decision.add_argument("--decision", required=True)
    decision.add_argument("--rationale", required=True)
    decision.add_argument("--evidence")

    assumption = sub.add_parser("assumption")
    assumption.add_argument("--name", required=True)
    assumption.add_argument("--value", required=True)
    assumption.add_argument("--status", required=True, choices=(
        "unverified", "verified", "rejected", "bounded"
    ))
    assumption.add_argument("--source")
    assumption.add_argument("--impact")

    issue = sub.add_parser("issue")
    issue.add_argument("--severity", required=True, choices=(
        "info", "low", "medium", "high", "critical"
    ))
    issue.add_argument("--title", required=True)
    issue.add_argument("--description", required=True)
    issue.add_argument("--status", default="open", choices=(
        "open", "investigating", "resolved", "accepted", "blocked"
    ))

    close = sub.add_parser("close-issue")
    close.add_argument("--id", required=True, type=int)
    close.add_argument("--status", default="resolved", choices=("resolved", "accepted"))
    close.add_argument("--resolution", required=True)

    run_start = sub.add_parser("run-start")
    run_start.add_argument("--solver", required=True)
    run_start.add_argument("--case", required=True)
    run_start.add_argument("--project")
    run_start.add_argument("--design")
    run_start.add_argument("--setup")
    run_start.add_argument("--mesh")
    run_start.add_argument("--inputs")
    run_start.add_argument("--log")
    run_start.add_argument("--notes")

    run_end = sub.add_parser("run-end")
    run_end.add_argument("--id", required=True, type=int)
    run_end.add_argument("--status", required=True, choices=(
        "ok", "warning", "failed", "hung", "cancelled"
    ))
    run_end.add_argument("--duration", type=float)
    run_end.add_argument("--metrics")
    run_end.add_argument("--log")
    run_end.add_argument("--notes")

    artifact = sub.add_parser("artifact")
    artifact.add_argument("--kind", required=True)
    artifact.add_argument("--path", required=True)
    artifact.add_argument("--description", required=True)
    artifact.add_argument("--run-id", type=int)

    handoff = sub.add_parser("handoff")
    handoff.add_argument("--phase", required=True)
    handoff.add_argument("--status", required=True)
    handoff.add_argument("--next-step", required=True)
    handoff.add_argument("--summary", required=True)
    handoff.add_argument("--blocker")

    sub.add_parser("summary")
    return root


def main() -> None:
    args = parser().parse_args()
    with connect(args.db.resolve()) as con:
        initialise(con)
        if args.cmd == "init":
            print(args.db.resolve())
        elif args.cmd == "action":
            print(add_action(con, args))
        elif args.cmd == "decision":
            print(add_decision(con, args))
        elif args.cmd == "assumption":
            print(add_assumption(con, args))
        elif args.cmd == "issue":
            print(add_issue(con, args))
        elif args.cmd == "close-issue":
            close_issue(con, args)
        elif args.cmd == "run-start":
            print(start_run(con, args))
        elif args.cmd == "run-end":
            end_run(con, args)
        elif args.cmd == "artifact":
            print(add_artifact(con, args))
        elif args.cmd == "handoff":
            set_handoff(con, args)
        elif args.cmd == "summary":
            print_summary(con)


if __name__ == "__main__":
    main()
