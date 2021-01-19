"""트리를 반전 시켜라"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def invertTree(root: TreeNode) -> TreeNode:
    if root:
        root.left, root.right = invertTree(root.right), invertTree(root.left)
        return root
    return None



root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(9)


print(invertTree(root).val)
print(invertTree(root).left.val)
print(invertTree(root).right.val)
print(invertTree(root).left.left.val)
print(invertTree(root).left.right.val)
