import heapq

def dijkstra(graph, start):
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
    graph = {'A': {'B': 1, 'C': 4}, 'B': {'C': 2, 'D': 5}, 'C': {'D': 1}, 'D': {}}
    dist = dijkstra(graph, 'A')
    assert dist['A'] == 0
    assert dist['B'] == 1
    assert dist['C'] == 3
    assert dist['D'] == 4
    graph = {0: {1: 2}, 1: {}, 2: {}}
    dist = dijkstra(graph, 0)
    assert dist[0] == 0
    assert dist[1] == 2
    assert dist[2] == float('inf')
    graph = {0: {}}
    dist = dijkstra(graph, 0)
    assert dist == {0: 0}
