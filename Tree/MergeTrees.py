"""두 이진 트리를 병합하라. 중복되는 노드는 값을 합산한다."""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def merge_tree(t1: TreeNode, t2: TreeNode) -> TreeNode:
    if t1 and t2:
        node = TreeNode(t1.val + t2.val)
        node.left = merge_tree(t1.left, t2.left)
        node.right = merge_tree(t1.right, t2.right)

        return node
    else:
        return t1 or t2

t1 = TreeNode(1)
t1.left = TreeNode(3)
t1.right = TreeNode(2)
t1.left.left = TreeNode(5)

t2 = TreeNode(2)
t2.left = TreeNode(1)
t2.right = TreeNode(3)
t2.left.right = TreeNode(4)
t2.right.right = TreeNode(7)

print(merge_tree(t1, t2).val)
print(merge_tree(t1, t2).left.val)
print(merge_tree(t1, t2).right.val)
print(merge_tree(t1, t2).left.left.val)
print(merge_tree(t1, t2).left.right.val)
print(merge_tree(t1, t2).right.right.val)
