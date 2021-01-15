"""이진 트리의 최대 깊이를 구하라."""
import collections
from typing import List

nums = [3, 9, 20, "", "", 15, 7]

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def max_depth(root : TreeNode) -> int:
    if root is None:
        return 0
    queue = collections.deque([root])
    depth = 0

    while queue:
        depth += 1
        # 큐연산 추출 노드의 자식 노드 삽입
        for _ in range(len(queue)):
            cur_root = queue.popleft()
            if cur_root.left:
                queue.append(cur_root.left)
            if cur_root.right:
                queue.append(cur_root.right)
    # BFS 반복 횟수 == 깊이
    return depth

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print(max_depth(root))


