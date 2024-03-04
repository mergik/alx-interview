#!/usr/bin/python3
"""returns the perimeter of the island described in grid"""

def island_perimeter(grid):
    """returns the perimeter of the island described in grid"""
    total = 0
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            if grid[x][y] == 1:
                total += 4
                if x != 0 and grid[x - 1][y] == 1:
                    total -= 2
                if y != 0 and grid[x][y - 1] == 1:
                    total -= 2
    return total
