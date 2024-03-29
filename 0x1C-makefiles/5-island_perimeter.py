#!/usr/bin/python3
# Author: devbismarkkwaku
"""Calculating the perimeter of an island."""


def island_perimeter(grid):
    """Returns the perimeter of the island described in grid.
    Water is represented by 0 and land by 1.
    Args:
        grid (list): has the lists of islands' integers.
    Returns:
        island's perimeter.
    """
    the_size = 0
    the_width = len(grid[0])
    the_edges = 0
    the_height = len(grid)

    for index in range(the_height):
        for index2 in range(the_width):
            if grid[index][index2] == 1:
                the_size = the_size + 1
                if (index2 > 0 and grid[index][index2 - 1] == 1):
                    the_edges = the_edges + 1
                if (index > 0 and grid[index - 1][index2] == 1):
                    the_edges = the_edges + 1
    perimeter = the_size * 4 - the_edges * 2
    return perimeter
