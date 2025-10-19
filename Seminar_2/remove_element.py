import random

class Node:
    def __init__(self, value: int) -> None:
        self.next__ = None
        self.value__ = value

    def set_value(self, value: int) -> None:
        self.value__ = value

    def get_value(self) -> int:
        return self.value__
    
    def set_next(self, next: Node | None) -> None:
        self.next__ = next

    def get_next(self) -> Node | None:
        return self.next__
    
def remove_element(head: Node | None, val: int) -> Node | None:
    dummy = Node(0)
    dummy.set_next(head)
    prev = dummy
    while head is not None:
        if head.get_value() == val:
            prev.set_next(head.get_next())
        else:
            prev = head
        head = head.get_next()
    return dummy.get_next()


if __name__ == '__main__':
    a = None
    assert remove_element(a, 0) is None, 'Empty list'
    a = Node(1)
    assert remove_element(a, 1) is None, "Single element removed"
    a = Node(1)
    b = Node(2)
    a.set_next(b)
    res = remove_element(a, 2)
    assert res == a and res.get_next() is None, "Two elements, removed last"
    a = Node(1)
    b = Node(2)
    c = Node(3)
    a.set_next(b)
    b.set_next(c)
    res = remove_element(a, 2)
    assert res == a and res.get_next() == c, "Three elements, removed middle"
    a = Node(1)
    b = Node(2)
    c = Node(3)
    a.set_next(b)
    b.set_next(c)
    res = remove_element(a, 4)
    assert res == a and res.get_next() == b and res.get_next().get_next() == c, "Three elements, value not in list"
    n = 1000000
    lst = [Node(i) for i in range(n)]
    for i in range(n-1):
        lst[i].set_next(lst[i+1])
    val = random.randint(0, n-1)
    res = remove_element(lst[0], val)
    assert res == lst[0], f'{n} elements, removed value {val}'
    l = 0
    while res is not None:
        if l == val:
            l += 1
            continue
        assert res.get_value() == l, f'Check value {val}'
        l += 1
        res = res.get_next()
    assert l == n, 'Length mismatch'
    print('OK!')