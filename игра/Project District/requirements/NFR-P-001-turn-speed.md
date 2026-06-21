---
id: NFR-P-001
type: non-functional
category: Performance
priority: Must
status: complete
---

# NFR-P-001: Скорость расчета хода

Ход на карте из 4 районов MUST рассчитываться менее чем за 1 секунду на обычной локальной машине.

| Metric | Target | Measurement Method |
|--------|--------|--------------------|
| turn_resolution_time | < 1s | Замер времени между подтверждением приказов и готовым отчетом |

## Traces

- **Goal**: [[игра/Project District/product-brief#goals--success-metrics|G-002]]
- **Architecture**: [[игра/Project District/architecture/ADR-001-turn-engine|ADR-001]]
