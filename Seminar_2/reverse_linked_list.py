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

def reverse_linked_list(head: Node | None) -> Node | None:
    prev = None
    while head is not None:
        next = head.get_next()
        head.set_next(prev)
        prev = head
        head = next
    return prev

if __name__ == '__main__':
    a = None
    assert reverse_linked_list(a) is None, "Empty list"
    a = Node(1)
    assert reverse_linked_list(a) == a, "One element"
    b = Node(2)
    a.set_next(b)
    head = reverse_linked_list(a)
    assert head == b and head.get_next() == a and a.get_next() is None, "Two elements"
    c = Node(3)
    d = Node(4)
    e = Node(5)
    a.set_next(b)
    b.set_next(c)
    c.set_next(d)
    d.set_next(e)
    head = reverse_linked_list(a)
    assert head == e, "Five elements"
    assert head.get_next() == d and d.get_next() == c and c.get_next() == b and b.get_next() == a and a.get_next() is None, 'Order check'
    n = 1000000
    lst = [Node(i) for i in range(n)]
    for i in range(n-1):
        lst[i].set_next(lst[i+1])
    head = reverse_linked_list(lst[0])
    assert head == lst[-1], f"{n} elements"
    for i in range(n-1, -1 , -1):
        assert head.get_value() == i, f"Order check, {i} elements"
        head = head.get_next()
    assert head is None, "No cycle"
    print('OK!')
