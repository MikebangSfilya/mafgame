---
session_id: SPEC-project-district-2026-05-27
phase: 3
document_type: requirements-index
status: complete
generated_at: 2026-05-27T20:54:00+03:00
version: 1
dependencies:
  - ../spec-config.json
  - ../product-brief.md
---

# Requirements: Project District

PRD фиксирует минимальный вертикальный срез: 4 района, 2 бригады, 2 вражеские банды, 5 приказов, расчет исходов, отчеты и простая карта. Все требования направлены на проверку ядра непрямого управления.

## Requirement Summary

| Priority | Count | Coverage |
|----------|-------|----------|
| Must Have | 6 | Игровой цикл, карта, приказы, расчет исходов, отчеты, победа/поражение |
| Should Have | 2 | Понятный ИИ врагов, балансируемые параметры |
| Could Have | 1 | Простая 2D-карта вместо консоли |
| Won't Have | 10 | Все крупные системы вне версии 0.1 |

## Functional Requirements

| ID | Title | Priority | Traces To |
|----|-------|----------|-----------|
| [[игра/Project District/requirements/REQ-001-day-loop|REQ-001]] | Дневной игровой цикл | Must | [[игра/Project District/product-brief#goals--success-metrics|G-002]] |
| [[игра/Project District/requirements/REQ-002-district-map|REQ-002]] | Карта из 4 районов | Must | [[игра/Project District/product-brief#goals--success-metrics|G-004]] |
| [[игра/Project District/requirements/REQ-003-crews-and-orders|REQ-003]] | Бригады и 5 приказов | Must | [[игра/Project District/product-brief#goals--success-metrics|G-001]] |
| [[игра/Project District/requirements/REQ-004-outcome-resolution|REQ-004]] | Расчет пяти уровней исходов | Must | [[игра/Project District/product-brief#goals--success-metrics|G-001]] |
| [[игра/Project District/requirements/REQ-005-reports|REQ-005]] | Утренние и вечерние отчеты | Must | [[игра/Project District/product-brief#goals--success-metrics|G-003]] |
| [[игра/Project District/requirements/REQ-006-win-loss|REQ-006]] | Условия победы и поражения | Must | [[игра/Project District/product-brief#goals--success-metrics|G-002]] |
| [[игра/Project District/requirements/REQ-007-enemy-ai|REQ-007]] | Понятный вражеский ИИ | Should | [[игра/Project District/product-brief#goals--success-metrics|G-003]] |
| [[игра/Project District/requirements/REQ-008-balance-config|REQ-008]] | Балансируемые параметры | Should | [[игра/Project District/product-brief#goals--success-metrics|G-004]] |
| [[игра/Project District/requirements/REQ-009-simple-2d-map|REQ-009]] | Простая 2D-карта | Could | [[игра/Project District/product-brief#goals--success-metrics|G-003]] |

## Non-Functional Requirements

| ID | Title | Target |
|----|-------|--------|
| [[игра/Project District/requirements/NFR-P-001-turn-speed|NFR-P-001]] | Скорость расчета хода | Ход на 4 районах считается менее чем за 1 секунду |
| [[игра/Project District/requirements/NFR-U-001-readable-feedback|NFR-U-001]] | Читаемость обратной связи | Каждый приказ объяснен текстом и списком эффектов |
| [[игра/Project District/requirements/NFR-M-001-small-scope|NFR-M-001]] | Ограничение объема | Версия 0.1 не выходит за 4 района, 2 бригады, 5 приказов |

## Data Requirements

| Entity | Description | Key Attributes |
|--------|-------------|----------------|
| District | Район карты | name, owner, income, defense, heat, tension, feature, neighbors |
| Gang | Банда | name, money, strength, aggression, caution, districts, relation_to_player, current_goal |
| Crew | Бригада игрока | name, strength, caution, loyalty, brutality, experience, status |
| Order | Приказ на день | crew, action, target |
| Report | Запись результата | title, text, effects, cause |

## Constraints & Assumptions

### Constraints
- В версии 0.1 карта фиксирована.
- Каждая бригада получает максимум один приказ в день.
- Игрок не видит точные проценты расчета.
- Полиция в 0.1 представлена жарой полиции, а не отдельной фракцией.

### Assumptions
- Прототип может жить без сохранений.
- Все тексты отчетов могут быть шаблонными.
- Случайность нужна, но должна быть объяснимой.

## Traceability Matrix

| Goal | Requirements |
|------|--------------|
| G-001 | REQ-003, REQ-004, REQ-005 |
| G-002 | REQ-001, REQ-006, NFR-P-001 |
| G-003 | REQ-005, REQ-007, REQ-009, NFR-U-001 |
| G-004 | REQ-002, REQ-008, NFR-M-001 |

## References

- Derived from: [[игра/Project District/product-brief|Product Brief]]
- Next: [[игра/Project District/architecture/_index|Architecture]]
