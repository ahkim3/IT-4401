# Reads a series of integer numbers from a file and determines and displays the
# name of file, sum of numbers, count of numbers, average of numbers, maximum
# value, minimum value, range, median, and mode of values

def read_file(filename):
    nums = []

    with open(filename, 'r') as file:
        # Read the file's contents as a list of strings.
        unconverted_numbers = file.readlines()
        # Convert the strings to integers and store them in numbers list
        for number in unconverted_numbers:
            nums.append(int(number))
    return nums


def calculate_data(nums):
    results = {}

    results["sum"] = sum(nums)
    results["count"] = len(nums)
    results["avg"] = results["sum"] / results["count"]
    results["max"] = max(nums)
    results["min"] = min(nums)
    results["range"] = results["max"] - results["min"]

    # Calculate the median
    middle = results["count"] // 2
    if (results["count"] % 2 == 0):
        results["median"] = (nums[middle] + nums[middle - 1]) / 2
    else:
        results["median"] = nums[middle]

    # Calculate the mode(s)
    num_counts = {}
    mode = []
    for num in nums:  # Determine frequency of each number
        if num in num_counts:
            num_counts[num] += 1
        else:
            num_counts[num] = 1
    max_count = max(num_counts.values())
    for num in num_counts:  # Find the number with the highest frequency
        if num_counts[num] == max_count:
            mode.append(num)
        results["mode"] = mode
    return results


def display_results(filename, results):
    print()
    print("File name:", filename)
    print("Sum:", results["sum"])
    print("Count:", results["count"])
    print("Average:", results["avg"])
    print("Maximum:", results["max"])
    print("Minimum:", results["min"])
    print("Range:", results["range"])
    print("Median:", results["median"])
    print("Mode:", results["mode"])


def main():
    repeat = 'y'

    # Loop until the user wants to quit
    while repeat == 'y':
        print()
        filename = input("Enter the name of the file to read: ")

        try:
            with open(filename, "r") as file:
                try:
                    nums = read_file(filename)

                    # Ensure that the file isn't empty
                    if (len(nums) == 0):
                        raise ZeroDivisionError

                    nums.sort()
                    results = calculate_data(nums)
                    display_results(filename, results)

                except (ZeroDivisionError):
                    print("Error: No numbers could be found in file.")
                except (OSError, IOError):
                    print("Error reading from file " + filename + ".")
        except (FileNotFoundError, PermissionError, OSError):
            print("Error opening file " + filename + ".")
        except Exception as e:
            print("An error occurred:", e)

        # Ask the user if they want to repeat the program
        print()
        repeat = input("Would you like to evaluate another file? (y/n) ")


main()
