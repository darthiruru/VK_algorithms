def reverse_array(a, start, end):
    left, right = start, end
    while left < right:
        a[left], a[right] = a[right], a[left]
        left += 1
        right -= 1


def rotate_array(a, k):
    if not a:
        return
    k %= len(a)
    reverse_array(a, 0, len(a) - 1)
    reverse_array(a, 0, k - 1)
    reverse_array(a, k, len(a) - 1)


if __name__ == "__main__":
    a = list(map(int, input().split()))
    k = int(input())
    rotate_array(a, k)
    print(*a)
