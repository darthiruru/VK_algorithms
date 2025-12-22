def can_make_valid_with_deletions(s: str, k: int) -> bool:
    balance = 0
    extra_closed_balance = 0
    for ch in s:
        balance += 1 if ch == '(' else -1
        if balance < 0:
            extra_closed_balance += 1
            balance = 0
    total_needed = balance + extra_closed_balance
    return total_needed <= k

if __name__ == '__main__':
    assert can_make_valid_with_deletions("()", 0) is True
    assert can_make_valid_with_deletions("(())", 0) is True
    assert can_make_valid_with_deletions("(()", 1) is True
    assert can_make_valid_with_deletions("())", 1) is True
    assert can_make_valid_with_deletions("())(", 2) is True
    assert can_make_valid_with_deletions("(()", 0) is False
    assert can_make_valid_with_deletions("())", 0) is False
    assert can_make_valid_with_deletions("", 0) is True
    assert can_make_valid_with_deletions("((((", 4) is True
    assert can_make_valid_with_deletions("))))", 3) is False