def sort_even(a):
    i, even_i = 0, 0
    for i in range(len(a)):
        if a[i] % 2 == 0:
            a[i], a[even_i] = a[even_i], a[i]
            even_i += 1


# O(n^2) по времени, но сохраняет порядок нечетных элементов
def sort_even_stable(a):
    even_i = 0
    for i in range(len(a)):
        if a[i] % 2 == 0:
            tmp = a[i]
            j = i
            while j > even_i:
                a[j] = a[j - 1]
                j -= 1
            a[even_i] = tmp
            even_i += 1


if __name__ == "__main__":
    a = list(map(int, input().split()))
    b = a[::]
    sort_even(a)
    print(*a)
    sort_even_stable(b)
    print(*b)
