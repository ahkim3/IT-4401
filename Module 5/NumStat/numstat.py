# Reads a series of integer numbers from a file and determines and displays the
# name of file, sum of numbers, count of numbers, average of numbers, maximum
# value, minimum value, and range of values


repeat = 'y'

# Loop until the user wants to quit
while repeat == 'y':
    print()
    filename = input("Enter the name of the file to read: ")

    try:
        nums = []
        with open(filename, "r") as file:
            try:
                for line in file:
                    try:
                        nums.append(int(line.rstrip("\n")))
                    except ValueError:
                        print(
                            "An invalid value was found. Please ensure only integer values are in the file.")
                        break

                # Calculate and print data
                print()
                print("File name: " + filename)
                print("Sum: " + str(sum(nums)))
                print("Count: " + str(len(nums)))
                print("Average: " + str(sum(nums) / len(nums)))
                print("Maximum: " + str(max(nums)))
                print("Minimum: " + str(min(nums)))
                print("Range: " + str(max(nums) - min(nums)))

            except (OSError, IOError):
                print("Error reading from file " + filename + ".")
    except (FileNotFoundError, PermissionError, OSError):
        print("Error opening file " + filename + ".")

    # Ask the user if they want to repeat the program
    print()
    repeat = input("Would you like to evaluate another file? (y/n) ")
