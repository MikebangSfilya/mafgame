import dataclasses


@dataclasses.dataclass
class DailyReport:
    title: str
    content: str

@dataclasses.dataclass
class DayTurn:
    daily_report : DailyReport | None = None
    num_day : int | None = None
    turn_count : int | None = None
    local_turn_count : int | None = None
    day_started : bool = False
    day_phase: str = ""
    report_history: list[DailyReport] = dataclasses.field(default_factory=list)
    def to_dict(self):
        return dataclasses.asdict(self)
    def start_day(self):
        if not self.day_started:
            self.day_started = True
            self.day_phase = "Starring Game"
            self.num_day = 1
            self.turn_count = 1
            self.local_turn_count = 0
            print("Game started")
        else:
            print("Game already started")

    def new_turn(self, input_comma: str):
        if input_comma == 'end_day':
            self.end_day()
        elif input_comma == 'new_turn':
            if self.local_turn_count == 2:
                self.end_day()
                self.local_turn_count = 0
            else:
                self.turn_count += 1
                self.local_turn_count += 1
                report = DailyReport(
                    title=f'Turn {self.turn_count}',
                    content = f'Turn {self.turn_count}, Content'
                )
                self.report_history.append(report)
        else:
            raise ValueError(f'Unknown input {input_comma}')
    def end_day(self):
        self.turn_count += 1
        self.day_phase = "Ending Game"
        self.num_day += 1
        print(self.report_history)



