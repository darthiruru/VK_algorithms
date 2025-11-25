from collections import deque

class TreeNode:
    def __init__(self, val: int=0, left: TreeNode=None, right: TreeNode=None) -> None:
        self.val = val
        self.left = left
        self.right = right

def mirror_tree(node: TreeNode) -> TreeNode:
    if node is None:
        return None
    node.left, node.right = node.right, node.left
    mirror_tree(node.left)
    mirror_tree(node.right)
    return node

def mirror_tree_iterative(node: TreeNode) -> TreeNode:
    if node is None:
        return None
    queue = deque([node])
    while queue:
        current = queue.popleft()
        current.left, current.right = current.right, current.left
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    return node


if __name__ == "__main__":
    root = TreeNode(5, TreeNode(3, TreeNode(2), TreeNode(4)), TreeNode(7, TreeNode(6), TreeNode(8)))
    mirror_tree(root)
    assert root.left.val == 7
    assert root.right.val == 3
    assert root.left.left.val == 8
    assert root.left.right.val == 6
    assert root.right.left.val == 4
    assert root.right.right.val == 2
    assert mirror_tree(None) is None
    root = TreeNode(10)
    mirror_tree(root)
    assert root.val == 10
    assert root.left is None
    assert root.right is None

    root = TreeNode(5, TreeNode(3, TreeNode(2), TreeNode(4)), TreeNode(7, TreeNode(6), TreeNode(8)))
    mirror_tree_iterative(root)
    assert root.left.val == 7
    assert root.right.val == 3
    assert root.left.left.val == 8
    assert root.left.right.val == 6
    assert root.right.left.val == 4
    assert root.right.right.val == 2
    assert mirror_tree_iterative(None) is None
    root = TreeNode(10)
    mirror_tree_iterative(root)
    assert root.val == 10
    assert root.left is None
    assert root.right is None