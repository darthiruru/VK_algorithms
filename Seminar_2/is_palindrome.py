class Stack:
    def __init__(self) -> None:
        self.arr__ = []

    def push(self, value: str) -> None:
        self.arr__.append(value)

    def pop(self) -> str | None:
        if len(self.arr__) == 0:
            return None
        return self.arr__.pop()
    
class Node:
    def __init__(self, value: str) -> None:
        self.next__ = None
        self.prev__ = None
        self.value__ = value

    def set_value(self, value: str) -> None:
        self.value__ = value

    def get_value(self) -> str:
        return self.value__
    
    def set_next(self, next: Node | None) -> None:
        self.next__ = next

    def get_next(self) -> Node | None:
        return self.next__
    
    def set_prev(self, prev: Node | None) -> None:
        self.prev__ = prev

    def get_prev(self) -> Node | None:
        return self.prev__

class Deque:
    def __init__(self) -> None:
        self.head__ = None
        self.tail__ = None
        self.size__ = 0

    def push_front(self, value: str) -> None:
        new_node = Node(value)
        if self.size__ == 0:
            self.head__ = new_node
            self.tail__ = new_node
        else:
            self.head__.set_prev(new_node)
            new_node.set_next(self.head__)
            self.head__ = new_node
        self.size__ += 1

    def push_back(self, value: str) -> None:
        new_node = Node(value)
        if self.size__ == 0:
            self.head__ = new_node
            self.tail__ = new_node
        else:
            self.tail__.set_next(new_node)
            new_node.set_prev(self.tail__)
            self.tail__ = new_node
        self.size__ += 1

    def pop_front(self) -> str | None:
        if self.size__ == 0:
            return None
        value = self.head__.get_value()
        if self.head__.get_next() is None:
            self.head__ = None
            self.tail__ = None
        else:
            self.head__.get_next().set_prev(None)
            self.head__ = self.head__.get_next()
        self.size__ -= 1
        return value

    def pop_back(self) -> str | None:
        if self.size__ == 0:
            return None
        value = self.tail__.get_value()
        if self.tail__.get_prev() is None:
            self.head__ = None
            self.tail__ = None
        else:
            self.tail__.get_prev().set_next(None)
            self.tail__ = self.tail__.get_prev()
        self.size__ -= 1
        return value

    def peek_front(self) -> str | None:
        if self.size__ == 0:
            return None
        return self.head__.get_value()

    def peek_back(self) -> str | None:
        if self.size__ == 0:
            return None
        return self.tail__.get_value()
    
    def get_size(self) -> int:
        return self.size__

def is_palindrome_stack(s: str) -> bool:
    stack = Stack()
    for char in s:
        stack.push(char)
    for char in s:
        if char != stack.pop():
            return False
    return True

def is_palindrome_deque(s: str) -> bool:
    deque = Deque()
    for char in s:
        deque.push_back(char)
    while deque.get_size() > 1:
        if deque.peek_front() != deque.peek_back():
            return False
        deque.pop_front()
        deque.pop_back()
    return True

def is_palindrome(s: str) -> bool:
    i, j = 0, len(s) - 1
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True

if __name__ == "__main__":
    for func in (is_palindrome_stack, is_palindrome_deque, is_palindrome):
        assert func("racecar") is True
        assert func("abba") is True
        assert func("abc") is False
        assert func("") is True
        assert func("a") is True
        assert func("aa") is True
        assert func("ab") is False
        assert func("12321") is True
    print("OK!")