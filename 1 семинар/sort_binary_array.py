def sort_binary_array(a):
    start = 0
    end = len(a) - 1
    while start < end:
        if a[start] == 0:
            start += 1
        elif a[end] == 1:
            end -= 1
        else:
            a[start], a[end] = a[end], a[start]
            start += 1
            end -= 1


def sort_binary_array_sum(a):
    sum_ = sum(a)
    for i in range(len(a)):
        if i < len(a) - sum_:
            a[i] = 0
        else:
            a[i] = 1


if __name__ == "__main__":
    a = list(map(int, input().split()))
    b = a[::]
    sort_binary_array(a)
    print(*a)
    sort_binary_array_sum(b)
    print(*b)
