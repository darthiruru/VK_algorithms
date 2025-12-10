def max_profit(prices: list[int]) -> int:
    profit = 0
    min_price = prices[0]
    for i in range(1, len(prices)):
        profit = max(profit, prices[i] - min_price)
        min_price = min(prices[i], min_price)
    return profit

if __name__ == '__main__':
    assert max_profit([8, 9, 3, 7, 4, 16, 12]) == 13
    assert max_profit([1, 2, 3, 4, 5, 6]) == 5
    assert max_profit([10, 9, 8, 7, 6]) == 0
    assert max_profit([7, 1, 5, 3, 6, 4]) == 5
    assert max_profit([3, 2, 6]) == 4
    assert max_profit([4, 4, 4, 4]) == 0
    assert max_profit([9, 7, 2, 1, 6, 20]) == 19