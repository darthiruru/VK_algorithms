def is_bipartite_bfs(graph: dict[int: list[int]]) -> bool:
    colors = [0] * len(graph)
    def bfs(start: int) -> bool:
        queue = [start]
        colors[start] = 1
        while len(queue) > 0:
            node = queue.pop(0)
            for neighbor in graph[node]:
                if colors[neighbor] == 0:
                    colors[neighbor] = -colors[node]
                    queue.append(neighbor)
                elif colors[neighbor] == colors[node]:
                    return False
        return True
    for v in graph:
        if colors[v] == 0:
            if not bfs(v):
                return False
    return True

def is_bipartite_dfs(graph: dict[int: list[int]]) -> bool:
    colors = [0] * len(graph)
    def dfs(node: int, c: int) -> bool:
        colors[node] = c
        for neighbor in graph[node]:
            if colors[neighbor] == 0:
                if not dfs(neighbor, -c):
                    return False
            elif colors[neighbor] == colors[node]:
                return False
        return True
    for v in graph:
        if colors[v] == 0:
            if not dfs(v, 1):
                return False
    return True


if __name__ == '__main__':
    graph = {0: [1], 1: [0, 2], 2: [1]}
    assert is_bipartite_bfs(graph) is True
    assert is_bipartite_dfs(graph) is True
    graph = {0: [1, 3], 1: [0, 2], 2: [1, 3], 3: [0, 2]}
    assert is_bipartite_bfs(graph) is True
    assert is_bipartite_dfs(graph) is True
    graph = {0: [1, 2], 1: [0, 2], 2: [0, 1]}
    assert is_bipartite_bfs(graph) is False
    assert is_bipartite_dfs(graph) is False
    graph = {0: [1], 1: [0], 2: [], 3: []}
    assert is_bipartite_bfs(graph) is True
    assert is_bipartite_dfs(graph) is True
    graph = {0: [0]}
    assert is_bipartite_bfs(graph) is False
    assert is_bipartite_dfs(graph) is False