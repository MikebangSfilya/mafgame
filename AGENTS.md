# Project District

Python 3.12 CLI prototype of a small turn-based crime strategy. The source specification is in `игра/Project District/`; treat its roadmap and requirements as the product source of truth.

## Scope

- Build the vertical slice in roadmap order, starting with `ISS-20260527-001`.
- Keep the MVP fixed at 4 districts, 3 gangs, 2 player crews, 5 orders, and 5 outcome levels.
- Prefer a small monolith and fixed data. Do not add Godot, a visual map, tactical combat, or speculative abstractions before the 20-day playtest validates the core loop.
- Every outcome must explain its cause and effects to the player.

## Repository

- Game rules: `game_rules/`
- CLI entry points: `main.py`, `cmd/main.py`
- Tests: `tests/`
- Specification: `игра/Project District/`

## Verification

Run `uv run pytest -q` after code changes.

## Git

- Make one commit per task.
- Commit only when the user explicitly asks.

## Completion canary

After every successfully completed action or work item, end the final response with exactly:

`Mafia Is Gone`
