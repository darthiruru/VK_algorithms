def shell_sort(arr: list[int]) -> list[int]:
    arr = arr.copy()
    gaps = [1]
    while (gaps[-1] + 1) * 2 < len(arr):
        gaps.append((gaps[-1] + 1) * 2 - 1)
    for gap in reversed(gaps):
        for pos in range(gap, len(arr)):
            m_gap = pos
            while m_gap >= gap and arr[m_gap] < arr[m_gap - gap]:
                arr[m_gap], arr[m_gap - gap] = arr[m_gap - gap], arr[m_gap]
                m_gap -= gap
    return arr


if __name__ == '__main__':
    assert shell_sort([]) == []
    assert shell_sort([5]) == [5]
    assert shell_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert shell_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
    assert shell_sort([3, 3, 2, 1, 2]) == [1, 2, 2, 3, 3]
    n = 10 ** 6
    assert shell_sort(list(range(n - 1, -1, -1))) == list(range(n))
