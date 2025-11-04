def two_sum(data: list[int], target: int) -> list[int]:
    cache = set()
    for elem in data:
        if (target - elem) in cache:
            return [target - elem, elem]
        cache.add(elem) 
    return []


if __name__ == '__main__':
    assert two_sum([2, 7, 11, 15], 9) == [2, 7]
    assert two_sum([1, 2, 3], 10) == [] 
    assert two_sum([], 5) == []
    assert two_sum([1, 1, 1], 2) == [1, 1]
    assert two_sum([1, 2, 3, 4, 5], 6) == [2, 4]