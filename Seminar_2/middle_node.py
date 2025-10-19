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
    
def middle_node(head: Node | None) -> Node | None:
    if head is None:
        return None
    slow = head
    fast = head
    while fast is not None and fast.get_next() is not None:
        slow = slow.get_next()
        fast = fast.get_next().get_next()
    return slow

if __name__ == '__main__':
    a = None
    assert middle_node(a) is None, "Empty list"
    a = Node(1)
    assert middle_node(a) == a, "One element"
    a = Node(1)
    b = Node(2)
    a.set_next(b)
    assert middle_node(a) == b, "Two elements"
    c = Node(3)
    b.set_next(c)
    assert middle_node(a) == b, "Three elements"
    n = 1000000
    lst = [Node(i) for i in range(n)]
    for i in range(n-1):
        lst[i].set_next(lst[i+1])
    assert middle_node(lst[0]) == lst[n // 2], f"{n} elements"
    print('OK!')