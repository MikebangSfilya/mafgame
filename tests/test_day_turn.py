
from game_rules.day_turn import DayTurn


def test_start_day_initializes_state() -> None:
    game = DayTurn()

    game.start_day()

    assert game.day_started is True
    assert game.day_phase == "Starring Game"
    assert game.num_day == 1
    assert game.turn_count == 1
    assert game.local_turn_count == 0


def test_new_turn_adds_report_history() -> None:
    game = DayTurn()
    game.start_day()

    game.new_turn("new_turn")

    assert game.turn_count == 2
    assert game.local_turn_count == 1
    assert len(game.report_history) == 1
    assert game.report_history[0].title == "Turn 2"


def test_new_turn_rejects_unknown_command() -> None:
    game = DayTurn()
    game.start_day()

    try:
        game.new_turn("bad_command")
    except ValueError as exc:
        assert "Unknown input bad_command" in str(exc)
    else:
        raise AssertionError("ValueError was not raised")
