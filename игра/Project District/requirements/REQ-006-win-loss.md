---
id: REQ-006
type: functional
priority: Must
traces_to: [G-002]
status: complete
---

# REQ-006: Условия победы и поражения

Система MUST иметь простые условия победы и поражения для вертикального среза.

## User Story

As a игрок, I want to иметь понятную цель so that мои решения за 20 дней имели направление.

## Acceptance Criteria

- [ ] Победа засчитывается, если игрок контролирует 3 из 4 районов 5 дней подряд.
- [ ] Альтернативная победа засчитывается, если влияние всех конкурентов уничтожено.
- [ ] Поражение наступает, если игрок теряет все районы.
- [ ] Поражение наступает, если общая жара полиции достигает 10 и начинается большая облава.
- [ ] Вертикальный срез может также завершиться после 20 дней с итоговой оценкой выживания.

## Traces

- **Goal**: [[игра/Project District/product-brief#goals--success-metrics|G-002]]
- **Architecture**: [[игра/Project District/architecture/ADR-001-turn-engine|ADR-001]]
- **Implemented by**: [[игра/Project District/epics/EPIC-005-ai-police-winloss|EPIC-005]]
