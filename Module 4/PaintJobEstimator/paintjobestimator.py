import math

repeat = 'y'

# Loop until the user wants to quit
while repeat == 'y':
    print()  # Add a spacer

    # Obtain and validate user inputs
    while (True):
        try:
            wall_space = float(input("Enter the square feet of wall space: "))
            if (wall_space <= 0):
                print("Only positive wall space values are allowed.")
                continue
        except ValueError:
            print("The value you entered is invalid. Only numerical values are valid.")
        else:
            break

    while (True):
        try:
            price_per_gallon = float(
                input("Enter the price per gallon of paint: "))
            if (price_per_gallon <= 0):
                print("Only positive prices are allowed.")
                continue
        except ValueError:
            print("The value you entered is invalid. Only numerical values are valid.")
        else:
            break

    # Perform calculations
    gallons_required = wall_space / 350
    rounded_gallons_required = int(math.ceil(gallons_required))
    hours_required = 6 * (wall_space / 350)
    paint_cost = price_per_gallon * rounded_gallons_required
    labor_cost = 62.25 * hours_required
    total_cost = paint_cost + labor_cost

    # Display data to user
    print()
    print("The number of gallons of paint required (rounded up) is",
          rounded_gallons_required)
    print("The hours of labor required is", "{:.1f}".format(hours_required))
    print("The cost of the paint is $" + "{:.2f}".format(paint_cost))
    print("The labor charges are $" + "{:.2f}".format(labor_cost))
    print("The total cost of the paint job is $" + "{:.2f}".format(total_cost))
    print()

    # Ask the user if they want to repeat the program
    repeat = input("Would you like to do another estimate? (y/n): ")
