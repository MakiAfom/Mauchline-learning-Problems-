"""
def max_visible_buildings(grid):
    if not grid:
        return 0
    
    m, n = len(grid), len(grid[0])
    
    row_max = [max(row) for row in grid]
    col_max = [max(col) for col in zip(*grid)]
    
    total_visible = 0
    for i in range(m):
        for j in range(n):
            max_visible = max(row_max[i], col_max[j])
            if grid[i][j] == max_visible:
                total_visible += 1
    
    return total_visible

# Example usage:
grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]
print(max_visible_buildings(grid))  # Output: 35
"""


def shortest_path(grid):
    """
    Given a 2D boolean grid, where True represents an obstacle and False represents a walkable cell, find the minimum number of steps required to move from the top-left corner (0, 0) to the bottom-right corner (m-1, n-1), while avoiding all obstacles.

    Args:
        grid (List[List[bool]]): A 2D boolean array representing the grid, where True indicates an obstacle and False indicates a walkable cell.

    Returns:
        int: The minimum number of steps required to reach the bottom-right corner, or -1 if no path exists.
    """
    # Check for edge cases
    if not grid or not grid[0]:
        return -1  # Invalid grid

    rows = len(grid)
    cols = len(grid[0])
    
    # Direction vectors for up, down, left, right
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    # Queue to hold the current position and step count
    queue = [(0, 0, 0)]
    visited = [[False] * cols for _ in range(rows)]
    visited[0][0] = True
    
    while queue:
        row, col, steps = queue.pop(0)
        
        # If we have reached the bottom-right corner
        if row == rows - 1 and col == cols - 1:
            return steps
        
        # Explore all possible directions
        for dr, dc in directions:
            next_row, next_col = row + dr, col + dc
            
            # If the cell is within bounds, not visited, and not an obstacle
            if 0 <= next_row < rows and 0 <= next_col < cols and not visited[next_row][next_col] and not grid[next_row][next_col]:
                visited[next_row][next_col] = True
                queue.append((next_row, next_col, steps + 1))
    
    # If the queue is exhausted without finding a path, return -1
    return -1


