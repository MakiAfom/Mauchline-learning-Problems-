def build_graph(edges):
    graph = {}
    for edge in edges:
        a, b = edge
        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []
        graph[a].append(b)
        graph[b].append(a)
    return graph
def dfs(node, path_length, visited, k, graph):
    if path_length == k:
        return 1
    
    count = 0
    for neighbor in graph[node]:
        if neighbor not in visited:
            visited.add(neighbor)
            count += dfs(neighbor, path_length + 1, visited, k, graph)
            visited.remove(neighbor)
    return count


def max_disjoint_paths(edges, k):
    graph = build_graph(edges)
    total_paths = 0
    used_nodes = set()
    
    for start_node in graph:
        if start_node not in used_nodes:
            visited = set([start_node])
            paths = dfs(start_node, 1, visited, k, graph)
            if paths > 0:
                total_paths += paths
                used_nodes.update(visited)
    
    return total_paths

# Test the example
edges = [[1, 2], [2, 3], [3, 4], [4, 1], [1, 5]]
k = 3
print(max_disjoint_paths(edges, k))  
