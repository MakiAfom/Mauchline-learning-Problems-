def maximal_rectangle_area(grid, threshold):
    if not grid or not grid[0]:
        return 0
    
    m, n = len(grid), len(grid[0])
    max_area = 0
    
    # Directions: right, down, and diagonal (down-right)
    directions = [(0, 1), (1, 0), (1, 1)]
    
    for i in range(m):
        for j in range(n):
            for dir in directions:
                dx, dy = dir
                x, y = i, j
                height = 0
                while x < m and y < n and height <= threshold:
                    height = min(height + grid[x][y], threshold)
                    width = y - j + 1  # Adjusted width calculation
                    max_area = max(max_area, height * width)
                    x += dx
                    y += dy
    
    return max_area


# Example usage

grid = [
    [3, 1, 2, 3, 5],
    [2, 4, 3, 4, 4],
    [2, 3, 5, 3, 1],
    [6, 5, 4, 3, 2]
]

threshold = 3
max_area = maximal_rectangle_area(grid, threshold)
print("Maximum area of the rectangle:", max_area)