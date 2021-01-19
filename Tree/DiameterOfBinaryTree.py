"""이진트리에서 두 노드 간 가장 ㅇ긴 경로의 길이를 출력하라"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    longest: int = 0
    
    def diameter_of_binary_tree(self, root :TreeNode)-> int:
        def dfs(node: TreeNode) -> int:
            if not node:
                return -1
            # 왼쪽, 오른쪽의 각 리프 노드까지 탐색
            left = dfs(node.left)
            right = dfs(node.right)

            # 가장 긴 경로
            self.longest = max(self.longest, left + right + 2)
            # 상태값
            return max(left, right) + 1
        dfs(root)
        return self.longest

        


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

e = Solution()


print(e.diameter_of_binary_tree(root))
