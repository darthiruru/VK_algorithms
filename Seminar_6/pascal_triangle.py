def pascal_triangle(n: int) -> list[int]:
    dp = [[1] * (i + 1) for i in range(n)]
    for row in range(1, n):
        for col in range(1, row):
            dp[row][col] = dp[row - 1][col - 1] + dp[row - 1] [col]
    return dp
4
if __name__ == '__main__':
    n = int(input())
    print(pascal_triangle(n))