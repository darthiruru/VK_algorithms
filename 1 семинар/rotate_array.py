def reverseArray(a, start, end):
    left, right = start, end
    while left < right:
        a[left], a[right] = a[right], a[left]
        left += 1
        right -= 1


def rotateArray(a, k):
    if not a:
        return
    k %= len(a)
    reverseArray(a, 0, len(a) - 1)
    reverseArray(a, 0, k - 1)
    reverseArray(a, k, len(a) - 1)


if __name__ == "__main__":
    a = list(map(int, input().split()))
    k = int(input())
    rotateArray(a, k)
    print(*a)
