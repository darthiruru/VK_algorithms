def reverseArray(a):
    res = a[::]
    left, right = 0, len(a) - 1
    while left < right:
        res[left], res[right] = res[right], res[left]
        left += 1
        right -= 1
    return res


def rotateArray(a, k):
    k = k % len(a)
    res = reverseArray(a)
    res[:k] = reverseArray(res[:k])
    res[k:] = reverseArray(res[k:])
    return res


if __name__ == "__main__":
    a = list(map(int, input().split()))
    k = int(input())
    print(*rotateArray(a, k))
