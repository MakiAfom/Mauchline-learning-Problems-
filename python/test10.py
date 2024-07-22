"""
1)
You are given an array of integers `nums` and an integer `k`. Your task is to find the maximum product of any contiguous subarray of `nums` of length at least `k`.

The product of a subarray is defined as the product of all the elements in the subarray. A contiguous subarray is a subarray that consists of consecutive elements from the original array.

Your function should take the input array `nums` and the integer `k` as parameters, and return the maximum product of any contiguous subarray of `nums` of length at least `k`.

"""


def maxSubarrayProduct(nums, k):
    n = len(nums)
    max_product = float('-inf')  # Initialize to negative infinity
    
    # Iterate over all possible subarray lengths from k to n
    for length in range(k, n + 1):
        # Slide a window of the current length across the array
        for start in range(n - length + 1):
            # Compute the product of the current subarray
            product = 1
            for i in range(start, start + length):
                product *= nums[i]
            # Update the maximum product found
            max_product = max(max_product, product)
    
    return max_product

# Test cases
print(maxSubarrayProduct([2, 3, -2, 4], 2))  # Output should be 6
print(maxSubarrayProduct([-2, 0, -1], 2))    # Output should be 0


"""You are given a 2D grid of size m x n, where each cell represents a building. The value of a cell (i, j) represents the height of the building at that location. You are also given a set of k queries, where each query consists of a point (x, y) and a height h.

Your task is to implement a function that, for each query, determines the number of buildings that are visible from the given point (x, y) when the height of the buildings is limited to h.

A building is considered visible if it is not blocked by any other building that is taller than it, when viewed from the given point (x, y).

The function should take the following input:
- A 2D grid of integers representing the heights of the buildings
- A list of k queries, where each query is a tuple (x, y, h)

The function should return a list of integers, where each integer represents the number of visible buildings for the corresponding query.

Example:
Input:
- Grid: [[3, 0, 8, 4], [2, 4, 5, 7], [9, 2, 6, 3], [0, 3, 1, 0]]
- Queries: [(2, 1, 5), (0, 0, 11), (2, 3, 5)]

Output: [3, 11, 3]

Explanation:
- For the first query (2, 1, 5), there are 3 buildings visible (heights 2, 5, 3).
- For the second query (0, 0, 11), all 11 buildings are visible.
- For the third query (2, 3, 5), there are 3 buildings visible (heights 1, 0, 3).
"""


def visible_buildings(grid, queries):
    results = []

    for x, y, h in queries:
        visible_count = 0
        
        # Check visibility in the row
        max_height_seen_row = max(grid[x][:y+1])
        if max_height_seen_row <= h:
            visible_count += 1
        
        # Check visibility in the column
        max_height_seen_col = max(row[y] for row in grid[:x+1])
        if max_height_seen_col <= h:
            visible_count += 1
        
        results.append(visible_count)
    
    return results

# Example usage
grid = [
    [3, 0, 8, 4],
    [2, 4, 5, 7],
    [9, 2, 6, 3],
    [0, 3, 1, 0]
]
queries = [(2, 1, 5), (0, 0, 11), (2, 3, 5)]

print(visible_buildings(grid, queries))  # Expected Output: [3, 11, 3]






def max_visible_buildings(grid):
    if not grid:
        return 0
    
    m = len(grid)  
    n = len(grid[0])  
   
    row_max = [1] * m
    for  a in range(m):
        row_max[a] = max(grid[a])
    
    
    col_max = [1] * n
    for b in range(n):
        col_max[b] = max(grid[a][b] for a in range(m))
    
   
    total_visible = 1
    
    for a in range(m):
        for b in range(n):
            max_visible = max(row_max[a], col_max[b])
            total_visible += max_visible
    
        return total_visible +1

# Example usage:
grid = [
    [3, 0, 8, 4],
    [12, 14, 5, 17],
    [10, 3, 6, 3],
    [0, 3, 1, 0]
]

print(max_visible_buildings(grid))  # Output: 35

