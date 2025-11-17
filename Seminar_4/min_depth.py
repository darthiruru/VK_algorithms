class TreeNode:
    def __init__(self, val: int=0, left: TreeNode=None, right: TreeNode=None) -> None:
        self.val = val
        self.left = left
        self.right = right

def min_depth(root: TreeNode) -> int:
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    if root.left is not None and root.right is not None:
        return 1 + min(min_depth(root.left), min_depth(root.right))
    if root.left is not None:
        return 1 + min_depth(root.left)
    return 1 + min_depth(root.right)

def min_depth_bfs(root: TreeNode) -> int:
    if root is None:
        return 0
    queue = [root]
    depth = 1
    while len(queue) > 0:
        next_level = []
        for node in queue:
            if node.left is None and node.right is None:
                return depth
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)
        queue = next_level
        depth += 1
    return depth

if __name__ == '__main__':
    assert min_depth(None) == 0
    assert min_depth(None) == 0
    assert min_depth(TreeNode(1)) == 1
    assert min_depth_bfs(TreeNode(1)) == 1
    root = TreeNode(1, TreeNode(2))
    assert min_depth(root) == 2
    assert min_depth_bfs(root) == 2
    root = TreeNode(1, None, TreeNode(2))
    assert min_depth(root) == 2
    assert min_depth_bfs(root) == 2
    root = TreeNode(1, TreeNode(2), TreeNode(3))
    assert min_depth(root) == 2
    assert min_depth_bfs(root) == 2
    root = TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3))
    assert min_depth(root) == 2
    assert min_depth_bfs(root) == 2
    root = TreeNode(1, TreeNode(2), TreeNode(3, None, TreeNode(5)))
    assert min_depth(root) == 2
    assert min_depth_bfs(root) == 2
    root = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4))))
    assert min_depth(root) == 4
    assert min_depth_bfs(root) == 4
    root = TreeNode(1, None, TreeNode(2, None, TreeNode(3, None, TreeNode(4))))
    assert min_depth(root) == 4
    assert min_depth_bfs(root) == 4
    root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5, TreeNode(6), None)), TreeNode(3))
    assert min_depth(root) == 2
    assert min_depth_bfs(root) == 2
    root = TreeNode(1, TreeNode(2, None, TreeNode(3, None, TreeNode(4))), None)
    assert min_depth(root) == 4
    assert min_depth_bfs(root) == 4