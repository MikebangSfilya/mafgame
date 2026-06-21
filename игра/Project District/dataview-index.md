---
type: index
project: Project District
status: complete
created: 2026-05-27
---

# Dataview Index: Project District

## Requirements

```dataview
TABLE id AS ID, priority AS Priority, type AS Type, status AS Status
FROM "игра/Project District/requirements"
WHERE id
SORT id ASC
```

## Epics

```dataview
TABLE id AS ID, priority AS Priority, mvp AS MVP, size AS Size, status AS Status
FROM "игра/Project District/epics"
WHERE id
SORT id ASC
```

## Architecture Decisions

```dataview
TABLE id AS ID, status AS Status, date AS Date, requirements AS Requirements
FROM "игра/Project District/architecture"
WHERE id
SORT id ASC
```

## MVP Epics

```dataview
TABLE id AS ID, size AS Size, requirements AS Requirements
FROM "игра/Project District/epics"
WHERE mvp = true
SORT id ASC
```

## Must Requirements

```dataview
TABLE id AS ID, type AS Type, traces_to AS Goals, status AS Status
FROM "игра/Project District/requirements"
WHERE priority = "Must"
SORT id ASC
```
