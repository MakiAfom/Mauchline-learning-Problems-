
def find_shortest_path(grid, start_location, end_location, min_terrain_type):
    """
    Find the shortest path between two locations on a 2D grid, subject to the following constraints:
    1. The path must start at a cell with terrain type 10 and end at a cell with terrain type 10.
    2. The path must only traverse cells with terrain types greater than or equal to the specified minimum terrain type.
    3. The path must minimize the total distance traveled, where the distance between two adjacent cells is 1.
    4. If multiple shortest paths exist, the function should return the one that minimizes the sum of the terrain types along the path.

    Args:
        grid (List[List[int]]): A 2D grid of integers representing the terrain types.
        start_location (Tuple[int, int]): The starting location (x, y).
        end_location (Tuple[int, int]): The ending location (x, y).
        min_terrain_type (int): The minimum required terrain type (between 1 and 9).

    Returns:
        List[Tuple[int, int]]: The shortest path as a list of (x, y) coordinates, or an empty list if no valid path exists.
    """




from collections import deque

def find_shortest_path(grid, start_location, end_location, min_terrain_type):
    m, n = len(grid), len(grid[0])
    queue = deque([(start_location, [start_location], 0, 0)])  # (location, path, distance, terrain_sum)
    visited = set()

    while queue:
        location, path, distance, terrain_sum = queue.popleft()
        x, y = location

        if location == end_location and grid[x][y] == 10:
            return path

        if location in visited or grid[x][y] < min_terrain_type:
            continue

        visited.add(location)

        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < m and 0 <= new_y < n:
                new_location = (new_x, new_y)
                new_path = path + [new_location]
                new_distance = distance + 1
                new_terrain_sum = terrain_sum + grid[new_x][new_y]
                queue.append((new_location, new_path, new_distance, new_terrain_sum))

    return []
unit_tests = [
    {
        "grid": [
            [10, 4, 9, 9, 10],
            [9, 7, 8, 9, 9],
            [8, 6, 7, 8, 9],
            [7, 5, 6, 3, 8],
            [10, 9, 8, 7, 10]
        ],
        "start_location": (0, 0),
        "end_location": (4, 4),
        "min_terrain_type": 7,
        "expectedOutput": [(0, 0), (1, 1), (2, 2), (2, 3), (3, 4), (4, 4)]
    },
    {
        "grid": [
            [10, 4, 9, 9, 10],
            [9, 7, 8, 9, 9],
            [8, 6, 7, 8, 9],
            [7, 5, 6, 3, 8],
            [10, 9, 8, 7, 10]
        ],
        "start_location": (0, 0),
        "end_location": (4, 0),
        "min_terrain_type": 7,
        "expectedOutput": [(0, 0), (1, 1), (2, 0), (3, 0), (4, 0)]
    },
    {
        "grid": [
            [10, 4, 9, 9, 10],
            [9, 7, 8, 9, 9],
            [8, 6, 7, 8, 9],
            [7, 5, 6, 3, 8],
            [10, 9, 8, 7, 10]
        ],
        "start_location": (0, 0),
        "end_location": (4, 4),
        "min_terrain_type": 4,
        "expectedOutput": [(0, 0), (1, 1), (2, 1), (3, 2), (4, 3), (4, 4)]
    }
]

# Running the unit tests
for test in unit_tests:
    result = find_shortest_path(
        test["grid"],
        test["start_location"],
        test["end_location"],
        int(test["min_terrain_type"])
    )
    assert result == test["expectedOutput"], f"Failed for test: {test}"
    print(f"Test Passed for {test}")



"""
from collections import deque
from typing import List, Tuple 


def find_shortest_path(grid: List[List[int]], start_location: Tuple[int, int], end_location: Tuple[int, int], min_terrain_type: int) -> List[Tuple[int, int]]:
    """
    Find the shortest path between two locations on a 2D grid, subject to the following constraints:
    1. The path must start at a cell with terrain type 10 and end at a cell with terrain type 10.
    2. The path must only traverse cells with terrain types greater than or equal to the specified minimum terrain type.
    3. The path must minimize the total distance traveled, where the distance between two adjacent cells is 1.
    4. If multiple shortest paths exist, the function should return the one that minimizes the sum of the terrain types along the path.

    Args:
        grid (List[List[int]]): A 2D grid of integers representing the terrain types.
        start_location (Tuple[int, int]): The starting location (x, y).
        end_location (Tuple[int, int]): The ending location (x, y).
        min_terrain_type (int): The minimum required terrain type (between 1 and 9).

    Returns:
        List[Tuple[int, int]]: The shortest path as a list of (x, y) coordinates, or an empty list if no valid path exists.
    """


    m, n = len(grid), len(grid[0])
    start_x, start_y = start_location
    end_x, end_y = end_location

    # Check if start and end locations are valid
    if grid[start_x][start_y] != 10 or grid[end_x][end_y] != 10:
        return []
    if min_terrain_type < 1 or min_terrain_type > 9:
        return []

    # Initialize the queue for BFS
    queue = deque([(start_x, start_y, [(start_x, start_y)])])
    visited = set()
    visited.add((start_x, start_y))

    while queue:
        x, y, path = queue.popleft()

        # Check if we've reached the end location
        if (x, y) == end_location:
            return path

        # Explore the neighboring cells
        for dx, dy in [(1, 1), (1, -1),(1,1) , (-1,1)]:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < m and 0 <= new_y < n and (new_x, new_y) not in visited and grid[new_x][new_y] >= min_terrain_type:
                visited.add((new_x, new_y))
                new_path = path + [(new_x, new_y)]
                queue.append((new_x, new_y, new_path))

    # No valid path found
    return []

# Test case
grid =[[10, 4, 9, 9, 10],
        [9, 7, 8, 9, 9],
        [8, 6, 7, 8, 9],
        [7, 5, 6, 3, 8],
        [10, 9, 8, 7, 10]]
start_location = (0,0)
end_location = (4, 4)
min_terrain_type =2

shortest_path = find_shortest_path(grid, start_location, end_location, min_terrain_type)
print(shortest_path)
"""