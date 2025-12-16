def find_connected_components(graph: dict[int: list[int]]) -> list[list[int]]:
    visited = [False] * len(graph)
    connected_components = []
    for v in graph:
        if not visited[v]:
            component = []
            dfs(graph, v, visited, component)
            connected_components.append(component)
    return connected_components

def dfs(graph: dict[int: list[int]], v: int, visited: list[bool], component: list[int]) -> None:
    visited[v] = True
    component.append(v)
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited, component)

def dfs_color(graph: dict[int: list[int]], v: int, visited: list[int], color: int) -> None:
    visited[v] = color
    for i in graph[v]:
        if not visited[i]:
            dfs_color(graph, i, visited, color)

def find_connected_components_color(graph: dict[int: list[int]]) -> list[int]:
    visited = [0] * len(graph)
    color = 0
    for v in graph:
        if visited[v] == 0:
            color += 1
            dfs_color(graph, v, visited, color)
    return visited


if __name__ == '__main__':
    graph = {0: [1, 2], 1: [0, 2], 2: [0, 1]}
    cc = find_connected_components(graph)
    assert len(cc) == 1
    assert set(cc[0]) == {0, 1, 2}
    colors = find_connected_components_color(graph)
    assert len(set(colors)) == 1
    assert colors[0] == colors[1] == colors[2]
    graph = {0: [1], 1: [0], 2: [3], 3: [2]}
    cc = find_connected_components(graph)
    assert len(cc) == 2
    assert {frozenset(c) for c in cc} == {frozenset({0, 1}),frozenset({2, 3})}
    colors = find_connected_components_color(graph)
    assert len(set(colors)) == 2
    assert colors[0] == colors[1]
    assert colors[2] == colors[3]
    assert colors[0] != colors[2]
    graph = {0: [], 1: [], 2: []}
    cc = find_connected_components(graph)
    assert len(cc) == 3
    assert {frozenset(c) for c in cc} == {frozenset({0}), frozenset({1}), frozenset({2})}
    colors = find_connected_components_color(graph)
    assert len(set(colors)) == 3
    assert colors[0] != colors[1]
    assert colors[1] != colors[2]
    assert colors[0] != colors[2]
    graph = {0: [1], 1: [0], 2: [],}
    cc = find_connected_components(graph)
    assert len(cc) == 2
    assert {frozenset(c) for c in cc} == {frozenset({0, 1}), frozenset({2})}
    colors = find_connected_components_color(graph)
    assert len(set(colors)) == 2
    assert colors[0] == colors[1]
    assert colors[2] != colors[0]
