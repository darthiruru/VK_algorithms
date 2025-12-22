def pivot_index(nums: list[int]) -> int:
    total_sum = sum(nums)
    left_sum = 0
    for i in range(len(nums)):
        if left_sum == total_sum - left_sum - nums[i]:
            return i
        left_sum += nums[i]
    return -1

if __name__ == '__main__':
    assert pivot_index([1, 7, 3, 6, 5, 6]) == 3
    assert pivot_index([1, 2, 3]) == -1
    assert pivot_index([2, 1, -1]) == 0
    assert pivot_index([5]) == 0
    assert pivot_index([]) == -1
    assert pivot_index([-1, -1, -1, 0, 1, 1]) == 0
    assert pivot_index([0, 0, 0, 0]) == 0