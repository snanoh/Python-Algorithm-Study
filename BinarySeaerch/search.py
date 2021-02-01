"""정렬된 nums를 입력받아 이진 검색으로 target에 해당하는 인덱스를 찾아라."""
import bisect
from typing import List

nums, target = [-1,0,3,5,9,12], 9


# 재귀함수
def search(nums: List[int], target: int) -> int:
    def binary_search(left, right):
        if left <= right:
            mid = (left + right) // 2

            if nums[mid] < target :
                return binary_search(mid + 1, right)
            elif nums[mid] > target :
                return binary_search(left, mid - 1)
            else:
                return mid
        else :
            return -1
    return binary_search(0, len(nums) - 1)

# 반복
def search2(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) //2

        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        else:
            return mid
    return -1


# 이진검색 모듈
def search3(nums: List[int], target: int) -> int:
    index = bisect.bisect_left(nums, target)
    print(index)
    if index < len(nums) and nums[index] == target:
        return index
    else:
        return -1




#print(search(nums,target))
#print(search2(nums,target))
print(search3(nums,target))