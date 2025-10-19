def sort_array(a):
    low, mid = 0, 0
    high = len(a) - 1
    while mid <= high:
        if a[mid] == 2:
            a[mid], a[high] = a[high], a[mid]
            high -= 1
        elif a[mid] == 0:
            a[mid], a[low] = a[low], a[mid]
            low += 1
            mid += 1
        else:
            mid += 1


if __name__ == "__main__":
    a = list(map(int, input().split()))
    sort_array(a)
    print(*a)
