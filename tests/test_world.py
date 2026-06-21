from game_rules.world import load_initial_world


def test_initial_districts_form_fixed_two_by_two_map() -> None:
    world = load_initial_world()

    assert set(world.districts) == {
        "Барная улица",
        "Рынок",
        "Старые дома",
        "Склады",
    }
    assert world.is_neighbor("Барная улица", "Рынок")
    assert world.is_neighbor("Рынок", "Барная улица")
    assert not world.is_neighbor("Барная улица", "Склады")
    assert all(
        district.feature
        and district.income >= 0
        and district.defense >= 0
        and district.heat >= 0
        and district.tension >= 0
        for district in world.districts.values()
    )


def test_initial_gangs_and_ownership_are_fixed() -> None:
    world = load_initial_world()

    assert set(world.gangs) == {"Игрок", "Южные", "Крысы"}
    assert world.districts_owned_by("Игрок") == ("Барная улица",)
    assert world.districts_owned_by("Южные") == ("Рынок",)
    assert world.districts_owned_by("Крысы") == ("Старые дома",)
    assert world.districts["Склады"].owner is None
    assert all(
        gang.money >= 0
        and gang.strength >= 0
        and gang.aggression >= 0
        and gang.caution >= 0
        for gang in world.gangs.values()
    )


def test_player_crews_have_visible_parameters_and_status_controls_availability() -> None:
    world = load_initial_world()

    assert set(world.crews) == {"Быки", "Тени"}
    assert world.crews["Быки"].strength > world.crews["Тени"].strength
    assert world.crews["Тени"].caution > world.crews["Быки"].caution
    assert all(crew.available for crew in world.crews.values())

    world.crews["Быки"].status = "injured"

    assert not world.crews["Быки"].available
    summary = world.summary()
    assert "Барная улица: владелец=Игрок" in summary
    assert "Быки: сила=4" in summary
