def count_sequences(n: int) -> int:
    if n == 0:
        return 1
    if n == 1:
        return 2
    if n == 2:
        return 4
    dp = [1, 2, 4]
    for i in range(3, n + 1):
        dp.append(dp[i - 1] + dp[i - 2] + dp[i - 3])
    return dp[n]

if __name__ == "__main__":
    n = int(input())
    print(count_sequences(n))