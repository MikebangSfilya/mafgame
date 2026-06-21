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
