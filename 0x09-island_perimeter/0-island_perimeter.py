#!/usr/bin/python3
"""island perimeter """


def island_perimeter(grid):
    """ a function that calculate the island perimeter 
    Args:
         grid : A list of list of integers (0 or 1)
    Return:
         The perimeter of the island
    """
    rows = len(grid)
    cols = len(grid[0])
    island = 0
    connect = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                island += 1
                if (r > 0 and grid[r-1][c] == 1):
                    connect += 1
                if (c > 0 and grid[r][c-1] == 1):
                    connect += 1
    return island * 4 - connect * 2
