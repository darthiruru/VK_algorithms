def subarray_sum(nums: list[int], k: int) -> int:
    prefix_sum = 0
    prefix_count = {0 : 1}
    count = 0
    for num in nums:
        prefix_sum += num
        count += prefix_count.get(prefix_sum - k, 0)
        prefix_count[prefix_sum] = prefix_count.get(prefix_sum, 0) + 1
    return count

if __name__ == '__main__':
    assert subarray_sum([1, 1, 1], 2) == 2
    assert subarray_sum([1, -1, 1], 1) == 3
    assert subarray_sum([0, 0, 0], 0) == 6
    assert subarray_sum([5], 5) == 1
    assert subarray_sum([], 0) == 0
    assert subarray_sum([1, 2, 3], 7) == 0
    assert subarray_sum([-1, -1, 1], -1) == 3