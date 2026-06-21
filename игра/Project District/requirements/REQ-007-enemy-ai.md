---
id: REQ-007
type: functional
priority: Should
traces_to: [G-003]
status: complete
---

# REQ-007: Понятный вражеский ИИ

Вражеские банды SHOULD выбирать одно действие в ход по простым правилам и оставлять следы в отчетах.

## User Story

As a игрок, I want to понимать, почему враги действуют so that воспринимать их как угрозу, а не как случайность.

## Acceptance Criteria

- [ ] Каждая вражеская банда выбирает максимум одну цель в ход.
- [ ] Если денег мало, банда чаще собирает деньги.
- [ ] Если район под угрозой, банда чаще укрепляет его.
- [ ] Если сосед слабый, банда может давить или атаковать.
- [ ] Если игрок недавно атаковал банду, она может мстить.
- [ ] Если жара высокая, банда может залечь на дно.
- [ ] Отчет объясняет выбранную мотивацию.

## Traces

- **Goal**: [[игра/Project District/product-brief#goals--success-metrics|G-003]]
- **Architecture**: [[игра/Project District/architecture/ADR-005-readable-ai|ADR-005]]
- **Implemented by**: [[игра/Project District/epics/EPIC-005-ai-police-winloss|EPIC-005]]
