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
    
def merge_sorted_lists(l1: Node | None, l2: Node | None) -> Node | None:
    if l1 is None:
        return l2
    if l2 is None:
        return l1
    if l1.get_value() < l2.get_value():
        head, prev = l1, l1
        l1 = l1.get_next()
    else:
        head, prev = l2, l2
        l2 = l2.get_next()
    while l1 is not None and l2 is not None:
        if l1.get_value() < l2.get_value():
            prev.set_next(l1)
            prev = l1
            l1 = l1.get_next()
        else:
            prev.set_next(l2)
            prev = l2
            l2 = l2.get_next()
    prev.set_next(l1 if l1 is not None else l2)   
    return head

def create_linked_list(lst: list[int]) -> Node:
    head = Node(lst[0])
    current = head
    for value in lst[1:]:
        new_node = Node(value)
        current.set_next(new_node)
        current = new_node
    return head

def create_list(head: Node) -> list[int]:
    res = []
    while head is not None:
        res.append(head.get_value())
        head = head.get_next()
    return res

if __name__ == '__main__':
    assert merge_sorted_lists(None, None) is None, "Empty lists"
    l1 = None
    l2 = create_linked_list([1, 2, 3])
    assert create_list(merge_sorted_lists(l1, l2)) == [1, 2, 3], "Left empty"
    l1 = create_linked_list([1, 2, 3])
    l2 = None
    assert create_list(merge_sorted_lists(l1, l2)) == [1, 2, 3], "Right empty"
    l1 = create_linked_list([1])
    l2 = create_linked_list([2])
    assert create_list(merge_sorted_lists(l1, l2)) == [1, 2], "Single elements"
    l1 = create_linked_list([1, 3, 5])
    l2 = create_linked_list([2, 4])
    assert create_list(merge_sorted_lists(l1, l2)) == [1, 2, 3, 4, 5], "Different lengths"
    l1 = create_linked_list([1, 2, 2, 3])
    l2 = create_linked_list([2, 2, 4])
    assert create_list(merge_sorted_lists(l1, l2)) == [1, 2, 2, 2, 2, 3, 4], "The same elements"
    n = 1000000
    l1 = create_linked_list(list(range(0, n * 2, 2)))
    l2 = create_linked_list(list(range(1, n * 2, 2)))
    res = merge_sorted_lists(l1, l2)
    assert create_list(res) == list(range(n * 2)), "Large merge test"


