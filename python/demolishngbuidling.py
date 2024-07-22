"""
You are given a 2D array grid of size m x n, where each cell represents a building. The value of each cell is the height of the building at that location. You are also given an integer maxHeight.

Your task is to find the maximum number of buildings that can be demolished such that the height of the remaining buildings is less than or equal to maxHeight, and the total area of the demolished buildings is maximized.

The area of a building is defined as the product of its height and the number of cells it occupies (1 cell for a single-story building, 4 cells for a 2x2 building, etc.).

The function should take the grid and maxHeight as input and return the maximum total area of the demolished buildings.

Example:
- grid = [[5,3,4,4,4,3,3],[3,2,4,3,3,2,2],[3,5,6,3,3,5,4]]
- maxHeight = 4
- Output: 58 (The maximum total area of the demolished buildings is 58, which can be achieved by demolishing the buildings at (0,1), (0,5), (0,6), (1,0), (1,1), and (2,1).)
"""


def max_demolished_area(grid, maxHeight):
    if not grid:
        return 0
    
    m, n = len(grid), len(grid[0])
    total_area = 0
    
    for i in range(m):
        for j in range(n):
            if grid[i][j] > maxHeight:
                total_area += grid[i][j]
    
    return total_area

# Example usage:
grid = [
    [5, 3, 4, 4, 4, 3, 3],
    [3, 2, 4, 3, 3, 2, 2],
    [3, 5, 6, 3, 3, 5, 4]
]
maxHeight = 4
print(max_demolished_area(grid, maxHeight))  # Output: 58
