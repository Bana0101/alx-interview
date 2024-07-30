#!/usr/bin/python3
"""island perimeter """


def island_perimeter(grid):
    """ a function that calculate the island perimeter 
    Args:
         grid : A list of list of integers (0 or 1)
    """
    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                if r == 0 or grid[r-1][c] == 0:
                    perimeter += 1
                if r == rows - 1 or grid[r+1][c] == 0:
                    perimeter += 1
                if c == 0 or grid[r][c-1] == 0:
                    perimeter += 1
                if c == cols - 1 or grid[r][c+1] ==0:
                    perimeter += 1
    return perimeter
