class TreeNode:
    def __init__(self, val: int=0, left: TreeNode=None, right: TreeNode=None) -> None:
        self.val = val
        self.left = left
        self.right = right

def build_tree(arr: list[int], i: int=0) -> TreeNode:
    if i >= len(arr):
        return None
    root = TreeNode(arr[i])
    root.left = build_tree(arr, 2 * i + 1)
    root.right = build_tree(arr, 2 * i + 2)
    return root


if __name__ == "__main__":
    assert build_tree([]) is None
    r = build_tree([5])
    assert r.val == 5 and r.left is None and r.right is None
    arr = [1,2,3,4,5,6,7]
    r = build_tree(arr)
    assert r.val == 1
    assert r.left.val == 2
    assert r.right.val == 3
    assert r.left.left.val == 4
    assert r.left.right.val == 5
    assert r.right.left.val == 6
    assert r.right.right.val == 7
