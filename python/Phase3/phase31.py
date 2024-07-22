"""
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

def subgrid_sum(prefix_sum, top, left, bottom, right):
    result = prefix_sum[bottom][right]
    if top > 0:
        result -= prefix_sum[top-1][right]
    if left > 0:
        result -= prefix_sum[bottom][left-1]
    if top > 0 and left > 0:
        result += prefix_sum[top-1][left-1]
    return result

def max_sum_subgrid(grid, k):
    # Dimensions of the grid
    m = len(grid)
    n = len(grid[0]) if m > 0 else 0
    
    if m == 0 or n == 0:
        return 0

    # Compute the prefix sum matrix
    prefix_sum = [[0] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            prefix_sum[i][j] = grid[i][j]
            if i > 0:
                prefix_sum[i][j] += prefix_sum[i-1][j]
            if j > 0:
                prefix_sum[i][j] += prefix_sum[i][j-1]
            if i > 0 and j > 0:
                prefix_sum[i][j] -= prefix_sum[i-1][j-1]

    max_sum = float('-inf')

    # Iterate over all possible top and bottom rows for subgrids
    for top in range(m):
        for bottom in range(top, m):
            # Iterate over all possible left and right columns for subgrids
            for left in range(n):
                for right in range(left, n):
                    area = (bottom - top + 1) * (right - left + 1)
                    if area < k:
                        current_sum = subgrid_sum(prefix_sum, top, left, bottom, right)
                        max_sum = max(max_sum, current_sum)

    return max_sum if max_sum != float('-inf') else 0

# Example usage
grid = [
    [1, 2, -1, -4, -20],
    [-8, -3, 4, 2, 1],
    [3, 8, 10, 1, 3],
    [-4, -1, 1, 7, -6]
]
k = 6

print(max_sum_subgrid(grid, k))  # Output should be the maximum sum of subgrid with area less than k



def subgrid_sum(prefix_sum, top, left, bottom, right):
    result = prefix_sum[bottom][right]
    if top > 0:
        result -= prefix_sum[top-1][right]
    if left > 0:
        result -= prefix_sum[bottom][left-1]
    if top > 0 and left > 0:
        result += prefix_sum[top-1][left-1]
    return result

def max_sum_subgrid(grid, k):
    # Dimensions of the grid
    m = len(grid)
    n = len(grid[0]) 
    
    if m == 0 or n == 0:
        return 0

    # Compute the prefix sum matrix
    prefix_sum = [[0] * n for x in range(m)]
    for i in range(m):
        for j in range(n):
            prefix_sum[i][j] = grid[i][j]
            if i > 0:
                prefix_sum[i][j] += prefix_sum[i-1][j]
            if j > 0:
                prefix_sum[i][j] += prefix_sum[i][j-1]
            if i > 0 and j > 0:
                prefix_sum[i][j] -= prefix_sum[i][j]

    max_sum = float('-inf')

    # Iterate over all possible top and bottom rows for subgrids
    for top in range(m):
        for bottom in range(top, m):
            # Iterate over all possible left and right columns for subgrids
            for left in range(n):
                for right in range(left, n):
                    area = (bottom - top + 1) * (right - left + 1)
                    if area < k:
                        current_sum = subgrid_sum(prefix_sum, top, left, bottom, right)
                        max_sum = max(max_sum, current_sum)

    return max_sum-1 

# Example usage
grid =  [[1, 2, -1, -4, -20],
 [-8, -3, 4, 2, 1],
 [3, 8, 10, 1, 3],
 [-4, -1, 1, 7, -6]]
k=6


print(max_sum_subgrid(grid, k)) 
"""


 # Output should be the maximum sum of subgrid with area less than k

#prefix_sum: 14, top: 1, left: 2, bottom: 2, right: 3, Expected Output: 17

#prefix_sum: 1, top: 1, left: 0, bottom: 3, right: 1, Expected Output: 8


def max_subgrid_sum(grid, k):
    def calculate_sum(grid, row1, col1, row2, col2):
        total = 0
        for r in range(row1, row2 + 1):
            for c in range(col1, col2 + 1):
                total += grid[r][c]
        return total
    
    rows = len(grid)
    cols = len(grid[0])
    max_sum = float('-inf')
    
    for row1 in range(rows):
        for col1 in range(cols):
            for row2 in range(row1, rows):
                for col2 in range(col1, cols):
                    area = (row2 - row1 ) * (col2 - col1)
                    if area <= k:
                        current_sum = calculate_sum(grid, row1, col1, row2, col2)
                        max_sum = max(max_sum, current_sum)
    
    return max_sum

# Example usage:
grid =   [ [1, 2, ], [-8, - 4], [3, 8], [-4, -1] ]
k = 4

print(max_subgrid_sum(grid, k))  # Output: 29
