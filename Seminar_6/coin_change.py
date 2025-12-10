def coin_change(coins: list[int], amount: int) -> int:
    dp = []
    for i in range(amount + 1):
        dp.append(float('inf'))
    dp[0] = 0
    for i in range(amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    if dp[amount] == float('inf'):
        return -1
    return dp[amount]

if __name__ == '__main__':
    assert coin_change([1, 2, 5], 11) == 3
    assert coin_change([1, 2, 3], 0) == 0
    assert coin_change([2], 3) == -1
    assert coin_change([7], 14) == 2
    assert coin_change([2, 3, 5], 10) == 2
    assert coin_change([1, 3, 4], 6) == 2
    assert coin_change([5, 10, 25], 30) == 2
    assert coin_change([5, 1, 3], 7) == 3
    assert coin_change([4, 5], 3) == -1
    assert coin_change([2, 5, 10, 1], 27) == 4