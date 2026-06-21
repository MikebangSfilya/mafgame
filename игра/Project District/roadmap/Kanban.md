---

kanban-plugin: board
project: Project District
status: active
created: 2026-05-27

---

## Project District Kanban



## Backlog

- [ ] ISS-20260527-006: [Validation] 20-дневный плейтест и баланс
	  - Depends on: ISS-20260527-004, ISS-20260527-005
	  - DoD: есть лог 20 дней и решение, расширять карту или чинить ядро.


## Wave 1 - MVP Skeleton

- [ ] ISS-20260527-001: [MVP Skeleton] Дневной цикл прототипа
	  - Scope: старт игры, счетчик дней, фазы дня, отчет-заглушка.
	  - Verify: пройти 3 дня без ошибок.
	  - Note 30.05.2026: заложен черновой DayTurn и базовый тестовый каркас как подготовка к issue; acceptance criteria еще не реализованы и статус не менялся.
- [ ] ISS-20260527-002: [MVP State] Карта, банды и бригады
	  - Depends on: ISS-20260527-001
	  - Scope: 4 района, 3 банды, 2 бригады, стартовое владение.
	  - Verify: вывести стартовое состояние и сверить с PRD.


## Wave 2 - Playable Core

- [ ] ISS-20260527-003: [Playable Core] 5 приказов и расчет исходов
	  - Depends on: ISS-20260527-002
	  - Scope: 5 приказов, 5 исходов, успех, риск полиции, самовольство.
	  - Verify: каждый приказ выполнить минимум 3 раза.
- [ ] ISS-20260527-004: [Playable Feedback] Оценки риска и отчеты
	  - Depends on: ISS-20260527-003
	  - Scope: качественные оценки, утро, вечер, cause/effects.
	  - Verify: пройти 5 дней и проверить отчеты.


## Wave 3 - World Pressure

- [ ] ISS-20260527-005: [World Pressure] Враги, полиция, победа и поражение
	  - Depends on: ISS-20260527-003
	  - Scope: rule-based враги, жара, рейды, win/loss.
	  - Verify: сценарии высокой жары, слабого района и контроля 3 районов.


## Done





%% kanban:settings
```
{"kanban-plugin":"board"}
```
%%