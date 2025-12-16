def is_tree(graph: dict[int: list[int]], start: int) -> bool:
    visited = {start}
    queue = [start]
    parent = {start: None}
    while queue:
        v = queue.pop(0)
        for i in graph[v]:
            if i not in visited:
                visited.add(i)
                queue.append(i)
                parent[i] = v
            else:
                if parent[v] != i:
                    return False
    return len(visited) == len(graph)


if __name__ == '__main__':
    graph = {0: [1], 1: [0, 2], 2: [1]}
    assert is_tree(graph, 0) is True
    graph = {0: [1, 2], 1: [0, 2], 2: [0, 1]}
    assert is_tree(graph, 0) is False
    graph = {0: [1], 1: [0], 2: []}
    assert is_tree(graph, 0) is False
    graph = {0: []}
    assert is_tree(graph, 0) is True
    graph = {0: [1, 2, 3], 1: [0], 2: [0], 3: [0]}
    assert is_tree(graph, 0) is True