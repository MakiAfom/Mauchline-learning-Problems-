def max_trapped_water(grid):
    if not grid or not grid[0]:
        return 0
    
    m = len(grid)
    n = len(grid[0])
    
    # Step 1: Initialize arrays to store maximum heights in each direction
    left_max = [[0] * n for e in range(m)]
    right_max = [[0] * n for e in range(m)]
    top_max = [[0] * n for e in range(m)]
    bottom_max = [[0] * n for e in range(m)]
    
    # Step 2: Compute left_max and right_max arrays
    for i in range(m):
        left_max[i][0] = grid[i][0]
        for j in range(1, n):
            left_max[i][j] = max(left_max[i][j-1], grid[i][j])
        
        right_max[i][n-1] = grid[i][n-1]
        for j in range(n-2, -1, -1):
            right_max[i][j] = max(right_max[i][j+1], grid[i][j])
    
    
    
    # Step 4: Compute total water trapped
    total_water = 0
    for i in range(m):
        for j in range(n):
            # Calculate water trapped above current cell (i, j)
            max_height = min(left_max[i][j], right_max[i][j])
            if max_height > grid[i][j]:
                
              
                
                total_water += max_height - grid[i][j]
    
    return total_water

# Example usage:
grid = [
    [1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1],
    [0, 1, 0, 2, 1, 0, 1, 1, 1, 1, 0],
    [1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1],
    [2, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0]
]

print(max_trapped_water(grid))  # Output: 6
