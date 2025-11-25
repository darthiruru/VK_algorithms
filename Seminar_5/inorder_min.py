class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorder_min_iterative(root: TreeNode, k: int):
    stack = []
    current = root
    counter = 0
    while stack or current:
        while current:
            stack.append(current)
            current = current.left
        current = stack.pop()
        counter += 1
        if counter == k:
            return current.val
        current = current.right
    return None

def inorder_min_recursive(node: TreeNode, k: int, counter: list[int]):
    if node is None:
        return None
    left_result = inorder_min_recursive(node.left, k, counter)
    if left_result is not None:
        return left_result
    counter[0] += 1
    if counter[0] == k:
        return node.val
    return inorder_min_recursive(node.right, k, counter)

def inorder_min(node: TreeNode, k: int):
    return inorder_min_recursive(node, k, [0])


if __name__ == "__main__":
    root = TreeNode(5, TreeNode(3, TreeNode(2), TreeNode(4)), TreeNode(7, TreeNode(6), TreeNode(8)))
    assert inorder_min_iterative(root, 1) == 2
    assert inorder_min(root, 1) == 2
    assert inorder_min_iterative(root, 2) == 3
    assert inorder_min(root, 2) == 3
    assert inorder_min_iterative(root, 3) == 4
    assert inorder_min(root, 3) == 4
    assert inorder_min_iterative(root, 4) == 5
    assert inorder_min(root, 4) == 5
    assert inorder_min_iterative(root, 5) == 6
    assert inorder_min(root, 5) == 6
    assert inorder_min_iterative(root, 6) == 7
    assert inorder_min(root, 6) == 7
    assert inorder_min_iterative(root, 7) == 8
    assert inorder_min(root, 7) == 8
    assert inorder_min_iterative(root, 8) is None
    assert inorder_min(root, 8) is None
    root = TreeNode(10)
    assert inorder_min_iterative(root, 1) == 10
    assert inorder_min(root, 1) == 10
    assert inorder_min_iterative(root, 2) is None
    assert inorder_min(root, 2) is None
    assert inorder_min_iterative(None, 1) is None
    assert inorder_min(None, 1) is None