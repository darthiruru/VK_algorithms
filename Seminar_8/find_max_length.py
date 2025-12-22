def find_max_length(nums: list[int]) -> int:
    prefix_sum = 0
    max_len = 0
    index_map = {0: -1}
    for i in range(len(nums)):
        num = nums[i]
        prefix_sum += -1 if num == 0 else 1
        if prefix_sum in index_map:
            max_len = max(max_len, i - index_map[prefix_sum])
        else:
            index_map[prefix_sum] = i
    return max_len

if __name__ == '__main__':
    assert find_max_length([0, 1]) == 2
    assert find_max_length([0, 1, 0]) == 2
    assert find_max_length([0, 1, 0, 1]) == 4
    assert find_max_length([0, 0, 1, 0, 0, 0, 1, 1]) == 6
    assert find_max_length([0, 0, 0]) == 0
    assert find_max_length([1, 1, 1]) == 0
    assert find_max_length([]) == 0
    assert find_max_length([1, 0, 1, 1, 1, 0, 0]) == 6