#!/usr/bin/python3
"""island perimeter """


def island_perimeter(grid):
    """Return the perimiter of an island.
    The grid represents water by 0 and land by 1.
    Args:
        grid (list): A list of list of integers representing an island.
    Returns:
        The perimeter of the island defined in grid.
    """
    rows = len(grid)
    cols = len(grid[0])
    island_unit = 0
    connect = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                island_unit += 1
                if r < rows -1 and grid[r+1][c] == 1:
                    connect += 1
                if c < cols - 1 and grid[r][c+1] == 1:
                    connect += 1
    return island_unit * 4 - connect * 2
