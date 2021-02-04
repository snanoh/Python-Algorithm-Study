"""파보나치"""

# 내 풀이
def solution():
    n = int(input())

    nums = [0,1]
    def fun(num1, num2):
        if num2 == n:
            return 0
        nums.append(nums[num1]+nums[num2])
        return fun(num1+1, num2+1)

    fun(0, 1)
    return nums[len(nums)-1]

def fibonacci(num):
    if num < 2:
        return num
    else:
        return fibonacci(num-1)+fibonacci(num-2)

def fibonacci():
    num = int(input())
    a, b = 0, 1
    for i in range(num):
        a, b = b, a+b
    return a





#print(solution())
#print(fibonacci(10))
print(fibonacci())