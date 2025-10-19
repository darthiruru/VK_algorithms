class Node:
    def __init__(self, value: str) -> None:
        self.next__ = None
        self.value__ = value

    def set_value(self, value: str) -> None:
        self.value__ = value

    def get_value(self) -> str:
        return self.value__
    
    def set_next(self, next: Node | None) -> None:
        self.next__ = next

    def get_next(self) -> Node | None:
        return self.next__

class Queue:
    def __init__(self) -> None:
        self.head__ = None
        self.tail__ = None
        self.size__ = 0

    def push(self, value: str) -> None:
        new_node = Node(value)
        if self.size__ == 0:
            self.head__ = new_node
            self.tail__ = new_node
        else:
            self.tail__.set_next(new_node)
            self.tail__ = new_node
        self.size__ += 1
    
    def pop(self) -> str | None:
        if self.size__ == 0:
            return None
        value = self.head__.get_value()
        self.size__ -= 1
        self.head__ = self.head__.get_next()
        if self.head__ is None:
            self.tail__ = None
        return value

    def peek(self) -> str | None:
        if self.size__ == 0:
            return None
        return self.head__.get_value()
    
    def get_size(self) -> int:
        return self.size__

def is_subsequence_queue(str1: str, str2: str) -> bool:
    q = Queue()
    for char in str1:
        q.push(char)
    for char in str2:
        if q.get_size() > 0 and q.peek() == char:
            q.pop()
    return q.get_size() == 0


def is_subsequence(str1: str, str2: str) -> bool:
    i, j = 0, 0
    while i < len(str1) and j < len(str2):
        if str1[i] == str2[j]:
            i += 1
        j += 1
    return i == len(str1)


if __name__ == '__main__':
    assert is_subsequence_queue("abc", "ahbgdc") is True
    assert is_subsequence_queue("axc", "ahbgdc") is False
    assert is_subsequence_queue("", "ahbgdc") is True
    assert is_subsequence_queue("a", "") is False
    assert is_subsequence_queue("ace", "abcde") is True
    print("Queue version OK")

    assert is_subsequence("abc", "ahbgdc") is True
    assert is_subsequence("axc", "ahbgdc") is False
    assert is_subsequence("", "ahbgdc") is True
    assert is_subsequence("a", "") is False
    assert is_subsequence("ace", "abcde") is True
    print("Index version OK")