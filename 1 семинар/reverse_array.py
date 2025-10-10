def reverseArray(a):
    res = a[::]
    left, right = 0, len(a) - 1
    while left < right:
        res[left], res[right] = res[right], res[left]
        left += 1
        right -= 1
    return res


if __name__ == "__main__":
    a = list(map(int, input().split()))
    print(*reverseArray(a))
