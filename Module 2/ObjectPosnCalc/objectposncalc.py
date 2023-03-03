# Obtain user inputs
position_initial = float(input("Enter the initial position: "))
velocity_initial = float(input("Enter the initial velocity: "))
acceleration = float(input("Enter the acceleration: "))
time = float(input("Enter the time: "))

# Calculate the final position
position_final = position_initial + velocity_initial * \
    time + 0.5 * acceleration * time ** 2

# Print the final position to the user
print("The final position is: " + str(position_final))
