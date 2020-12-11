
# 배열을 입력 받아 합으로 0을 만들 수 있는 3개의 엘리먼트를 출력하라
from typing import List

nums = [-1, 0, 1, 2, -1, -4]

def three_sum(nums: List[int]) -> List[List[int]]:
    result = []
    nums.sort() #정렬 [-4, -1, -1, 0, 1, 2]

    for i in range(len(nums) - 2):
        #중복된 값 건너 뛰기
        if nums[i] == nums[i - 1]:
            continue
        for j in range(i + 1, len(nums) - 1):
            if j > i and nums[j] == nums[j - 1]:
                continue
            for k in range(j + 1, len(nums)):
                if k > j + 1 and nums[k] == nums[k - 1]:
                    continue
                if nums[i] + nums[j] + nums[k] == 0:
                    result.append((nums[i], nums[j], nums[k]))

    return result

#print(three_sum(nums))

# 투포인트 방식
def three_sum2(nums: List[int]) -> List[List[int]]:
    result = []
    nums.sort() #정렬 [-4, -1, -1, 0, 1, 2]

    for i in range(len(nums) -2):
        #중복된 값 건너 뛰기
        if nums[i] == nums[i - 1]:
            continue
        #간격을 좁혀가며 합 sum 계산
        left, right = i + 1, len(nums) - 1
        while left < right:
            sum = nums[i] + nums[left] + nums[right]
            if sum < 0:
                left += 1
            elif sum > 0:
                right -= 1
            else:
                #sum = 0인 경우이므로 정답 및 스킵처리
                result.append((nums[i], nums[left], nums[right]))

            while left < right and nums[left] == nums[left + 1]:
                left += 1

            while left < right and nums[right] == nums[right -1 ]:
                right -= 1

            left += 1
            right -= 1
    return result

print(three_sum2(nums))