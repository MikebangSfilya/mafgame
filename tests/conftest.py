from game_rules.day_turn import DayTurn


def make_day_turn(*, started: bool = False) -> DayTurn:
    game = DayTurn()
    if started:
        game.start_day()
    return game
