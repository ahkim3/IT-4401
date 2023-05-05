import time
import os


# Starting position
class Entrance:
    BEGIN_X = 0
    BEGIN_Y = 0


# Direction of movement
class Direction:
    DOWN = 0
    RIGHT = 1
    UP = 2
    LEFT = 3


# Fill array with maze from a file
def fill(maze, size, inputFileName):
    try:
        with open(inputFileName, "r") as input:
            for line in input:
                maze.append(list(line.strip()))

            # Invert columns and rows
            maze = [[row[i] for row in maze] for i in range(size)]

            # Validate maze size
            if len(maze) != size or len(maze[size - 1]) != size:
                raise IndexError

        return maze

    except FileNotFoundError:
        print("File not found.")
        exit()
    except OSError:
        print("Error reading file.")
        exit()
    except IndexError:
        print("Maze size value does not match file.")
        exit()
    except Exception as e:
        print("Error:", e)
        exit()


# Traverse maze
def mazeTraverse(maze, size, xCurrent, yCurrent, direction, initialStep):
    directionFound = False
    nextDirection = Direction.DOWN
    previousChar = maze[xCurrent][yCurrent]

    # Enforce maze boundaries
    if xCurrent >= 0 and yCurrent >= 0 and xCurrent < size and yCurrent < size:
        maze[xCurrent][yCurrent] = "X"  # Mark current position

        # Briefly wait and print next step in maze
        time.sleep(0.1)
        os.system("cls" if os.name == "nt" else "clear")
        printMaze(maze, size)

        maze[xCurrent][yCurrent] = previousChar  # Restore previous character

        # Continue onto next position if maze is not yet solved
        if not isSolved(size, xCurrent, yCurrent):
            directionFound = False

            # Cycle through directions until a valid move is found
            while not directionFound:
                if direction == Direction.DOWN:
                    if validMove(maze, xCurrent, yCurrent + 1):
                        directionFound = True
                    else:
                        direction = Direction.RIGHT
                elif direction == Direction.RIGHT:
                    if validMove(maze, xCurrent + 1, yCurrent):
                        directionFound = True
                    else:
                        direction = Direction.UP
                elif direction == Direction.UP:
                    if validMove(maze, xCurrent, yCurrent - 1):
                        directionFound = True
                    else:
                        direction = Direction.LEFT
                elif direction == Direction.LEFT:
                    if validMove(maze, xCurrent - 1, yCurrent):
                        directionFound = True
                    else:
                        direction = Direction.DOWN

            # Check if maze is unsolvable
            if not initialStep and (
                (
                    xCurrent == Entrance.BEGIN_X - 1
                    and yCurrent == Entrance.BEGIN_Y
                    or xCurrent == Entrance.BEGIN_X
                    and yCurrent == Entrance.BEGIN_Y - 1
                )
                or (xCurrent == Entrance.BEGIN_X and yCurrent == Entrance.BEGIN_Y)
            ):
                print("\nMaze is unsolvable.\n")
                return

            # Move onto next step in maze
            if direction == Direction.DOWN:
                nextDirection = Direction.LEFT
                yCurrent += 1
            elif direction == Direction.RIGHT:
                nextDirection = Direction.DOWN
                xCurrent += 1
            elif direction == Direction.UP:
                nextDirection = Direction.RIGHT
                yCurrent -= 1
            elif direction == Direction.LEFT:
                nextDirection = Direction.UP
                xCurrent -= 1
            mazeTraverse(maze, size, xCurrent, yCurrent, nextDirection, False)


# Determine if moving to a specified position in a maze is allowed
def validMove(maze, xCoord, yCoord):
    if maze[xCoord][yCoord] == "#":  # Specified position is a border
        return False
    return True


# Determines if exit of maze has been reached
def isSolved(size, xCurrent, yCurrent) -> bool:
    # Edge of array has been reached AND it's not the entrance
    if (
        xCurrent != Entrance.BEGIN_X
        and yCurrent != Entrance.BEGIN_Y
        and (
            xCurrent == 0
            or xCurrent == (size - 1)
            or yCurrent == 0
            or yCurrent == (size - 1)
        )
    ):
        print("\nMaze solved!")
        return True
    return False


def printMaze(maze, size):
    for j in range(size):
        for i in range(size):
            print(maze[i][j], end=" ")
        print()
    print()


def main():
    maze = []

    try:
        # Ask user for maze size
        try:
            size = int(input("Enter maze size (between 7-14): "))
            if size < 7 or size > 14:  # Validate maze size
                raise Exception()
        except ValueError or Exception:
            raise Exception("Invalid maze size.")

        # Fill maze array with maze from file
        fileName = input("Enter maze file name: ")  # Ask user for maze file
        maze = fill(maze, size, fileName)

        direction = Direction.DOWN

        # Ask user for starting position
        try:
            rawStartingInput = input("Enter starting position (ie: x,y): ")

            # Check if input is in (x,y) format
            if (
                len(rawStartingInput) != 3
                or not rawStartingInput[0].isdigit()
                or not rawStartingInput[1] == ","
                or not rawStartingInput[2].isdigit()
            ):
                raise TypeError

            Entrance.BEGIN_X, Entrance.BEGIN_Y = map(int, rawStartingInput.split(","))
        except TypeError or ValueError or Exception:
            raise Exception("Invalid starting position.")

        # Validate maze
        if maze[Entrance.BEGIN_X][Entrance.BEGIN_Y] != ".":  # Entrance is not empty
            print(maze[Entrance.BEGIN_X][Entrance.BEGIN_Y])
            raise Exception("Invalid maze entrance.")

        mazeTraverse(maze, size, Entrance.BEGIN_X, Entrance.BEGIN_Y, direction, True)

    except KeyboardInterrupt:
        print("\nProgram terminated.")
        exit()

    except Exception as e:
        print("Error:", e)
        exit()


main()
