from collections import deque

class TreeNode:
    def __init__(self, val: int=0, left: TreeNode=None, right: TreeNode=None) -> None:
        self.val = val
        self.left = left
        self.right = right

def is_max_heap(arr: list[int]) -> bool:
    n = len(arr)
    for i in range((n - 2) // 2 + 1):
        left = 2 * i + 1
        right = 2 * i + 2
        if left < n and arr[i] < arr[left]:
            return False
        if right < n and arr[i] < arr[right]:
            return False
    return True

def is_max_heap_bfs(root: TreeNode) -> bool:
    if not root:
        return True
    queue = deque([root])
    shouldBeLeaf = False
    while queue:
        current = queue.popleft()
        if current.left:
            if shouldBeLeaf or current.left.val > current.val:
                return False
            queue.append(current.left)
        else:
            shouldBeLeaf = True
        if current.right:
            if shouldBeLeaf or current.right.val > current.val:
                return False
            queue.append(current.right)
        else:
            shouldBeLeaf = True
    return True


if __name__ == '__main__':
    assert is_max_heap([]) is True
    assert is_max_heap([42]) is True
    assert is_max_heap([10, 9, 8, 7, 6, 5, 4]) is True
    assert is_max_heap([5, 5, 5, 5, 5]) is True
    assert is_max_heap([20, 15, 18, 10, 12]) is True
    assert is_max_heap([10, 20, 5]) is False
    assert is_max_heap([10, 5, 30]) is False 
    assert is_max_heap([40, 30, 20, 10, 50]) is False

    assert is_max_heap_bfs(None) is True
    assert is_max_heap_bfs(TreeNode(42)) is True
    root = TreeNode(10, TreeNode(9, TreeNode(7), TreeNode(6)), TreeNode(8, TreeNode(5), TreeNode(4)))
    assert is_max_heap_bfs(root) is True
    root = TreeNode(5, TreeNode(5, TreeNode(5), TreeNode(5)), TreeNode(5))
    assert is_max_heap_bfs(root) is True
    root = TreeNode(20, TreeNode(15, TreeNode(10), TreeNode(12)), TreeNode(18))
    assert is_max_heap_bfs(root) is True
    root = TreeNode(10, TreeNode(20), TreeNode(5))
    assert is_max_heap_bfs(root) is False
    root = TreeNode(10, TreeNode(5), TreeNode(30))
    assert is_max_heap_bfs(root) is False
    root = TreeNode(40, TreeNode(30, TreeNode(10), TreeNode(50)), TreeNode(20))
    assert is_max_heap_bfs(root) is False

