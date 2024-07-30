#!/usr/bin/python3
"""The size perimeter """


def island_perimeter(grid):
    """A function that calculate the size perimeter 
    Args:
         grid (list): A list of list of integers (0 or 1)
    Returns:
         The perimeter of the size
    """
    height = len(grid)
    width = len(grid[0])
    size = 0
    edges = 0

    for r in range(height):
        for c in range(width):
            if grid[r][c] == 1:
                size += 1
                if (r > 0 and grid[r-1][c] == 1):
                    edges += 1
                if (c > 0 and grid[r][c-1] == 1):
                    edges += 1
    return size * 4 - edges * 2
