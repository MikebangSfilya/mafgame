---
id: NFR-M-001
type: non-functional
category: Maintainability
priority: Must
status: complete
---

# NFR-M-001: Ограничение объема

Версия 0.1 MUST сохранять малый объем до проверки игрового ядра.

| Metric | Target | Measurement Method |
|--------|--------|--------------------|
| scope_size | 4 района, 2 бригады, 2 врага, 5 приказов | Проверка состава стартовой конфигурации |

## Traces

- **Goal**: [[игра/Project District/product-brief#goals--success-metrics|G-004]]
- **Architecture**: [[игра/Project District/architecture/ADR-002-fixed-data-model|ADR-002]]
