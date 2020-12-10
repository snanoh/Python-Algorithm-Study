from typing import List

nums = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]

#투포인터
def trap(height: List[int]) -> int:
    #height에 값이 없을 경우 0 처리
    if not height:
        return 0

    # 물의 양
    volumn = 0
    left, right = 0, len(height) - 1
    left_max, right_max = height[left], height[right];

    while left < right:
        left_max = max(height[left], left_max)
        right_max = max(height[right], right_max)

        #더 높은 쪽을 향해 투 포인터 이동
        if left_max <= right_max:
            volumn += left_max - height[left]
            left += 1
        else:
            volumn += right_max - height[right]
            right -= 1
    return volumn

print(trap(nums))

#스택
def trap2(height: List[int]) -> int:
    stack = []
    volume = 0

    for i in range(len(height)):
        # 변곡점을 만나는 경우
        while stack and height[i] > height[stack[-1]]:
            #스택에서 꺼낸다
            top = stack.pop()

            if not len(stack):
                break

            #이전과의 차이만큰 물 높이 처리
            distance = i - stack[-1] - 1
            waters = min(height[i], height[stack[-1]] - height[top])

            volume += distance * waters

        stack.append(i)

    return volume

print(trap2(nums))