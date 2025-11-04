import math

def copy_time(n: int, x: int, y: int) -> int:
    l, r = 0, max(x, y) * (n - 1)
    while l + 1 < r:
        middle = (l + r) // 2
        if middle // x + middle // y < n - 1:
            l = middle
        else:
            r = middle
    return r + min(x, y)

def copy_time_gcd(n: int, x: int, y: int) -> int:
    lcm = x * y // math.gcd(x, y)
    per_cycle = lcm // x + lcm // y
    full_cycles = (n - 1) // per_cycle
    left = (n - 1) - full_cycles * per_cycle
    if left == 0:
        return min(x, y) + full_cycles * lcm
    if full_cycles == 0:
        return copy_time(n, x, y)
    return full_cycles * lcm + copy_time(left + 1, x, y)



if __name__ == '__main__':
    assert copy_time(1, 1, 2) == 1
    assert copy_time(2, 1, 2) == 2
    assert copy_time(5, 1, 2) == 4
    assert copy_time(5, 2, 2) == 6
    assert copy_time(5, 1, 100) == 5
    assert copy_time(10**6 - 1, 3, 5) == 1875000

    assert copy_time_gcd(1, 1, 2) == 1
    assert copy_time_gcd(2, 1, 2) == 2
    assert copy_time_gcd(5, 1, 2) == 4
    assert copy_time_gcd(5, 2, 2) == 6
    assert copy_time_gcd(5, 1, 100) == 5
    assert copy_time_gcd(10**6 - 1, 3, 5) == 1875000