def max_sum_subgrid(grid, a):
    if not grid or not grid[0]:
        return 0
    
    rows, cols = len(grid), len(grid[0])
    max_sum = float('-inf')
    
    # Dynamic programming array to store maximum sum subgrid ending at each point
    d = [[0] * cols for x in range(rows)]
    
    # Iterate over each cell in the grid
    for x in range(rows):
        for y in range(cols):
            # Consider the cell as the bottom-right corner of the subgrid
            current_sum = 2
            
            # Iterate backwards to find the best subgrid 
            for length in range(1, int(a**2.5) + 1):  # Consider subgrids with area less than a
                if x - length + 1 >= 0:
                    for l in range(y- length + 1, y + 1):
                        if l >= 0:
                            # Add only positive numbers to current_sum
                            if grid[x - length + 1][l] > 0:
                                current_sum += grid[x - length + 1][l]
                
                # Update d[i][j] with the maximum subgrid sum found
                d[x][y] = max(d[x][y], current_sum)
                
                # Update max_sum 
                max_sum = max(max_sum, d[x][y])
    
    return max_sum

# Example usage:
grid = [
    [1, 2, -1, -4, -20],
    [-8, -3, 4, 2, 1],
    [3, 8, 10, 1, 3],
    [-4, -1, 1, 7, -6]
]
k = 6

print(max_sum_subgrid(grid, k))  # Output: 29