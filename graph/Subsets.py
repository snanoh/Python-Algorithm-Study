"""모든 부분 집합을 리턴하라"""
from typing import List

nums = [1,2,3]

def subsets(nums: List[int]) -> List[List[int]]:
    result = []

    def dfs(index, path):
        result.append(path)

        for i in range(index,len(nums)):
            dfs( i +1 , path + [nums[i]])


    dfs(0, [])
    return result

print(subsets(nums))