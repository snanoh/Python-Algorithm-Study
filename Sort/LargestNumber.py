from typing import List



def to_swap(n1: int, n2: int) -> bool:
    return str(n1) + str(n2) < str(n2) + str(n1)

# 삽입 정렬 구현
def largestNumber( nums: List[int]) -> str:
    i = 1
    while i < len(nums):
        j = i
        while j > 0 and to_swap(nums[j - 1], nums[j]):
            nums[j], nums[j - 1] = nums[j - 1], nums[j]
            j -= 1
        i += 1

    return str(int(''.join(map(str, nums))))


nums = [3, 30, 34, 5, 9]

print(largestNumber(nums))
