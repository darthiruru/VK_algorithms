class TreeNode:
    def __init__(self, val: int=0, left: TreeNode=None, right: TreeNode=None) -> None:
        self.val = val
        self.left = left
        self.right = right
        self.balanceFactor = 0
        

def calculate_heights_and_balance(node: TreeNode) -> int:
    if node is None:
        return 0
    left_height = calculate_heights_and_balance(node.left)
    right_height = calculate_heights_and_balance(node.right)
    node.balanceFactor = left_height - right_height
    return 1 + max(left_height, right_height)

if __name__ == "__main__":
    assert calculate_heights_and_balance(None) == 0
    root = TreeNode(10)
    assert calculate_heights_and_balance(root) == 1
    assert root.balanceFactor == 0
    root = TreeNode(5, TreeNode(3), None)
    assert calculate_heights_and_balance(root) == 2
    assert root.balanceFactor == 1
    assert root.left.balanceFactor == 0
    root = TreeNode(5, TreeNode(3, TreeNode(2), TreeNode(4)), TreeNode(7, TreeNode(6), None))
    assert calculate_heights_and_balance(root) == 3
    assert root.balanceFactor == 0
    assert root.left.balanceFactor == 0
    assert root.right.balanceFactor == 1
    assert root.left.left.balanceFactor == 0
    assert root.left.right.balanceFactor == 0
    assert root.right.left.balanceFactor == 0
