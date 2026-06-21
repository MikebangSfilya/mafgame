---
id: REQ-009
type: functional
priority: Could
traces_to: [G-003]
status: complete
---

# REQ-009: Простая 2D-карта

Система MAY заменить консольную карту простой 2D-схемой из 4 прямоугольников с цветом владельца и ключевыми числами.

## User Story

As a игрок, I want to видеть районы визуально so that быстрее понимать фронт конфликта.

## Acceptance Criteria

- [ ] Каждый район показан отдельным блоком.
- [ ] Цвет блока отражает владельца.
- [ ] В блоке видны доход, защита и жара полиции.
- [ ] Связи соседства визуально понятны.
- [ ] Отсутствие 2D-карты не блокирует консольный MVP.

## Traces

- **Goal**: [[игра/Project District/product-brief#goals--success-metrics|G-003]]
- **Architecture**: [[игра/Project District/architecture/ADR-004-report-first-ui|ADR-004]]
- **Implemented by**: [[игра/Project District/epics/EPIC-004-reports-and-feedback|EPIC-004]]
