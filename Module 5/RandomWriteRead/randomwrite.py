# Writes a series of random integers to a file called randomnum.txt

import random

# Request from the user how many random numbers to generate, and the
# lower/upper bounds of the random numbers’ range
while (True):
    try:
        num = int(input("How many random numbers do you want to generate? "))
        if (num <= 0):
            print("The inputted integer should be positive.")
            continue
    except ValueError:
        print("The value you entered is invalid. Only positive integers are valid.")
    else:
        break

while (True):
    try:
        lower = int(input("What is the lowest the random number should be? "))
        if (lower <= 0):
            print("The inputted integer should be positive.")
            continue
    except ValueError:
        print("The value you entered is invalid. Only positive integers are valid.")
    else:
        break

while (True):
    try:
        upper = int(
            input("What is the upper bound of the random numbers' range? "))
        if (upper <= 0):
            print("The inputted integer should be positive.")
            continue
    except ValueError:
        print("The value you entered is invalid. Only positive integers are valid.")
    else:
        break


# Open and write to file
filename = "randomnum.txt"

try:
    with open(filename, "w") as file:
        try:
            for i in range(num):
                file.write(str(random.randint(lower, upper)) + '\n')
            print("The random numbers were written to " + filename + ".")
        except (OSError, IOError):
            print("Error writing to " + filename + ".")
except (FileNotFoundError, PermissionError, OSError):
    print("Error opening " + filename + ".")
