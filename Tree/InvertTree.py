"""트리를 반전 시켜라"""
import collections


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

#BPS 구조
def invertTree2(root: TreeNode) -> TreeNode:
    queue = collections.deque([root])

    while queue:
        node = queue.popleft()
        # 부모 노드부터 하향식 스왑
        if node:
            node.left, node.right = node.right, node.left

            queue.append(node.left)
            queue.append(node.right)

    return root

#DFS 구조
def invertTree3(root: TreeNode) -> TreeNode:
    stack = collections.deque([root])

    while stack:
        node = stack.pop()
        # 부모 노드부터 하향식 스왑
        if node:
            node.left, node.right = node.right, node.left

            stack.append(node.left)
            stack.append(node.right)
    return root



root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(9)


print(invertTree3(root).val)
print(invertTree3(root).left.val)
print(invertTree3(root).right.val)
print(invertTree3(root).left.left.val)
print(invertTree3(root).left.right.val)
print(invertTree3(root).right.left.val)
print(invertTree3(root).right.right.val)
