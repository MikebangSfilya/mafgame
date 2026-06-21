---
name: roadmap-progress-tracker
description: Audit implementation progress against a project roadmap, verify whether specific features or functions are truly done, update Kanban/backlog notes, and append factual worklog entries inside an Obsidian vault. Use when the user asks whether something from the roadmap is finished, wants to compare code against `roadmap/roadmap.md` or `roadmap/Kanban.md`, wants backlog grooming, or wants a concise log of what was done and what remains.
---

# Roadmap Progress Tracker

Use Russian by default unless the user explicitly asks otherwise.

Treat the current working directory as the code project root by default.
If the roadmap files are not in the current directory, find the matching Obsidian project by searching for an `implementation-plan.md` that references the current code path.

For the current game project, the expected code root is `/home/sfilya/mafgame`.

## Core Capabilities

1. Verify whether a roadmap item is actually implemented.
2. Compare roadmap scope against code and tests.
3. Update `roadmap/Kanban.md` conservatively.
4. Append a factual worklog entry with `done` and `next`.
5. Keep backlog items small and actionable.

## Files To Look For

First, locate the active code project folder. Then locate the matching design/roadmap folder. Prefer these files:

- current working directory or user-provided code path;
- `roadmap/roadmap.md`
- `roadmap/Kanban.md`
- `implementation-plan.md`
- `roadmap/issues.jsonl`

If the current directory is the code repo and does not contain roadmap files, search the user's vault for `implementation-plan.md` and match it against the absolute code path.

If the vault has several matching projects, ask one short question only when the target project is genuinely ambiguous.

Use `scripts/roadmap_status.py --code-root <cwd>` for the first pass. It can auto-detect the project folder in the vault.

If `implementation-plan.md` contains a code path in a fenced block, treat that path as the canonical implementation root and inspect it before deciding whether something is done.

## Default Workflow

1. Start from the current code project root.
2. Run `scripts/roadmap_status.py --code-root <cwd> --format markdown` to find the linked project folder in the vault and print the current issue list.
3. Read `roadmap/roadmap.md`, `roadmap/Kanban.md`, and `implementation-plan.md` from the detected project folder.
4. If the user asks whether a feature/function is done, inspect the codebase at the implementation root:
   - search for the feature, function, class, command, output text, tests, and any saved artifacts;
   - compare findings to the issue's `Criteria`, `Verification`, `DoD`, `Scope`, and dependencies;
   - distinguish `implemented`, `partially implemented`, `not found`, and `unclear`.
5. Update notes only after inspection. Never mark an issue done from user claims alone.
6. When the user gives a raw dump of completed work, normalize it into atomic factual bullets and update the worklog plus the relevant Kanban issue.

## Audit Rules

When checking whether something is done:

- Require code, tests, or a reproducible artifact as evidence.
- If the code exists but verification is missing, keep the issue in progress and note the missing proof.
- If part of the scope is done, say exactly which part and which acceptance criteria remain open.
- If dependencies are not done, do not mark the dependent issue done even if some code exists.
- Prefer file references and concrete evidence over general statements.

Use these status labels in your own summary:

- `done`: acceptance criteria appear satisfied and evidence exists;
- `in progress`: meaningful code exists but criteria are not yet satisfied;
- `blocked`: dependency, missing environment, or external decision prevents completion;
- `not started`: no credible implementation evidence found.

## Kanban Update Rules

Preserve the existing board structure. Keep diffs minimal.

- Move an item to `Done` only with evidence.
- Leave unchecked items unchecked if the proof is incomplete.
- Add short indented bullets under the issue only when they clarify evidence, gaps, or next actions.
- Put newly discovered future tasks into `## Backlog`, not into `Done`.
- Prefer one backlog item per concrete next step.

## Worklog Rules

Use `roadmap/worklog.md` if it exists. Otherwise create it using the template in `references/worklog-template.md`.

Append entries in this format:

```markdown
## DD.MM.YYYY

### Что сделал
- ...

### Что проверить
- ...

### Что дальше
- ...

### Связанные issue
- ISS-...
```

Rules:

- Keep bullets short and factual.
- Do not invent work that the user did not mention and that the code does not show.
- Mention issue IDs whenever they are known.
- If the same date already exists, append to that block instead of creating a new heading.

## Backlog Grooming

When the user asks to fill the backlog:

1. Read the roadmap waves and dependencies.
2. Read the current Kanban board.
3. Derive only the next small tasks that unblock the next issue.
4. Write backlog items as execution-sized steps, not vague themes.

Good:

- `ISS-20260527-001: добавить переход вечер -> следующий день`
- `ISS-20260527-003: покрыть приказ "сбор дани" ручным сценарием`

Bad:

- `доделать игру`
- `заняться балансом`

## Editing Rules

- Inspect files before editing.
- Use minimal diffs and preserve markdown/frontmatter.
- Do not rewrite the roadmap structure unless the user asks.
- Prefer appending instead of reorganizing old notes.

## Resources

- `scripts/roadmap_status.py`: detect the matching Obsidian project from the code repo path, parse roadmap/Kanban/implementation plan, and print a compact status summary.
- `references/worklog-template.md`: template for `roadmap/worklog.md`.
