# Rock Paper Scissors
# Andrew Kim

import random, pickle, os


def get_round(rps_info):
    return rps_info["wins"] + rps_info["losses"] + rps_info["ties"] + 1


def initial_menu_selection():
    print("Welcome to Rock, Paper, Scissors!")
    print()
    print("1. Start New Game")
    print("2. Load Game")
    print("3. Quit")
    print()

    while True:
        try:
            choice = input("Enter choice: ")
            print()

            # Verify valid input
            if not choice.isdigit():
                raise TypeError()
            elif choice != "1" and choice != "2" and choice != "3":
                raise ValueError()
            else:
                return choice
        except TypeError:
            print("Please enter a valid integer value.")
            print()
        except ValueError:
            print("Invalid choice. Please try again.")
            print()
        except Exception as e:
            print(e)
            print("Please try again.")
            print()


def initial_menu(repeat_later: bool):
    repeat = True
    while repeat:
        initial_choice = initial_menu_selection()

        if initial_choice == "1":  # Start new game
            repeat = False
            name = new_game()
            rps_info = {"name": name, "wins": 0, "losses": 0, "ties": 0}

            play_game(rps_info)

        elif initial_choice == "2":  # Load game
            name, rps_info, success = load_game()
            if success == True:
                repeat = False
                play_game(rps_info)

        elif initial_choice == "3":  # Quit
            repeat = False
            name = ""
            rps_info = {}
            repeat_later = False

    return name, rps_info, repeat_later


def repeat_menu():
    print("What would you like to do?")
    print()
    print("1. Play Again")
    print("2. View Statistics")
    print("3. Quit")
    print()

    while True:
        try:
            choice = input("Enter choice: ")
            print()

            # Verify valid input
            if not choice.isdigit():
                raise TypeError()
            elif choice != "1" and choice != "2" and choice != "3":
                raise ValueError("Invalid choice")
            else:
                return choice
        except TypeError:
            print("Please enter a valid integer value.")
            print()
        except ValueError:
            print("Invalid choice. Please try again.")
            print()
        except Exception as e:
            print(e)
            print("Please try again.")
            print()


def determine_object(choice):
    if choice == "1":
        return "Rock"
    elif choice == "2":
        return "Paper"
    elif choice == "3":
        return "Scissors"


def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        print("It's a tie!")
        return "tie"
    elif user_choice == "1":
        if computer_choice == "2":
            print("You lose!")
            return "loss"
        elif computer_choice == "3":
            print("You win!")
            return "win"
        else:
            print("Invalid choice. Please try again.")
    elif user_choice == "2":
        if computer_choice == "1":
            print("You win!")
            return "win"
        elif computer_choice == "3":
            print("You lose!")
            return "loss"
        else:
            print("Invalid choice. Please try again.")
    elif user_choice == "3":
        if computer_choice == "1":
            print("You lose!")
            return "loss"
        elif computer_choice == "2":
            print("You win!")
            return "win"
        else:
            print("Invalid choice. Please try again.")
    else:
        print("Invalid choice. Please try again.")
    return "invalid"


def game_choices(round_number):
    print("Round", round_number)
    print()
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    print()

    while True:
        try:
            choice = input("What will it be? ")
            print()

            # Verify valid input
            if not choice.isdigit():
                raise TypeError()
            elif choice != "1" and choice != "2" and choice != "3":
                raise ValueError("Invalid choice")
            else:
                return choice
        except TypeError:
            print("Please enter a valid integer value.")
            print()
        except ValueError:
            print("Invalid choice. Please try again.")
            print()
        except Exception as e:
            print(e)
            print("Please try again.")
            print()


def new_game():
    name = input("What is your name? ")
    print()
    print("Hello ", name, ". Let's play!", sep="")
    print()
    return name


def load_game():
    name = input("What is your name? ")
    print()
    rps_info, success = deserialize(name)
    return name, rps_info, success


def save_game(rps_info: dict, name: str):
    try:
        serialize(rps_info, name)
        print(name, ", your game has been saved.", sep="")
    except Exception as e:
        print("Sorry ", name, ", the game could not be saved.", sep="")
        print(e)


def play_game(rps_info):
    round = get_round(rps_info)

    user_choice = game_choices(round)  # Get user choice
    computer_choice = str(random.randint(1, 3))  # Get computer choice

    print("You chose ", determine_object(user_choice), ". ", sep="", end="")
    print(
        "The computer chose ", determine_object(computer_choice), ". ", sep="", end=""
    )
    round_result = determine_winner(user_choice, computer_choice)
    print()

    if round_result == "win":
        rps_info["wins"] += 1
    elif round_result == "loss":
        rps_info["losses"] += 1
    elif round_result == "tie":
        rps_info["ties"] += 1


def serialize(rps_info: dict, name: str):
    with open(name + ".rps", "wb") as f:
        pickle.dump(rps_info, f)


def deserialize(name: str):
    if os.path.isfile(name + ".rps"):
        # Open file and load game
        with open(name + ".rps", "rb") as f:
            success = True
            rps_info = pickle.load(f)
            print("Welcome back, ", name, ". Let's play!", sep="")
            print()
    else:
        rps_info = []
        success = False
        print(name, ", your game could not be found.", sep="")
        print()
    return rps_info, success


def view_statistics(rps_info: dict, name: str):
    print(name, ", here are your game play statistics...", sep="")
    print("Wins:", rps_info["wins"])
    print("Losses:", rps_info["losses"])
    print("Ties:", rps_info["ties"])
    print()
    try:
        print("Win/Loss Ratio:", "{:.2f}".format(rps_info["wins"] / rps_info["losses"]))
    except ZeroDivisionError:
        print("Win/Loss Ratio: N/A")
    print()


def main():
    repeat = True

    # Initialize game data and start game
    name, rps_info, repeat = initial_menu(repeat)

    # Repeat game options
    while repeat:
        menu_choice = repeat_menu()
        if menu_choice == "1":  # Play again
            play_game(rps_info)
            print()
        elif menu_choice == "2":  # View statistics
            view_statistics(rps_info, name)
        elif menu_choice == "3":  # Quit
            save_game(rps_info, name)
            repeat = False


main()
