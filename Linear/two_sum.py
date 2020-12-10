from typing import List

nums = [2, 9, 9, 15]
target = 18

#brute force
def two_sum(nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)):
        for j in range(i +1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

print(two_sum(nums, target))

def two_sum2(nums: List[int], target: int) -> List[int]:
    for i, n in enumerate(nums):
        complement = target - n

        if complement in nums[i + 1:]:
            return [nums.index(n), nums[i + 1:].index(complement) + (i + 1)]

print(two_sum2(nums, target))

def two_sum3(nums: List[int], target: int) -> List[int]:
    nums_map = {}
    # 키와 값을 바꿔서 딕셔너리로 저장
    for i, num in enumerate(nums):
        nums_map[num] = i

    for i, num in enumerate(nums):
        if target - num in nums_map and i != nums_map[target - num]:
            return [nums.index(num), nums_map[target - num]]

print(two_sum3(nums, target))

def two_sum4(nums: List[int], target: int) -> List[int]:
    nums_map = {}
    # 3번의 for문을 하나의 for 문으로 통합
    for i, num in enumerate(nums):
        if target - num in nums_map:
            return [nums_map[target - num], i]
        nums_map[num] = i
        
print(two_sum4(nums, target))

#투포인터 (정렬된 상태만 가능)
def two_sum5(nums: List[int], target: int) -> List[int]:
    left, right = 0, len(nums) -1
    while not left == right:
        # 합이 타겟보다 크면 오른쪽 포인터를 왼쪽으로
        if nums[left] + nums[right] < target:
            left += 1
        elif nums[left] + nums[right] > target:
            right -= 1
        else:
            return [left, right]

print(two_sum5(nums, target))