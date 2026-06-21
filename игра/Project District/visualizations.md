---
type: visualization
project: Project District
status: complete
created: 2026-05-27
---

# Visualizations: Project District

## Документная цепочка

```mermaid
graph LR
    A[00-Обзор] --> B[Product Brief]
    B --> C[Requirements]
    C --> D[Architecture]
    D --> E[Epics]
    E --> F[Roadmap]
    F --> G[Kanban]
```

## Цикл игрового дня

```mermaid
stateDiagram-v2
    [*] --> Morning
    Morning --> Planning: показать сводку
    Planning --> ResolvePlayerOrders: подтвердить приказы
    ResolvePlayerOrders --> ResolveEnemyActions: приказы игрока рассчитаны
    ResolveEnemyActions --> PoliceReaction: враги ответили
    PoliceReaction --> EveningReport: полиция отреагировала
    EveningReport --> WinLossCheck: игрок прочитал отчет
    WinLossCheck --> Morning: следующий день
    WinLossCheck --> Victory: победа
    WinLossCheck --> Defeat: поражение
```

## Поток расчета приказа

```mermaid
flowchart TD
    A[Игрок выбирает бригаду] --> B[Выбирает приказ]
    B --> C[Выбирает цель]
    C --> D[Система показывает качественную оценку]
    D --> E{Игрок подтверждает?}
    E -->|Нет| B
    E -->|Да| F[Расчет успеха]
    F --> G[Расчет риска полиции]
    G --> H[Расчет риска самовольства]
    H --> I[Бросок случайности]
    I --> J{Исход}
    J --> K[Полный успех]
    J --> L[Успех с осложнением]
    J --> M[Частичный успех]
    J --> N[Провал]
    J --> O[Катастрофа]
    K --> P[Применить эффекты]
    L --> P
    M --> P
    N --> P
    O --> P
    P --> Q[Сформировать отчет с причиной и эффектами]
```

## Зависимости эпиков

```mermaid
graph LR
    E1[EPIC-001<br/>Базовый дневной цикл] --> E2[EPIC-002<br/>Карта и состояние]
    E2 --> E3[EPIC-003<br/>Приказы и исходы]
    E3 --> E4[EPIC-004<br/>Отчеты]
    E3 --> E5[EPIC-005<br/>Враги, полиция, победа]
    E4 --> E6[EPIC-006<br/>Баланс и плейтест]
    E5 --> E6
```

## Трассировка от целей к реализации

```mermaid
graph TD
    G1[G-001<br/>Проверить непрямое управление] --> R3[REQ-003<br/>Бригады и приказы]
    G1 --> R4[REQ-004<br/>Расчет исходов]
    G2[G-002<br/>Полный дневной цикл] --> R1[REQ-001<br/>Дневной цикл]
    G2 --> R6[REQ-006<br/>Победа и поражение]
    G3[G-003<br/>Понятные последствия] --> R5[REQ-005<br/>Отчеты]
    G3 --> R7[REQ-007<br/>Понятный ИИ]
    G4[G-004<br/>Малый объем] --> R2[REQ-002<br/>4 района]
    G4 --> R8[REQ-008<br/>Балансируемые параметры]
    R1 --> E1[EPIC-001]
    R2 --> E2[EPIC-002]
    R3 --> E3[EPIC-003]
    R4 --> E3
    R5 --> E4[EPIC-004]
    R6 --> E5[EPIC-005]
    R7 --> E5
    R8 --> E6[EPIC-006]
```

## Состояния бригады

```mermaid
stateDiagram-v2
    [*] --> free
    free --> busy: получила приказ
    busy --> free: приказ выполнен
    busy --> wounded: потери
    wounded --> free: восстановилась
    free --> lying_low: залечь на дно
    lying_low --> free: вернулась
    busy --> arrested: рейд / катастрофа
    busy --> missing: катастрофа
    arrested --> [*]
    missing --> [*]
```

## Волны roadmap

```mermaid
gantt
    title Project District Roadmap
    dateFormat  YYYY-MM-DD
    axisFormat  %d.%m
    section Wave 1
    ISS-001 MVP Skeleton     :a1, 2026-05-27, 2d
    ISS-002 MVP State        :a2, after a1, 2d
    section Wave 2
    ISS-003 Playable Core    :b1, after a2, 4d
    ISS-004 Feedback         :b2, after b1, 3d
    section Wave 3
    ISS-005 World Pressure   :c1, after b1, 3d
    section Wave 4
    ISS-006 Validation       :d1, after b2, 2d
```
