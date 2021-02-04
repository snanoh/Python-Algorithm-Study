"""0보다 크거나 같은 정수 N이 주어진다. 이때, N!을 출력하는 프로그램을 작성하시오"""


def solution():
    N = input()
    def fun(n):
        if n == 0:
            return 1
        return n*fun(n-1)

    return fun(int(N))

print(solution())