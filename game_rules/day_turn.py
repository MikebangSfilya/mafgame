import dataclasses
from enum import StrEnum
from pprint import pp


class DayPhase(StrEnum):
    GameStart = 'Start Game'
    DayStart = 'MORNING PHASE'
    DayEnd = 'END DAY PHASE'
    Planning = 'PLAN PHASE'
    InProgress = 'InProgress Phase'
    NewDay = 'NEW DAY PHASE STARTED'

class Command(StrEnum):
    endDay = 'end_day'
    newTurn = 'new_turn'

@dataclasses.dataclass
class DailyReport:
    title: str
    content: str

#TODO: Rewrite to the most simple print and debud defs
@dataclasses.dataclass
class DayTurn:
    daily_report : DailyReport | None = None
    num_day : int | None = None
    turn_count : int | None = None
    local_turn_count : int | None = None
    day_started : bool = False
    order_phase : list[str] = dataclasses.field(default_factory=lambda:  [
        DayPhase.DayStart,
        DayPhase.Planning,
        DayPhase.InProgress,
        DayPhase.DayEnd
    ])
    day_phase: str = ""
    report_history: list[DailyReport] = dataclasses.field(default_factory=list)
    def to_dict(self):
        return dataclasses.asdict(self)
    def start_day(self):
        if not self.day_started:
            self.day_started = True
            self.day_phase = DayPhase.GameStart
            self.num_day = 0
            self.turn_count = 0
            self.local_turn_count = 0
            print("Game started")
        else:
            print("Game already started")

    def new_turn(self, input_comma: str):
        if input_comma == Command.endDay:
            self.end_day()
            print(DayPhase.NewDay)
        elif input_comma == Command.newTurn:
            if self.local_turn_count == 3:
                self.end_day()
                self.local_turn_count = 0
            elif self.local_turn_count == 0:
                a =DayPhase.DayStart
                print(DayPhase.DayStart)
                self.turn_count += 1
                self.local_turn_count += 1
                self.create_daily_report(a)
            else:
                a = self.order_phase[self.local_turn_count]
                self.turn_count += 1
                self.local_turn_count += 1
                self.create_daily_report(self.order_phase[self.local_turn_count])
                print(a)

        else:
            raise ValueError(f'Unknown input {input_comma}')
    def end_day(self):
        self.turn_count += 1
        self.day_phase = DayPhase.DayEnd
        print(self.day_phase)
        self.num_day += 1
        self.create_daily_report(self.day_phase)
        pp(self.report_history)
        pp(f'Day: {self.num_day}')
        self.report_history = []

    def create_daily_report(self, phase: str) -> None:
        report = DailyReport(
            title=f'Turn {self.turn_count}',
            content=f'Turn {self.turn_count}, Phase: {phase}',
        )
        self.report_history.append(report)

