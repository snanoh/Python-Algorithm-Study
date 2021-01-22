"""오름차순으로 정렬된 배열을 높이균형 이진 탐색 트리로 변환하라"""
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def sortedArrayToBST(nums: List[int]) -> TreeNode:
    if not nums:
        return None

    mid = len(nums) // 2

    # 분할 정복으로 이진 검색 결과 트리 구성
    node = TreeNode(nums[mid])
    node.left = sortedArrayToBST(nums[:mid])
    node.right = sortedArrayToBST(nums[mid + 1:])

    return node

print(sortedArrayToBST([-10, -3, 0, 5, 9]).val)
print(sortedArrayToBST([-10, -3, 0, 5, 9]).left.val)
print(sortedArrayToBST([-10, -3, 0, 5, 9]).right.val)