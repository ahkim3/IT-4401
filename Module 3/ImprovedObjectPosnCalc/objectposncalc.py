repeat = 'y'

# Loop until the user wants to quit
while repeat == 'y':
    print()  # Add a spacer

    # Obtain and validate user inputs
    while (True):
        try:
            position_initial = float(input("Enter the initial position: "))
        except ValueError:
            print("The value you entered is invalid. Only numerical values are valid.")
        else:
            break

    while (True):
        try:
            velocity_initial = float(input("Enter the initial velocity: "))
        except ValueError:
            print("The value you entered is invalid. Only numerical values are valid.")
        else:
            break

    while (True):
        try:
            acceleration = float(input("Enter the acceleration: "))
        except ValueError:
            print("The value you entered is invalid. Only numerical values are valid.")
        else:
            break

    while (True):
        try:
            time = float(input("Enter the elapsed time: "))
            if (time < 0):
                print("Negative elapsed times are not allowed.")
                continue
        except ValueError:
            print("The value you entered is invalid. Only numerical values are valid.")
        else:
            break

    # Calculate the final position
    position_final = position_initial + velocity_initial * \
        time + 0.5 * acceleration * time ** 2

    # Print the final position to the user
    print("The final position is:", position_final)

    # Ask the user if they want to repeat the program
    repeat = input("Do you want to repeat the program? (y/n): ")
