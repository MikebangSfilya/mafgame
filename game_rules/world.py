import json
from dataclasses import dataclass
from pathlib import Path


@dataclass
class District:
    name: str
    owner: str | None
    income: int
    defense: int
    heat: int
    tension: int
    feature: str
    neighbors: tuple[str, ...]


@dataclass
class WorldState:
    districts: dict[str, District]

    def is_neighbor(self, source: str, target: str) -> bool:
        return target in self.districts[source].neighbors


def load_initial_world() -> WorldState:
    data = json.loads(Path(__file__).with_name("initial_state.json").read_text())
    districts = {
        item["name"]: District(**(item | {"neighbors": tuple(item["neighbors"])}))
        for item in data["districts"]
    }
    return WorldState(districts=districts)
