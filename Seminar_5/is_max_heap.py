from collections import deque

def is_max_heap(arr: list[int]) -> bool:
    n = len(arr)
    for i in range((n - 2) // 2 + 1):
        left = 2 * i + 1
        right = 2 * i + 2
        if left < n and arr[i] < arr[left]:
            return False
        if right < n and arr[i] < arr[right]:
            return False
    return True

def is_max_heap_bfs(arr: list[int]) -> bool:
    n = len(arr)
    if n <= 1:
        return True
    queue = deque()
    queue.append(0)
    while (len(queue) > 0):
        i = queue.popleft()
        left = 2 * i + 1
        right = 2 * i + 2
        if left < n:
            if arr[i] < arr[left]:
                return False
            queue.append(left)
        if right < n:
            if arr[i] < arr[right]:
                return False
            queue.append(right)
    return True


if __name__ == '__main__':
    assert is_max_heap([]) is True
    assert is_max_heap_bfs([]) is True
    assert is_max_heap([42]) is True
    assert is_max_heap_bfs([42]) is True
    assert is_max_heap([10, 9, 8, 7, 6, 5, 4]) is True
    assert is_max_heap_bfs([10, 9, 8, 7, 6, 5, 4]) is True
    assert is_max_heap([5, 5, 5, 5, 5]) is True
    assert is_max_heap_bfs([5, 5, 5, 5, 5]) is True
    assert is_max_heap([20, 15, 18, 10, 12]) is True
    assert is_max_heap_bfs([20, 15, 18, 10, 12]) is True
    assert is_max_heap([10, 20, 5]) is False
    assert is_max_heap_bfs([10, 20, 5]) is False
    assert is_max_heap([10, 5, 30]) is False 
    assert is_max_heap_bfs([10, 5, 30]) is False 
    assert is_max_heap([40, 30, 20, 10, 50]) is False
    assert is_max_heap_bfs([40, 30, 20, 10, 50]) is False
