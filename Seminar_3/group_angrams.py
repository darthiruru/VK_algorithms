def group_anagrams(strs: list[str]) -> list[list[str]]:
    dict_res = dict()
    for s in strs:
        key = ''.join(sorted(s))
        dict_res.setdefault(key, [])
        dict_res[key].append(s)
    return [value for value in dict_res.values()]



if __name__ == '__main__':
    assert group_anagrams(['eat', 'tea', 'tan', 'ate', 'nat', 'bat']) == [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
    assert group_anagrams(["won","now","aaa","ooo","ooo"]) ==  [["won","now"], ["aaa"], ["ooo", "ooo"]]
    assert group_anagrams([]) == []
    assert group_anagrams(["abc", "def", "ghi"]) == [["abc"], ["def"], ["ghi"]]
    assert group_anagrams(["ab", "ba", "abc", "cab", "c"]) == [["ab", "ba"], ["abc", "cab"], ["c"]]
