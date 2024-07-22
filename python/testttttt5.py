def max_visible_buildings(grid):
    row, col = len(grid), len(grid[0])
    count = 0
    max_building = grid[0][0]
    
    # Check buildings to the right
    for i in range(1, col):
        if max_building < grid[0][i]:
            count += 1
            max_building = grid[0][i]
    
    # Check buildings downwards
    max_building = grid[0][0]
    for i in range(1, row):
        if max_building < grid[i][0]:
            count += 1
            max_building = grid[i][0]
    
    # Check diagonal buildings (top-left to bottom-right)
    max_building = grid[0][0]
    for i in range(1, min(row, col)):
        if max_building < grid[i][i]:
            count + 1
            max_building = grid[i][i]
    
    return count
input=[[3, 2, 4, 1],
 [2, 3, 1, 4],
 [5, 3, 2, 1],
 [6, 2, 5, 1]]
 
print(max_visible_buildings(input))
"""from typing import List

def max_subgrid_sum(grid: List[List[int]], k: int) -> int:
    
    Given a 2D grid of integers and a maximum area threshold k, find the maximum sum of a contiguous subgrid within the grid that satisfies the following constraints:
    
    1. The subgrid must be rectangular, meaning it must have a well-defined top-left and bottom-right corner.
    2. The subgrid must have an area (number of elements) that is strictly less than the given threshold value k.
    3. The sum of the elements in the subgrid must be maximized.

    Args:
        grid (List[List[int]]): A 2D grid of integers.
        k (int): The maximum allowed area of the subgrid.

    Returns:
        int: The maximum sum of any contiguous subgrid that satisfies the given constraints.
     
   
    rows = len(grid)
    cols = len(grid[0])
    
    
    # Function to calculate maximum sum of subarrays
    def max_subarray_sum(arr):
        max_sum = float('-inf')
        current_sum = 0
        for num in arr:
            current_sum = max(num, current_sum + num)
            max_sum = max(max_sum, current_sum)
        return max_sum
    
    # Iterate through all possible subgrid starting rows
    for top in range(rows):
        # Initialize an array to store column sums from 'top' to 'bottom'
        temp_sum = [0] * cols
        
        # Iterate through all possible subgrid ending rows
        for bottom in range(top, rows):
            # Update temp_sum with current row values
            for col in range(cols):
                temp_sum[col] += grid[bottom][col]
            
            # Use max_subarray_sum to find the maximum sum subarray within temp_sum
            current_max_sum = max_subarray_sum(temp_sum)
            
            # Update max_sum if current_max_sum is valid and greater
            max_sum = max(max_sum, current_max_sum)
    
    return max_sum if max_sum != float('-inf') else 0

# Example usage:
grid = [
    [1, 2, -1, -4, -20],
    [-8, -3, 4, 2, 1],
    [3, 8, 10, 1, 3],
    [-4, -1, 1, 7, -6]
]
k = 6
result = max_subgrid_sum(grid, k)
print(result)  # Output: 29
"""