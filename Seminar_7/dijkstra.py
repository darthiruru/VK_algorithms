import heapq

def dijkstra(graph: dict[int: list[int]], start: int) -> dict[int: int]:
    distances = {v: float('inf') for v in graph}
    distances[start] = 0
    priority_queue = [(0, start)]
    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)
        if current_distance > distances[current_vertex]:
            continue
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    return distances


if __name__ == '__main__':
    graph = {0: {1: 1, 2: 4}, 1: {2: 2, 3: 5}, 2: {3: 1}, 3: {}}
    dist = dijkstra(graph, 0)
    assert dist[0] == 0
    assert dist[1] == 1
    assert dist[2] == 3
    assert dist[3] == 4
    graph = {0: {1: 2}, 1: {}, 2: {}}
    dist = dijkstra(graph, 0)
    assert dist[0] == 0
    assert dist[1] == 2
    assert dist[2] == float('inf')
    graph = {0: {}}
    dist = dijkstra(graph, 0)
    assert dist == {0: 0}
