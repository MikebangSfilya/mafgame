---
id: REQ-002
type: functional
priority: Must
traces_to: [G-004]
status: complete
---

# REQ-002: Карта из 4 районов

Система MUST моделировать фиксированную карту из 4 районов: Барная улица, Рынок, Старые дома, Склады.

## User Story

As a игрок, I want to видеть районы, владельцев и риски so that выбирать, где давить, где укрепляться и где собирать деньги.

## Acceptance Criteria

- [ ] У каждого района есть владелец, доход, защита, жара полиции, напряжение, особенность.
- [ ] Районы связаны сеткой 2x2: Барная улица - Рынок, Барная улица - Старые дома, Рынок - Склады, Старые дома - Склады.
- [ ] Давить и атаковать можно только соседний район.
- [ ] Контроль района влияет на доход банды.
- [ ] Стартовое состояние содержит 1 район игрока, 2 района врагов и 1 нейтральный район.

## Traces

- **Goal**: [[игра/Project District/product-brief#goals--success-metrics|G-004]]
- **Architecture**: [[игра/Project District/architecture/ADR-002-fixed-data-model|ADR-002]]
- **Implemented by**: [[игра/Project District/epics/EPIC-002-map-and-state|EPIC-002]]
