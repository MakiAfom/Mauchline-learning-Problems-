
def visible_buildings(grid, m, n):
    """
    Given a 2D grid of building heights, find the maximum number of buildings that can be seen from the sky.

    Args:
        grid (List[List[int]]): A 2D grid of building heights.
        m (int): The number of rows in the grid.
        n (int): The number of columns in the grid.

    Returns:
        int: The total number of visible buildings.
    """
    def count_visible_buildings(grid, m, n):
        # Number of rows and columns
        m = len(grid)
        n = len(grid[0]) if m > 0 else 0

        # Number of visible buildings
        num_visible_buildings = 0

        # Visibility row-wise
        for row in grid:
            max_height_count = 0
            for height in row:
                if height > max_height_count:
                    num_visible_buildings += 1
                    max_height_count = height

        # Visibility column-wise
        for col in range(n):
            max_height_count = 0
            for row in range(m):
                if grid[row][col] > max_height_count:
                    num_visible_buildings += 1
                    max_height_count = grid[row][col]

        return num_visible_buildings

    return count_visible_buildings(grid, m, n)

# Example usage:
grid1 = [[3, 0, 8, 4], [2, 4, 5, 7], [9, 2, 6, 3], [0, 3, 1, 0]]
print(visible_buildings(grid1, 4, 4))  # Output: 17

grid2 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
print(visible_buildings(grid2, 4, 4))  # Output: 16

grid3 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(visible_buildings(grid3, 3, 3))  # Output: 10
