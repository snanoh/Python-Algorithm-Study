"""정렬된 배열을 받아 타겟을 만들 수 있는 배열의 두숫자 인덱스를 리턴하라."""


from typing import List

# 투포인터
def twoSum(numbers: List[int], target: int) -> List[int]:
    left, right = 0, len(numbers) - 1
    while not left == right:
        if numbers[left] + numbers[right] < target:
            left += 1
        elif numbers[left] + numbers[right] > target:
             right -= 1
        else:
            return left + 1, right +1

def twoSum2(numbers: List[int], target: int) -> List[int]:
    for k, v in enumerate(numbers):
        left, right = k+1, len(numbers) - 1
        expected = target - v
        # 이진 검색으로 나머지 값 판별
        while left <= right:
            mid = left + (right - left)
            if numbers[mid] < expected:
                left = mid + 1
            elif numbers[mid] > expected:
                right = mid - 1
            else:
                return k + 1, mid + 1


numbers = [2,7,11,15]
target = 9

print(twoSum(numbers, target))
print(twoSum2(numbers, target))
