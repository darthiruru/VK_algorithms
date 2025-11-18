class TreeNode:
    def __init__(self, val: int=0, left: TreeNode=None, right: TreeNode=None) -> None:
        self.val = val
        self.left = left
        self.right = right

def is_same_tree(a: TreeNode, b: TreeNode) -> bool:
    if a is None and b is None:
        return True
    if a is None or b is None:
        return False
    if a.val != b.val:
        return False
    return is_same_tree(a.left, b.left) and is_same_tree(a.right, b.right)


if __name__ == '__main__':
    assert is_same_tree(None, None) is True
    assert is_same_tree(TreeNode(1), None) is False
    assert is_same_tree(None, TreeNode(1)) is False
    assert is_same_tree(TreeNode(1), TreeNode(1)) is True
    assert is_same_tree(TreeNode(1), TreeNode(2)) is False
    a = TreeNode(1, TreeNode(2), TreeNode(3))
    b = TreeNode(1, TreeNode(2), TreeNode(3))
    assert is_same_tree(a, b) is True
    a = TreeNode(1, TreeNode(2), None)
    b = TreeNode(1, None, TreeNode(2))
    assert is_same_tree(a, b) is False
    a = TreeNode(1, TreeNode(2, TreeNode(3)))
    b = TreeNode(1, TreeNode(2, TreeNode(3)))
    assert is_same_tree(a, b) is True
    a = TreeNode(1, TreeNode(2, TreeNode(3)))
    b = TreeNode(1, TreeNode(2, TreeNode(4)))
    assert is_same_tree(a, b) is False
    a = TreeNode(1, TreeNode(2), TreeNode(3))
    b = TreeNode(1, TreeNode(2), TreeNode(4))
    assert is_same_tree(a, b) is False