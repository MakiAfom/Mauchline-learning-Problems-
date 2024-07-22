def minimum_edges_to_remove(n, graph, k, d):
    """
    Finds the minimum weight set of edges to remove from an undirected weighted graph to ensure
    that the remaining graph has exactly k connected components, each with a diameter of at most d.

    Args:
    - n (int): Number of nodes in the graph
    - graph (list of lists): Adjacency list representation of the graph, where each sublist contains tuples (j, w)
      representing neighboring node j and edge weight w of node i.
    - k (int): Desired number of connected components in the final graph
    - d (int): Maximum diameter allowed for each connected component

    Returns:
    - list of tuples: List of tuples (u, v) representing edges that need to be removed
    - int: Total weight of the removed edges
    """
    def calculate_diameter(start_node, n, graph):
        """Calculate the diameter of the connected component starting from start_node."""
        visited = [False] * n
        max_distance = 0

        def bfs(node):
            queue =([(node, 0)])
            visited[node] = True
            max_dist = 0

            while queue:
                current, dist = queue.popleft()
                for neighbor, weight in graph[current]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        queue.append((neighbor, dist + weight))
                        max_dist = max(max_dist, dist + weight)
            return max_dist

        max_distance = bfs(start_node)
        return max_distance
    
    def is_valid_diameter(weight_threshold):
        """Check if we can achieve k components with diameter <= d by removing edges >= weight_threshold."""

        # Create a modified graph by removing edges >= weight_threshold
        modified_graph = {i: [] for i in range(n)}  # Initialize modified graph

        for u in range(n):
            for v, weight in graph[u]:
                if weight < weight_threshold:
                    modified_graph[u].append((v, weight))

        # Check number of components and their diameters
        visited = [False] * n
        components = 0

        for i in range(n):
            if not visited[i]:
                diameter = calculate_diameter(i, n, modified_graph)
                if diameter <= d:
                    components += 1
                    if components > k:
                        return False, float('inf')

        if components == k:
            # Calculate total weight of removed edges
            removed_weight = sum(weight for u in range(n) for v, weight in graph[u] if weight >= weight_threshold)
            total_removed_weight = removed_weight
            return True, removed_weight
        else:
            return False, float('inf')
# Example usage:
n1 = 10
graph1 = [
    [],
    [(1,1),(2,2)],
    [(0,2),(3,4)],
    [(2,4),(4,5),(6,7)],
    [(3,5),(5,6)],
    [(3,6),(4,6),(6,8)],
    [(3,7),(5,8),(7,8)],
    [(6,8),(8,9)],
    [(5,6),(6,7),(7,9)],
    [(7,9)]
]
k1 = 3
d1 = 3

edges_to_remove, total_weight = minimum_edges_to_remove(n1, graph1, k1, d1)
print(f"Edges to remove: {edges_to_remove}, Total weight: {total_weight}")

n2 = 20
graph2 = [
    [],
    [(2,3)],
    [(0,3),(3,2),(4,4)],
    [(0,2),(1,3),(4,5),(5,6)],
    [(2,4),(3,5),(6,7),(7,8)],
    [(3,6),(4,7),(8,9),(9,10)],
    [(3,7),(4,8),(5,9),(10,11)],
    [(4,8),(5,10),(6,11),(11,12)],
    [(4,9),(5,10),(6,11),(12,13)],
    [(5,10),(6,12),(7,13),(13,14)],
    [(5,11),(6,12),(7,13),(14,15)],
    [(6,12),(7,14),(8,15),(15,16)],
    [(7,13),(8,15),(9,16),(16,17)],
    [(8,14),(9,16),(10,17),(17,18)],
    [(9,15),(10,17),(11,18),(18,19)],
    [(10,16),(11,18),(12,19)],
    [],
    [],
    [],
    []
]
k2 = 5
d2 = 4

edges_to_remove, total_weight = minimum_edges_to_remove(n1, graph1, k1, d1)
print(f"Edges to remove: {edges_to_remove}, Total weight: {total_weight}")
