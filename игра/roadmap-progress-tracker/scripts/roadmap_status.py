#!/usr/bin/env python3
import argparse
import json
import os
import re
from pathlib import Path


ROADMAP_ROW_RE = re.compile(
    r"^\|\s*(?P<wave>[^|]+?)\s*\|\s*(?P<issue_id>ISS-[^|]+?)\s*\|\s*"
    r"(?P<layer>[^|]+?)\s*\|\s*(?P<goal>[^|]+?)\s*\|\s*(?P<priority>[^|]+?)\s*\|\s*"
    r"(?P<dependencies>[^|]+?)\s*\|$"
)
KANBAN_ISSUE_RE = re.compile(r"^- \[(?P<done>[ xX])\]\s+(?P<issue_id>ISS-[^:]+):\s+(?P<title>.+)$")
FENCED_BLOCK_RE = re.compile(r"```(?:text)?\n(?P<body>.*?)\n```", re.DOTALL)


def parse_roadmap(roadmap_path: Path) -> list[dict]:
    issues = []
    for line in roadmap_path.read_text(encoding="utf-8").splitlines():
        match = ROADMAP_ROW_RE.match(line.strip())
        if not match:
            continue
        data = {key: value.strip() for key, value in match.groupdict().items()}
        issues.append(data)
    return issues


def parse_kanban(kanban_path: Path) -> dict:
    sections = {}
    current_section = None
    for raw_line in kanban_path.read_text(encoding="utf-8").splitlines():
        line = raw_line.rstrip()
        if line.startswith("## "):
            current_section = line[3:].strip()
            sections.setdefault(current_section, [])
            continue
        match = KANBAN_ISSUE_RE.match(line)
        if match and current_section:
            sections[current_section].append(
                {
                    "issue_id": match.group("issue_id").strip(),
                    "title": match.group("title").strip(),
                    "done": match.group("done").lower() == "x",
                }
            )
    return sections


def parse_implementation_root(implementation_plan_path: Path) -> str | None:
    text = implementation_plan_path.read_text(encoding="utf-8")
    for match in FENCED_BLOCK_RE.finditer(text):
        body = match.group("body").strip()
        if body.startswith("/"):
            return body
    return None


def build_summary(project_root: Path) -> dict:
    roadmap_path = project_root / "roadmap" / "roadmap.md"
    kanban_path = project_root / "roadmap" / "Kanban.md"
    implementation_plan_path = project_root / "implementation-plan.md"
    worklog_path = project_root / "roadmap" / "worklog.md"

    roadmap_issues = parse_roadmap(roadmap_path)
    kanban_sections = parse_kanban(kanban_path)
    implementation_root = parse_implementation_root(implementation_plan_path)

    kanban_index = {}
    for section, items in kanban_sections.items():
        for item in items:
            kanban_index[item["issue_id"]] = {
                "section": section,
                "done": item["done"],
                "title": item["title"],
            }

    merged = []
    for issue in roadmap_issues:
        kanban = kanban_index.get(issue["issue_id"], {})
        merged.append(
            {
                **issue,
                "kanban_section": kanban.get("section"),
                "kanban_done": kanban.get("done"),
                "kanban_title": kanban.get("title"),
            }
        )

    return {
        "project_root": str(project_root),
        "implementation_root": implementation_root,
        "worklog_exists": worklog_path.exists(),
        "issues": merged,
    }


def detect_project_root_from_code_root(code_root: Path, vault_root: Path | None) -> Path | None:
    candidates = []
    search_roots = []
    if vault_root:
        search_roots.append(vault_root)
    else:
        home = Path.home()
        for default in [home / "obsidian", home / "Obsidian"]:
            if default.exists():
                search_roots.append(default)

    code_root_text = str(code_root.resolve())
    for search_root in search_roots:
        for implementation_plan_path in search_root.rglob("implementation-plan.md"):
            try:
                text = implementation_plan_path.read_text(encoding="utf-8")
            except OSError:
                continue
            if code_root_text not in text:
                continue
            project_root = implementation_plan_path.parent
            if (project_root / "roadmap" / "roadmap.md").exists() and (project_root / "roadmap" / "Kanban.md").exists():
                candidates.append(project_root)

    if len(candidates) == 1:
        return candidates[0]
    if not candidates:
        return None

    candidates.sort(key=lambda path: len(str(path)))
    return candidates[0]


def as_markdown(summary: dict) -> str:
    lines = [
        f"Project root: {summary['project_root']}",
        f"Implementation root: {summary['implementation_root'] or 'not found'}",
        f"Worklog: {'present' if summary['worklog_exists'] else 'missing'}",
        "",
        "| Issue | Wave | Goal | Kanban | Done |",
        "|---|---|---|---|---|",
    ]
    for issue in summary["issues"]:
        lines.append(
            "| {issue_id} | {wave} | {goal} | {kanban_section} | {done} |".format(
                issue_id=issue["issue_id"],
                wave=issue["wave"],
                goal=issue["goal"],
                kanban_section=issue["kanban_section"] or "-",
                done="yes" if issue["kanban_done"] else "no",
            )
        )
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Summarize roadmap and Kanban status.")
    parser.add_argument("--project-root", help="Path to project root inside the vault.")
    parser.add_argument("--code-root", help="Path to the code repository root.")
    parser.add_argument("--vault-root", help="Optional Obsidian vault root for project auto-detection.")
    parser.add_argument("--format", choices=["markdown", "json"], default="markdown")
    args = parser.parse_args()

    if not args.project_root and not args.code_root:
        parser.error("one of --project-root or --code-root is required")

    project_root = None
    if args.project_root:
        project_root = Path(args.project_root).expanduser().resolve()
    else:
        code_root = Path(args.code_root).expanduser().resolve()
        vault_root = Path(args.vault_root).expanduser().resolve() if args.vault_root else None
        project_root = detect_project_root_from_code_root(code_root, vault_root)
        if project_root is None:
            search_hint = str(vault_root) if vault_root else os.path.join(str(Path.home()), "obsidian")
            raise SystemExit(
                f"Could not find a project in the vault for code root {code_root}. "
                f"Try --project-root explicitly or pass --vault-root (searched under {search_hint})."
            )

    summary = build_summary(project_root)

    if args.format == "json":
        print(json.dumps(summary, ensure_ascii=False, indent=2))
    else:
        print(as_markdown(summary))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
