def max_min_multiplication(data: lis[int]) -> int:
    if len(data) < 3:
        return -1
    i = 1
    while 2 * i + 1 < len(data):
        i = 2 * i + 1
    min_index = i
    i = 2
    while 2 * i + 2 < len(data):
        i = 2 * i + 2
    max_index = i
    return data[min_index] * data[max_index]


if __name__ == '__main__':
    a = list(map(int, input().split()))
    print(max_min_multiplication(a))