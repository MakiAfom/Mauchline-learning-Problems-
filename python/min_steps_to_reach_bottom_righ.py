"""def min_steps_to_reach_bottom_right(grid):
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
print(min_steps_to_reach_bottom_right([[False, False, False],
                                            [True, True, False],
                                            [False, False, False]])) 
    
print(min_steps_to_reach_bottom_right([[False, False, False],
                                            [True, True, True],
                                            [False, False, False]])) 
    
print(min_steps_to_reach_bottom_right([[False, True, False],
                                            [False, True, False],
                                            [False, False, False]]))

"""



def min_steps_to_reach_bottom_right(grid):
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
    queue = [(1, 1, 1)]
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
print(min_steps_to_reach_bottom_right([[False, False, False],
                                            [True, True, False],
                                            [False, False, False]])) 
    
print(min_steps_to_reach_bottom_right([[False, False, False],
                                            [True, True, True],
                                            [False, False, False]])) 
    
print(min_steps_to_reach_bottom_right([[False, True, False],
                                            [False, True, False],
                                            [False, False, False]]))

