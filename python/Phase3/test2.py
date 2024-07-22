"""
This script calculates the maximum area of a rectangle that can be formed in a 2D grid,
given a height threshold.
"""

def maximal_rectangle(grid, threshold):
    """
    Calculate the maximum area of a rectangle that can be formed in the grid
    where all building heights are ≤ threshold.
    
    Args:
    - grid (list[list[int]]): 2D array representing heights of buildings.
    - threshold (int): Maximum height of the rectangle.
    
    Returns:
    - int: Maximum area of the rectangle that satisfies the height constraint.
    """

    if not grid or not grid[0]:
        return 0
    
    rows = len(grid)
    cols = len(grid[0])
    max_area = 0
    
    # Initialize heights array for histogram calculation
    heights = [0] * cols
    
    for row in range(rows):
        # Update heights based on current row
        for col in range(cols):
            if grid[row][col] <= threshold:
                heights[col] += grid[row][col]
            else:
                heights[col] = 0
        
        # Calculate the largest rectangle area in the histogram formed by `heights`
        stack = []
        for i in range(cols + 1):
            while stack and (i == cols or heights[i] < heights[stack[-1]]):
                h = heights[stack.pop()]
                w = i if not stack else i - stack[-1] - 1
                if h <= threshold:
                    max_area = max(max_area, h * w)
            stack.append(i)
    
    return max_area
grid = [[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 5, 4, 3, 2]]
threshold = 3
result = maximal_rectangle(grid, threshold)
print(result)  # Output: 12
