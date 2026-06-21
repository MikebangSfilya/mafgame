---
id: REQ-008
type: functional
priority: Should
traces_to: [G-004]
status: complete
---

# REQ-008: Балансируемые параметры

Основные числа SHOULD быть вынесены в простую конфигурацию или отдельный блок данных, чтобы их можно было менять без переписывания логики.

## User Story

As a геймдизайнер, I want to быстро менять доходы, защиту и рост жары so that балансировать прототип после плейтеста.

## Acceptance Criteria

- [ ] Доход районов задан данными.
- [ ] Защита районов задана данными.
- [ ] Шумность приказов задана данными.
- [ ] Рост и снижение жары полиции заданы данными.
- [ ] Частота атак ИИ задана данными или явными коэффициентами.
- [ ] Изменение параметра не требует менять код расчета исхода.

## Traces

- **Goal**: [[игра/Project District/product-brief#goals--success-metrics|G-004]]
- **Architecture**: [[игра/Project District/architecture/ADR-002-fixed-data-model|ADR-002]]
- **Implemented by**: [[игра/Project District/epics/EPIC-006-balance-and-playtest|EPIC-006]]
