import pytest

from game_rules.day_turn import DayPhase, DayTurn


def test_start_opens_day_one_with_morning_summary() -> None:
    game = DayTurn()

    summary = game.start()

    assert game.day == 1
    assert game.phase is DayPhase.PLANNING
    assert summary == "Day 1: morning briefing."


def test_confirm_rejects_invalid_orders_and_locks_valid_orders() -> None:
    game = DayTurn()
    game.start()

    with pytest.raises(ValueError, match="Unknown orders: attack"):
        game.assign_orders(["attack"])

    game.orders = ["attack"]
    with pytest.raises(ValueError, match="Unknown orders: attack"):
        game.confirm_day()

    game.assign_orders(["wait", "wait"])
    report = game.confirm_day()

    assert game.orders_locked is True
    assert game.phase is DayPhase.REPORT
    assert report.content == "Resolved 2 order(s)."
    with pytest.raises(RuntimeError, match="cannot be changed"):
        game.assign_orders([])


def test_three_days_complete_with_reports_and_updated_effects() -> None:
    game = DayTurn(temporary_effects={"injured": 2, "alert": 1})
    game.start()

    for expected_day in range(1, 4):
        game.assign_orders([])
        report = game.confirm_day()
        assert report.day == expected_day
        if expected_day < 3:
            assert game.next_day() == f"Day {expected_day + 1}: morning briefing."

    assert game.day == 3
    assert len(game.report_history) == 3
    assert game.temporary_effects == {}
