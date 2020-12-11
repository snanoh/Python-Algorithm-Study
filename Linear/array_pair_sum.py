from typing import List

nums = [1, 4, 3, 2]

def array_pair_sum(nums: List[int]) -> int:
    sum = 0
    pair = []
    nums.sort()

    for n in nums:
        #앞에서부터 오름차순으로 페어를 만들어서 합 계산
        pair.append(n)
        if len(pair) == 2:
            sum += min(pair)
            pair = []

    return sum

# min 사용 x
def array_pair_sum2(nums: List[int]) -> int:
    sum = 0
    nums.sort()

    for i, n in enumerate(nums):
        # 짝수 번째의 값의 합 계산
        if i % 2 == 0:
            sum += n

    return sum

#파이썬 다운 방식
def array_pair_sum3(nums: List[int]) -> int:
    return sum(sorted(nums)[::2])

print(array_pair_sum(nums))
print(array_pair_sum2(nums))
print(array_pair_sum3(nums))

