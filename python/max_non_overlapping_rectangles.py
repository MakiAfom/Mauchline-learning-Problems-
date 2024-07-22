
"""
#def max_non_overlapping_rectangles(grid):
   
    Given a 2D grid of size m x n, where each cell represents a building, find the maximum number of non-overlapping rectangular areas that can be constructed within the grid, such that each area satisfies the following conditions:

    1. The area must be a rectangle, with its sides parallel to the grid axes.
    2. The area must contain only cells with a value of 1, representing a building.
    3. The area must have a height and width of at least 2 units.
    4. The area must not overlap with any other area.

    Args:
        grid (List[List[int]]): A 2D grid, where grid[i][j] is 1 if there is a building at that cell, and 0 otherwise.

    Returns:
        int: The maximum number of non-overlapping rectangular areas that can be constructed within the grid.


def max_non_overlapping_rectangles(grid):
    m, n = len(grid), len(grid[0])
    used = [[False] * n for _ in range(m)]
    count = 0

    def can_form_rectangle(x, y, h, w):
        for i in range(x, x + h):
            for j in range(y, y + w):
                if i >= m or j >= n or grid[i][j] == 0 or used[i][j]:
                    return False
        return True

    def mark_rectangle(x, y, h, w):
        for i in range(x, x + h):
            for j in range(y, y + w):
                used[i][j] = True

    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1 and not used[i][j]:
                for h in range(2, m - i + 1):
                    for w in range(2, n - j + 1):
                        if can_form_rectangle(i, j, h, w):
                            mark_rectangle(i, j, h, w)
                            count += 1
                            break

    return count

# Example of how to call the function
grid = [
    [1, 1, 0, 1],
    [1, 1, 0, 1],
    [0, 0, 1, 1],
    [1, 1, 1, 1]
]

print(max_non_overlapping_rectangles(grid))  # Replace with your grid to test
Given a 2D grid of size m x n, 
where each cell represents a building, your task is to find the maximum number of non-overlapping rectangular areas that can be constructed within the grid, such that each area satisfies the following conditions:

1. The area must be a rectangle, with its sides parallel to the grid axes.
2. The area must contain only cells with a value of 1, representing a building.
3. The area must have a height and width of at least 2 units.
4. The area must not overlap with any other area.


"""

def max_non_overlapping_rectangles(grid):
    """
    Given a 2D grid of size m x n, where each cell represents a building, find the maximum number of non-overlapping rectangular areas that can be constructed within the grid, such that each area satisfies the following conditions:

    1. The area must be a rectangle, with its sides parallel to the grid axes.
    2. The area must contain only cells with a value of 1, representing a building.
    3. The area must have a height and width of at least 2 units.
    4. The area must not overlap with any other area.

    Args:
        grid (List[List[int]]): A 2D grid, where grid[i][j] is 1 if there is a building at that cell, and 0 otherwise.

    Returns:
        int: The maximum number of non-overlapping rectangular areas that can be constructed within the grid.
    """
    m, n = len(grid), len(grid[0])
    used = [[False] * n for _ in range(m)]
    count = 0

    def can_form_rectangle(x, y, h, w):
        for i in range(x, x + h):
            for j in range(y, y + w):
                if i >= m or j >= n or grid[i][j] == 0 or used[i][j]:
                    return False
        return True

    def mark_rectangle(x, y, h, w):
        for i in range(x, x + h):
            for j in range(y, y + w):
                used[i][j] = True

    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1 and not used[i][j]:
                for h in range(2, m - i + 1):
                    for w in range(2, n - j + 1):
                        if can_form_rectangle(i, j, h, w):
                            mark_rectangle(i, j, h, w)
                            count += 1
                            break

    return count




# Example of how to call the function
grid = [
    [1, 1] ,[2,2],[4,0]]
print(max_non_overlapping_rectangles(grid))  # Replace with your grid to test





#this is what i have submitted in the code 
"""

from typing import List

def max_non_overlapping_rectangles(grid: List[List[int]]) -> int:
  
    Given a 2D grid of size m x n, where each cell represents a building, find the maximum number of non-overlapping rectangular areas that can be constructed within the grid, such that each area satisfies the following conditions:

    1. The area must be a rectangle, with its sides parallel to the grid axes.
    2. The area must contain only cells with a value of 1, representing a building.
    3. The area must have a height and width of at least 2 units.
    4. The area must not overlap with any other area.

    Args:
        grid (List[List[int]]): A 2D grid, where grid[i][j] is 1 if there is a building at that cell, and 0 otherwise.

    Returns:
        int: The maximum number of non-overlapping rectangular areas that can be constructed within the grid.
    
    if not grid or not grid[0]:
        return 0

    m, n = len(grid), len(grid[0])
    max_count = 0

    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                max_count = max(max_count, dfs(grid, i, j, m, n))

    return max_count

def dfs(grid: List[List[int]], i: int, j: int, m: int, n: int) -> int:
    if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == 0:
        return 0

    grid[i][j] = 0
    count = 1

    for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        count = max(count, 1 + dfs(grid, i + di, j + dj, m, n))

    return count

# Unit tests
def test_max_non_overlapping_rectangles():
    assert max_non_overlapping_rectangles([[1,1,1,1],[1,1,1,1],[1,1,1,1]]) == 2
    assert max_non_overlapping_rectangles([[1,0,0,0],[0,0,0,0],[0,0,0,0]]) == 1
    assert max_non_overlapping_rectangles([[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]]) == 1
    assert max_non_overlapping_rectangles([[0,0,0,0],[0,0,0,0],[0,0,0,0]]) == 0
    assert max_non_overlapping_rectangles([[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1]]) == 1

test_max_non_overlapping_rectangles()


"""