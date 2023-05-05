# Maze Solver (IT 4401 Final Project)

**Andrew Kim (AHKYQX)**

## Description

This maze solver implements the right-hand rule to solve a maze. It takes in a text file, where "#" characters represent boundaries, and "." characters represent open spaces. The solver also takes in a starting position and an ending position, and visually solves the maze for the user, or determines if there is no solution.

## Prerequisites

-   Python 3.8.10 or higher
-   Valid maze text file (see `Solvable_Maze.txt` or `Unsolvable_Maze.txt' for examples)
    -   Width and height must be equivalent in size
    -   Size must be between 7-14 characters
    -   Must exist in the same directory as `MazeSolver.py`

## Usage

1. Run `python3 MazeSolver.py`
2. Enter the size of the maze (e.g. `12`)
3. Enter the name of the maze text file (e.g. `Solvable_Maze.txt`)
4. Enter the starting position (e.g. `0,2`)

---

# Examples

## Solvable Example

1. Run `python3 MazeSolver.py`
2. Enter `12` for size of the maze
3. Enter `Solvable_Maze.txt` for name of the maze text file
4. Enter `0,2` for the starting position

## Unsolvable Example

1. Run `python3 MazeSolver.py`
2. Enter `12` for size of the maze
3. Enter `Unsolvable_Maze.txt` for name of the maze text file
4. Enter `0,2` for the starting position
