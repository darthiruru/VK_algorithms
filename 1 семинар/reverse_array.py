def reverse_array(a):
    left, right = 0, len(a) - 1
    while left < right:
        a[left], a[right] = a[right], a[left]
        left += 1
        right -= 1


if __name__ == "__main__":
    a = list(map(int, input().split()))
    reverse_array(a)
    print(*a)
