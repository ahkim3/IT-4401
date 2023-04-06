def encode(message):
    cipher = {
        "a": "0",
        "b": "1",
        "c": "2",
        "d": "3",
        "e": "4",
        "f": "5",
        "g": "6",
        "h": "7",
        "i": "8",
        "j": "9",
        "k": "!",
        "l": "@",
        "m": "#",
        "n": "$",
        "o": "%",
        "p": "^",
        "q": "&",
        "r": "*",
        "s": "(",
        "t": ")",
        "u": "-",
        "v": "+",
        "w": "<",
        "x": ">",
        "y": "?",
        "z": "="
    }

    result_message = ""

    # Loop through message and check for each character in cipher
    for character in message:
        if character in cipher:
            result_message += cipher[character]
        else:
            result_message += character

    return result_message


def decode(message):
    decipher = {
        "0": "a",
        "1": "b",
        "2": "c",
        "3": "d",
        "4": "e",
        "5": "f",
        "6": "g",
        "7": "h",
        "8": "i",
        "9": "j",
        "!": "k",
        "@": "l",
        "#": "m",
        "$": "n",
        "%": "o",
        "^": "p",
        "&": "q",
        "*": "r",
        "(": "s",
        ")": "t",
        "-": "u",
        "+": "v",
        "<": "w",
        ">": "x",
        "?": "y",
        "=": "z"
    }

    result_message = ""

    # Loop through message and check for each character in decipher
    for character in message:
        if character in decipher:
            result_message += decipher[character]
        else:
            result_message += character

    return result_message


def print_menu():
    print("Welcome to the Secret Message Encoder/Decoder")
    print("1. Encode a message")
    print("2. Decode a message")
    print("3. Exit")
    print()


def main():
    print_menu()
    choice = input("What would you like to do? ")
    print()

    while (True):
        match choice:
            case "1":  # Encode message
                message = input("Enter a message to encode: ")
                print("Encoded message:", encode(message))
                print()

                print_menu()
                choice = input("What would you like to do? ")
                print()

            case "2":  # Decode message
                message = input("Enter a message to decode: ")
                print("Encoded message:", decode(message))
                print()

                print_menu()
                choice = input("What would you like to do? ")
                print()

            case "3":  # Exit
                break

            case _:  # Invalid choice
                print(
                    choice, "is not a valid choice. Please enter an integer between 1 and 3.")
                choice = input("What would you like to do? ")
                print()


main()
