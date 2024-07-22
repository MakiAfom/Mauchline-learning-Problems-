"""
from collections import defaultdict
from heapq import heappush, heappop

def minimum_edges_to_remove(n, graph, k, d):
      
    Given an undirected weighted graph represented as an adjacency list, find the minimum weight set of edges that need to be removed from the graph to ensure that the remaining graph has exactly k connected components, where each connected component has a diameter (the maximum distance between any two nodes in the component) of at most d.

    Args:
        n (int): The number of nodes in the graph.
        graph (list[list[tuple[int, int]]]): The adjacency list representation of the graph, where each inner list contains tuples (j, w) representing the neighboring node j and the weight w of the edge between nodes i and j.
        k (int): The desired number of connected components in the final graph.
        d (int): The maximum diameter allowed for each connected component.

    Returns:
        list[tuple[int, int]]: A list of tuples (u, v) representing the edges that need to be removed from the graph.
        int: The total weight of the removed edges.

        
    
    edges = []
    for i, neighbors in enumerate(graph):
        for j, w in neighbors:
            if i < j:
                edges.append((w, i, j))
    edges.sort()

    parent = list(range(n))
    rank = [0] * n

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        x_root = find(x)
        y_root = find(y)
        if x_root == y_root:
            return
        if rank[x_root] < rank[y_root]:
            parent[x_root] = y_root
        elif rank[x_root] > rank[y_root]:
            parent[y_root] = x_root
        else:
            parent[y_root] = x_root
            rank[x_root] += 1

    removed_edges = []
    total_weight = 0
    components = n

    for weight, u, v in edges:
        if find(u) != find(v):
            if components - 1 == k:
                max_diameter = 0
                for i in range(n):
                    distances = [float('inf')] * n
                    distances[i] = 0
                    queue = [i]
                    while queue:
                        node = queue.pop(0)
                        for neighbor, _ in graph[node]:
                            if distances[neighbor] > distances[node] + 1:
                                distances[neighbor] = distances[node] + 1
                                queue.append(neighbor)
                    max_diameter = max(max_diameter, max(distances))
                if max_diameter <= d:
                    break
                removed_edges.append((u, v))
                total_weight += weight
            else:
                union(u, v)
                components -= 1

    return removed_edges, total_weight
n1 = 10   
graph = [[], 
              [(1, 1), (2, 2)],
              [(0, 2), (3, 4)], 
              [(2, 4), (4, 5), (6, 7)], 
              [(3, 5), (5, 6)], 
              [(3, 6), (4, 6), (6, 8)], 
              [(3, 7), (5, 8), (7, 8)], 
              [(6, 8), (8, 9)], 
              [(5, 6), (6, 7), (7, 9)],
              [(7, 9)] 
]
k1 = 3
d1 = 3

edges_to_remove, total_weight = minimum_edges_to_remove(n1, graph1, k1, d1)
print(f"Edges to remove: {edges_to_remove}, Total weight: {total_weight}")

"""


from collections import defaultdict
from heapq import heappush, heappop

def minimum_edges_to_remove(n, graph, k, d):
    edges = []
    for i, neighbors in enumerate(graph):
        for j, w in neighbors:
            if i < j:
             edges.append((w, i, j))
            edges.sort()

    parent = list(range(n))
    rank = [1] * n

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        x_root = find(x)
        y_root = find(y)
        if x_root == y_root:
            return
        if rank[x_root] < rank[y_root]:
            parent[x_root] = y_root
        elif rank[x_root] > rank[y_root]:
            parent[y_root] = x_root
        else:
            parent[y_root] = x_root
            rank[x_root] += 1

    removed_edges = []
    total_weight = 0
    components = n

    for weight, u, v in edges:
        if find(u) != find(v):
            if components - 1 == k:
                max_diameter = 0
                for i in range(n):
                    distances = [float('inf')] * n
                    distances[i] = 0
                    queue = [i]
                    while queue:
                        node = queue.pop(0)
                        for neighbor, _ in graph[node]:
                            if distances[neighbor] > distances[node] + 1:
                                distances[neighbor] = distances[node] + 1
                                queue.append(neighbor)
                    max_diameter = max(max_diameter, max(distances))
                if max_diameter <= d:
                    break
                removed_edges.append((u, v))
                total_weight += weight
            else:
                union(u, v)
                components -= 1

    return removed_edges, total_weight

n = 10
graph = [[], [(1, 1), (2, 2)], [(0, 2), (3, 4)], [(2, 4), (4, 5), (6, 7)], [(3, 5), (5, 6)], [(3, 6), (4, 6), (6, 8)], [(3, 7), (5, 8), (7, 8)], [(6, 8), (8, 9)], [(5, 6), (6, 7), (7, 9)], [(7, 9)]]
k = 3
d = 3

# Execute the function with the given inputs
removed_edges, total_weight = minimum_edges_to_remove(n, graph, k, d)
print(removed_edges, total_weight)




