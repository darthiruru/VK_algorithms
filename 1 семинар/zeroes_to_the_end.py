def sort_zeroes(a):
    i, non_zero_i = 0, 0
    for i in range(len(a)):
        if a[i] != 0:
            a[i], a[non_zero_i] = a[non_zero_i], a[i]
            non_zero_i += 1


if __name__ == "__main__":
    a = list(map(int, input().split()))
    sort_zeroes(a)
    print(*a)
