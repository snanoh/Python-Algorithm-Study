"""이진 트리가 높이 균현인지 판단하라 (모든 노드의 서브 트리간의 높이가 1이하인 것을 의미한다)"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def is_balanced(root: TreeNode) -> bool:
    def check(root):
        if not root:
            return 0

        left = check(root.left)
        right = check(root.right)
        # 높이 차이가 나는 경우 -1, 이외에는 높이에 따라 1 증가
        if left == -1 or right == -1 or abs(left - right) > 1:
            return -1
        return max(left, right) + 1
    return check(root) != -1

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(3)
#root.left.left.left = TreeNode(4)
#root.left.left.right = TreeNode(4)

print(is_balanced(root))

