import heapq

def merge_k_sorted_arrays(sorted_arrays: list[list[int]]) -> list[int]:
    merged_array = []
    min_heap = []
    for array_idx, arr in enumerate(sorted_arrays):
        if len(arr) > 0:
            heapq.heappush(min_heap, (arr[0], array_idx, 0))
    while min_heap:
        value, array_idx, element_idx = heapq.heappop(min_heap)
        merged_array.append(value)
        if element_idx + 1 < len(sorted_arrays[array_idx]):
            next_val = sorted_arrays[array_idx][element_idx + 1]
            heapq.heappush(min_heap, (next_val, array_idx, element_idx + 1))
    return merged_array


if __name__ == "__main__":
    assert merge_k_sorted_arrays([]) == []
    assert merge_k_sorted_arrays([[]]) == []
    assert merge_k_sorted_arrays([[1, 2, 3]]) == [1, 2, 3]
    assert merge_k_sorted_arrays([[1, 4, 7], [2, 5, 8]]) == [1, 2, 4, 5, 7, 8]
    arrays = [[1, 3, 5, 7], [2, 4], [0, 6, 8, 9, 10]]
    assert merge_k_sorted_arrays(arrays) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert merge_k_sorted_arrays([[3], [1], [2]]) == [1, 2, 3]
    arrays = [[1, 2, 2], [2, 2, 3], [0, 2, 2]]
    assert merge_k_sorted_arrays(arrays) == [0, 1, 2, 2, 2, 2, 2, 2, 3]
    arrays = [list(range(0, 10 ** 6, 2)), list(range(1, 10 ** 6, 2))]
    assert merge_k_sorted_arrays(arrays) == list(range(10 ** 6))
