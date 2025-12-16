def has_cycle(graph: dict[int: list[int]]) -> bool:
    visited = set()
    for v in graph:
        if v not in visited:
            if dfs(graph, v, None, visited):
                return True
    return False

def dfs(graph: dict[int: list[int]], v: int, parent: int, visited: set[int]) -> bool:
    visited.add(v)
    for i in graph[v]:
        if i not in visited:
            if dfs(graph, i, v, visited):
                return True
        elif i != parent:
            return True
    return False


if __name__ == '__main__':
    graph = {0: [1], 1: [0, 2], 2: [1]}
    assert has_cycle(graph) is False
    graph = {0: [1, 2], 1: [0, 2], 2: [0, 1]}
    assert has_cycle(graph) is True
    graph = {0: [1], 1: [0], 2: [3, 4], 3: [2, 4], 4: [2, 3]}
    assert has_cycle(graph) is True
    graph = {0: [1], 1: [0], 2: [], 3: []}
    assert has_cycle(graph) is False
    graph = {0: []}
    assert has_cycle(graph) is False
