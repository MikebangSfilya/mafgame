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
class Crew:
    name: str
    strength: int
    caution: int
    loyalty: int
    brutality: int
    experience: int
    status: str

    @property
    def available(self) -> bool:
        return self.status == "ready"


@dataclass
class WorldState:
    districts: dict[str, District]
    gangs: dict[str, Gang]
    crews: dict[str, Crew]

    def is_neighbor(self, source: str, target: str) -> bool:
        return target in self.districts[source].neighbors

    def districts_owned_by(self, gang: str) -> tuple[str, ...]:
        return tuple(
            district.name
            for district in self.districts.values()
            if district.owner == gang
        )

    def summary(self) -> str:
        district_lines = [
            f"- {item.name}: владелец={item.owner or 'нейтральный'}, "
            f"доход={item.income}, защита={item.defense}, жара={item.heat}, "
            f"напряжение={item.tension}, особенность={item.feature}"
            for item in self.districts.values()
        ]
        gang_lines = [
            f"- {item.name}: деньги={item.money}, сила={item.strength}, "
            f"агрессия={item.aggression}, осторожность={item.caution}"
            for item in self.gangs.values()
        ]
        crew_lines = [
            f"- {item.name}: сила={item.strength}, осторожность={item.caution}, "
            f"лояльность={item.loyalty}, жестокость={item.brutality}, "
            f"опыт={item.experience}, состояние={item.status}"
            for item in self.crews.values()
        ]
        return "\n".join(
            ["Районы:", *district_lines, "Банды:", *gang_lines, "Бригады:", *crew_lines]
        )


def load_initial_world() -> WorldState:
    data = json.loads(
        Path(__file__).with_name("initial_state.json").read_text(encoding="utf-8")
    )
    districts = {
        item["name"]: District(**(item | {"neighbors": tuple(item["neighbors"])}))
        for item in data["districts"]
    }
    gangs = {item["name"]: Gang(**item) for item in data["gangs"]}
    crews = {item["name"]: Crew(**item) for item in data["crews"]}
    return WorldState(districts=districts, gangs=gangs, crews=crews)
