from dataclasses import dataclass, field
from enum import StrEnum


class DayPhase(StrEnum):
    NOT_STARTED = "not_started"
    PLANNING = "planning"
    EXECUTION = "execution"
    REPORT = "report"


@dataclass(frozen=True)
class DailyReport:
    day: int
    title: str
    content: str


@dataclass
class DayTurn:
    day: int = 0
    phase: DayPhase = DayPhase.NOT_STARTED
    orders: list[str] = field(default_factory=list)
    orders_locked: bool = False
    morning_summary: str = ""
    report_history: list[DailyReport] = field(default_factory=list)
    temporary_effects: dict[str, int] = field(default_factory=dict)

    def start(self) -> str:
        if self.phase is not DayPhase.NOT_STARTED:
            raise RuntimeError("Game already started")
        self.day = 1
        self.phase = DayPhase.PLANNING
        self.morning_summary = self._morning_summary()
        return self.morning_summary

    def assign_orders(self, orders: list[str]) -> None:
        if self.phase is not DayPhase.PLANNING or self.orders_locked:
            raise RuntimeError("Orders cannot be changed now")
        if unknown := set(orders) - {"wait"}:
            raise ValueError(f"Unknown orders: {', '.join(sorted(unknown))}")
        self.orders = orders.copy()

    def confirm_day(self) -> DailyReport:
        if self.phase is not DayPhase.PLANNING:
            raise RuntimeError("Day can only be confirmed during planning")
        self.assign_orders(self.orders)
        self.orders_locked = True
        self.phase = DayPhase.EXECUTION
        report = DailyReport(
            day=self.day,
            title=f"Day {self.day} report",
            content=f"Resolved {len(self.orders)} order(s).",
        )
        self.report_history.append(report)
        self.phase = DayPhase.REPORT
        return report

    def next_day(self) -> str:
        if self.phase is not DayPhase.REPORT:
            raise RuntimeError("Finish the current day first")
        self.day += 1
        self.temporary_effects = {
            name: days - 1
            for name, days in self.temporary_effects.items()
            if days > 1
        }
        self.orders.clear()
        self.orders_locked = False
        self.phase = DayPhase.PLANNING
        self.morning_summary = self._morning_summary()
        return self.morning_summary

    def _morning_summary(self) -> str:
        return f"Day {self.day}: morning briefing."
