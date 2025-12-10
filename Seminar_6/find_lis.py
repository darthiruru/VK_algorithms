def find_lis(nums: list[int]) -> int:
    if len(nums) == 0:
        return 0
    if len(nums) == 1:
        return 1
    dp = [1] * len(nums)
    for i in range(1, len(nums)):
        if nums[i - 1] < nums[i]:
            dp[i] = dp[i - 1] + 1
    return max(dp)

if __name__ == '__main__':
    assert find_lis([]) == 0
    assert find_lis([5]) == 1
    assert find_lis([1, 2, 3, 4]) == 4
    assert find_lis([5, 4, 3, 2, 1]) == 1
    assert find_lis([3, 2, 8, 9, 5, 10]) == 3
    assert find_lis([1, 2, 7, 9, 0, 10]) == 4
    assert find_lis([8, 8, 8, 8]) == 1