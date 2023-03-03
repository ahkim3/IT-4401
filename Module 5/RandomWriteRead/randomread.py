# Reads a series of random numbers from a file called randomnum.txt, counts how
# many there are, displays the random numbers, and displays the count

filename = "randomnum.txt"

try:
    with open(filename, "r") as file:
        try:
            count = 0
            print("List of random numbers in " + filename + ":")
            for line in file:
                print(line.rstrip("\n"))
                count += 1
            print()
            print("Random number count: " + str(count))
        except (OSError, IOError):
            print("Error reading from file " + filename + ".")
except (FileNotFoundError, PermissionError, OSError):
    print("Error opening file " + filename + ".")
