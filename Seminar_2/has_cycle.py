class Node:
    def __init__(self, value):
        self.next__ = None
        self.value__ = value

    def set_value(self, value):
        self.value__ = value

    def get_value(self):
        return self.value__
    
    def set_next(self, next):
        self.next__ = next

    def get_next(self):
        return self.next__

def has_cycle(head):
    if head is None or head.get_next() is None:
        return False
    slow = head
    fast = head.get_next()
    while slow != fast:
        if fast is None or fast.get_next() is None:
            return False
        slow = slow.get_next()
        fast = fast.get_next().get_next()
    return True

if __name__ == '__main__':
    a = None
    assert has_cycle(a) == False, 'Empty list'
    a = Node(1)
    assert has_cycle(a) == False, 'One element, cycle found'
    a.set_next(a)
    assert has_cycle(a) == True, 'One element, cycle not found'
    b = Node(2)
    a.set_next(b)
    assert has_cycle(a) == False, 'Two elements, cycle found'
    b.set_next(a)
    assert has_cycle(a) == True, 'Two elements, cycle not found'
    c = Node(3)
    b.set_next(c)
    assert has_cycle(a) == False, 'Cycle found'
    d = Node(4)
    c.set_next(d)
    d.set_next(b)
    assert has_cycle(a) == True, 'Cycle not found'
    e = Node(5)
    d.set_next(e)
    e.set_next(c)
    assert has_cycle(a) == True, 'Cycle not found'
    print('OK!')
