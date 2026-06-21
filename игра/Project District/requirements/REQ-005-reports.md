---
id: REQ-005
type: functional
priority: Must
traces_to: [G-003]
status: complete
---

# REQ-005: Утренние и вечерние отчеты

Система MUST показывать отчеты, которые объясняют, что произошло, почему это произошло и какие параметры изменились.

## User Story

As a игрок, I want to читать понятные отчеты so that доверять игре даже при плохих исходах.

## Acceptance Criteria

- [ ] Утро показывает важные изменения: деньги, жара, угрозы, недовольство, подготовку врагов.
- [ ] Вечер показывает каждый приказ игрока и действие врагов.
- [ ] Каждый отчет содержит итог, текстовое объяснение и список эффектов.
- [ ] Если бригада отклонилась от приказа, отчет MUST объяснить причину.
- [ ] Действия врагов SHOULD объяснять мотивацию: мало денег, низкая защита соседа, месть, высокая жара.

## Traces

- **Goal**: [[игра/Project District/product-brief#goals--success-metrics|G-003]]
- **Architecture**: [[игра/Project District/architecture/ADR-004-report-first-ui|ADR-004]]
- **Implemented by**: [[игра/Project District/epics/EPIC-004-reports-and-feedback|EPIC-004]]
