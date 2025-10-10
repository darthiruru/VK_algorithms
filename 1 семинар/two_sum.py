def twosum(a, target):
    i, j = 0, len(a) - 1
    while i < j:
        if a[i] + a[j] > target:
            i += 1
        elif a[i] + a[j] < target:
            j -= 1
        else:
            return a[i], a[j]
    return 'Таких чисел нет в массиве'

if __name__ == '__main__':
    a = list(map(int, input().split()))
    target = int(input())
    print(twosum(a, target))

