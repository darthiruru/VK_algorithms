class TreeNode:
    def __init__(self, val: int=0, left: TreeNode=None, right: TreeNode=None) -> None:
        self.val = val
        self.left = left
        self.right = right

def is_symmetric(root: TreeNode) -> bool:
    if root is None:
        return True
    queue = [root]
    while len(queue) > 0:
        queue_len = len(queue)
        for i in range(queue_len // 2):
            left = queue[i]
            right = queue[-i - 1]
            if left is None and right is None:
                continue
            if left is None or right is None:
                return False
            if left.val != right.val:
                return False
        next_level = []
        for node in queue:
            if node is not None:
                next_level.append(node.left)
                next_level.append(node.right)
        queue = next_level
    return True

def depth_search(root: TreeNode, res: list[int]) -> None:
    if root is None:
        res.append(None)
        return
    depth_search(root.left, res)
    res.append(root.val)
    depth_search(root.right, res)
    
def is_symmetric_dfs(root: TreeNode) -> bool:
    if root is None:
        return True
    data = []
    depth_search(root, data)
    if data == data[::-1]:
        return True
    return False
    

if __name__ == "__main__":
    assert is_symmetric(None) == True
    assert is_symmetric_dfs(None) == True
    assert is_symmetric(TreeNode(1)) == True
    assert is_symmetric_dfs(TreeNode(1)) == True
    root = TreeNode(1, TreeNode(2), None)
    assert is_symmetric(root) == False
    assert is_symmetric_dfs(root) == False
    root = TreeNode(1, TreeNode(2), TreeNode(2))
    assert is_symmetric(root) == True
    assert is_symmetric_dfs(root) == True
    root = TreeNode(1,
        TreeNode(2, None, TreeNode(3)),
        TreeNode(2, TreeNode(3), None)
    )
    assert is_symmetric(root) == True
    assert is_symmetric_dfs(root) == True
    root = TreeNode(1,
        TreeNode(2, None, TreeNode(3)),
        TreeNode(2, None, TreeNode(3))
    )
    assert is_symmetric(root) == False
    assert is_symmetric_dfs(root) == False
    root = TreeNode(1, TreeNode(2), TreeNode(3))
    assert is_symmetric(root) == False
    assert is_symmetric_dfs(root) == False
    root = TreeNode(1,
        TreeNode(2, TreeNode(3), None),
        TreeNode(2, None, TreeNode(4))
    )
    assert is_symmetric(root) == False
    assert is_symmetric_dfs(root) == False
    root = TreeNode(1,
        TreeNode(2, TreeNode(3), None),
        None
    )
    assert is_symmetric(root) == False
    assert is_symmetric_dfs(root) == False