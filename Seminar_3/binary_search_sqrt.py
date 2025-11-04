def binary_search_sqrt(target: int) -> int:
    l = 0
    r = target
    while l <= r:
        middle = (l + r) // 2
        square = middle ** 2 
        if square > target:
            r = middle - 1
        elif square < target:
            l = middle + 1
        else:
            return middle
    return r

if __name__ == '__main__':
    assert binary_search_sqrt(0) == 0
    assert binary_search_sqrt(1) == 1
    assert binary_search_sqrt(9) == 3
    assert binary_search_sqrt(15) == 3
    assert binary_search_sqrt(10**50) == 10**25
    assert binary_search_sqrt(10**1000) == 10**500