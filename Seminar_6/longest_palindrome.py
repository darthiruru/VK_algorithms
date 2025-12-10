def longest_palindrome(s: str) -> str:
    n = len(s)
    if n <= 1:
        return s
    dp = [[False] * n for i in range(n)]
    start, max_len = 0, 1
    for i in range(n):
        dp[i][i] = True
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
            start = i
            max_len = 2
    for i in range(3, n + 1):
        for l in range(n - i + 1):
            r = l + i - 1
            if s[l] == s[r] and dp[l + 1][r - 1]:
                dp[l][r] = True
                if i > max_len:
                    start = l
                    max_len = i
    return s[start:start + max_len]

if __name__ == '__main__':
    assert longest_palindrome("babad") in ("bab", "aba")
    assert longest_palindrome("cbbd") == "bb"
    assert longest_palindrome("racecar") == "racecar"
    assert longest_palindrome("ab") in ("a", "b")
    assert longest_palindrome("") == ""