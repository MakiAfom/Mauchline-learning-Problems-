
def find_max_non_overlapping_areas(grid):
    """
    Find the maximum number of non-overlapping rectangular areas that can be constructed within the given 2D grid, subject to the following constraints:
    1. The area must be a rectangle, with its sides parallel to the grid axes.
    2. The area must contain only cells with a value of 1, representing a building.
    3. The area must have a height and width of at least 2 units.
    4. The area must not overlap with any other area.

    Args:
        grid (List[List[int]]): A 2D grid of integers, where 1 represents a building and 0 represents an empty cell.

    Returns:
        int: The maximum number of non-overlapping rectangular areas that can be constructed within the grid.
    """
    m, n = len(grid), len(grid[0])
    max_areas = 0

    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                # Find the maximum rectangle starting from (i, j)
                max_width, max_height = 2, 2
                while i + max_height - 1 < m and j + max_width - 1 < n:
                    valid = True
                    for x in range(i, i + max_height):
                        for y in range(j, j + max_width):
                            if grid[x][y] == 0:
                                valid = False
                                break
                        if not valid:
                            break
                    if valid:
                        max_areas = max(max_areas, max_width * max_height)
                        max_width += 1
                    else:
                        break
                    max_height += 1

    return max_areas



grid = [ [1, 1, 1, 1], [1, 1, 1, 1],[1,1,1,1]]
print(find_max_non_overlapping_areas(grid))

