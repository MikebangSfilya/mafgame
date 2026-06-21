from game_rules.day_turn import DayTurn


def main() -> None:
    game = DayTurn()
    print(game.start())
    while True:
        command = input("Command (wait / confirm / next / quit): ")
        if command == "quit":
            break
        try:
            if command == "wait":
                game.assign_orders(["wait", "wait"])
            elif command == "confirm":
                print(game.confirm_day().content)
            elif command == "next":
                print(game.next_day())
            else:
                print(f"Unknown command: {command}")
        except RuntimeError as error:
            print(error)


if __name__ == "__main__":
    main()
