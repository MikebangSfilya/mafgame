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
class Gang:
    name: str
    money: int
    strength: int
    aggression: int
    caution: int


@dataclass
class WorldState:
    districts: dict[str, District]
    gangs: dict[str, Gang]

    def is_neighbor(self, source: str, target: str) -> bool:
        return target in self.districts[source].neighbors

    def districts_owned_by(self, gang: str) -> tuple[str, ...]:
        return tuple(
            district.name
            for district in self.districts.values()
            if district.owner == gang
        )


def load_initial_world() -> WorldState:
    data = json.loads(Path(__file__).with_name("initial_state.json").read_text())
    districts = {
        item["name"]: District(**(item | {"neighbors": tuple(item["neighbors"])}))
        for item in data["districts"]
    }
    gangs = {item["name"]: Gang(**item) for item in data["gangs"]}
    return WorldState(districts=districts, gangs=gangs)
