def max_subarray_sum(arr: list[int], k: int) -> int | None:
    if len(arr) < k or k <= 0:
        return None
    current_sum = sum(arr[:k])
    max_sum = current_sum
    for i in range(k, len(arr)):
        current_sum = current_sum - arr[i-k] + arr[i]
        max_sum = max(max_sum, current_sum)
    return max_sum

if __name__ == '__main__':
    assert max_subarray_sum([1, 2, 3, 4, 5], 2) == 9
    assert max_subarray_sum([-1, -2, -3, -4], 2) == -3
    assert max_subarray_sum([1, 2, 3], 3) == 6
    assert max_subarray_sum([1, 2], 3) is None
    assert max_subarray_sum([4, -1, 2, 1], 1) == 4
    assert max_subarray_sum([1, 2, 3], 0) is None
    assert max_subarray_sum([1, 2, 3], -1) is None