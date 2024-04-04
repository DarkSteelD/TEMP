def normalize_cycle(cycle):
    cycle = cycle[:-1]
    rotations = [cycle[i:] + cycle[:i] for i in range(len(cycle))]
    inv_cycle = cycle[::-1]
    rotations += [inv_cycle[i:] + inv_cycle[:i] for i in range(len(cycle))]
    min_rotation = min(rotations)
    return tuple(min_rotation) + (min_rotation[0],)

def preprocess_graph(graph):
    modified = True
    while modified:
        modified = False
        for node in list(graph.keys()):
            if len(graph[node]) < 2:
                del graph[node]
                for neighbors in graph.values():
                    if node in neighbors:
                        neighbors.remove(node)
                modified = True
    return graph

def find_max_degree_node(graph):
    max_degree = 0
    max_node = None
    for node, neighbors in graph.items():
        if len(neighbors) > max_degree:
            max_degree = len(neighbors)
            max_node = node
    return max_node

def dfs(graph, start, current, path, visited, cycles, visited_starts):
    if len(path) == 4:
        if start in graph.get(current, []):  
            cycle = tuple(path + [start])
            normalized_cycle = normalize_cycle(cycle)
            cycles.add(normalized_cycle)
            for node in normalized_cycle[:-2]:
                visited_starts.add(node)
        return
    for next_node in graph.get(current, []):
        if next_node not in visited:
            visited.add(next_node)
            dfs(graph, start, next_node, path + [next_node], visited, cycles, visited_starts)
            visited.remove(next_node)

def find_all_cycles_of_length_4(graph):
    cycles = set()
    visited_starts = set()
    graph = preprocess_graph(graph)
    while graph:
        start_node = find_max_degree_node(graph)
        if start_node is None:
            break
        dfs(graph, start_node, start_node, [start_node], {start_node}, cycles, visited_starts)
        del graph[start_node]
    return cycles

N, M = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(M)]

graph = {i: [] for i in range(1, N+1)}
for u, v in edges:
    graph[u].append(v)
    graph[v].append(u)

cycles = find_all_cycles_of_length_4(graph)

for cycle in cycles:
    print(cycle)
print(len(cycles))
