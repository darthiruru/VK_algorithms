def extra_letter(a: str, b: str) -> str:
    dict_b = dict()
    for letter in b:
        dict_b[letter] = dict_b.get(letter, 0) + 1
    for letter in a:
        dict_b[letter] -= 1
    for letter, count in dict_b.items():
        if count > 0:
            return letter
    return ''


if __name__ == '__main__':
    assert extra_letter('uio', 'oeiu') == 'e'
    assert extra_letter('fe', 'efo') == 'o'
    assert extra_letter('ab', 'ab') == ''
    assert extra_letter('bbb', 'bbbb') == 'b'
