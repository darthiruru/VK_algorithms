def merge_sorted_arrays(a, b):
    res = []
    i, j = 0, 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            res.append(a[i])
            i += 1
        else:
            res.append(b[j])
            j += 1
    res.extend(a[i:])
    res.extend(b[j:])
    return res


def iter_merge_sorted_arrays(a, b):
    i, j = 0, 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            yield a[i]
            i += 1
        else:
            yield b[j]
            j += 1
    yield from a[i:]
    yield from b[j:]


if __name__ == "__main__":
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(*merge_sorted_arrays(a, b))
    print(*iter_merge_sorted_arrays(a, b))
