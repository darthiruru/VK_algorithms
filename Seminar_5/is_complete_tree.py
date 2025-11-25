from collections import deque

class TreeNode:
    def __init__(self, val: int=0, left: TreeNode=None, right: TreeNode=None) -> None:
        self.val = val
        self.left = left
        self.right = right


def is_complete_tree(root: TreeNode) -> bool:
    if not root:
        return True
    queue = deque([root])
    shouldBeLeaf = False
    while len(queue) > 0:
        node = queue.popleft()
        if not node:
            shouldBeLeaf = True
        else:
            if shouldBeLeaf:
                return False
            queue.append(node.left)
            queue.append(node.right)
    return True


if __name__ == '__main__':
    assert is_complete_tree(None) is True
    assert is_complete_tree(TreeNode(1)) is True
    root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
    assert is_complete_tree(root) is True
    root = TreeNode(1, TreeNode(2, None, TreeNode(4)),TreeNode(3))
    assert is_complete_tree(root) is False
    root = TreeNode(1, TreeNode(2, TreeNode(4), None), TreeNode(3, None, None))
    assert is_complete_tree(root) is True
    root = TreeNode(1, TreeNode(2, TreeNode(4), None), TreeNode(3, None, TreeNode(7)))
    assert is_complete_tree(root) is False

    
