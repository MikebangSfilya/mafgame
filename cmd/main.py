from game_rules.day_turn import DayTurn


def main():
    game = DayTurn()
    game.start_day()
    while True:
        input_comma = input("Введите команду (new_turn / end_day / quit): ")
        if input_comma == 'quit':
            break

        if not game.day_started:
            game.start_day()
        game.new_turn(input_comma)

if __name__ == "__main__":
    main()