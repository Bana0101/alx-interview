#!/usr/bin/python3
""" a function that calculate the island perimeter """


def island_perimeter(grid):
    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                #check up
                if r == 0 or grid[r-1][c] == 0:
                    perimeter += 1
                #check down
                if r == rows - 1 or grid[r+1][c] == 0:
                    perimeter += 1
                #check left
                if c == 0 or grid[r][c-1] == 0:
                    perimeter += 1
                #check right
                if c == cols - 1 or grid[r][c+1] ==0:
                    perimeter += 1
    return perimeter
