---
id: NFR-U-001
type: non-functional
category: Usability
priority: Must
status: complete
---

# NFR-U-001: Читаемость обратной связи

Каждый приказ MUST возвращать текстовый отчет, который показывает итог, причину и измененные параметры.

| Metric | Target | Measurement Method |
|--------|--------|--------------------|
| explained_orders | 100% | Проверка вечернего отчета за 20 дней |

## Traces

- **Goal**: [[игра/Project District/product-brief#goals--success-metrics|G-003]]
- **Architecture**: [[игра/Project District/architecture/ADR-004-report-first-ui|ADR-004]]
