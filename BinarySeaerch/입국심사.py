
#속도 문제로 탈락
def solution(n, times):
    answer = 1

    while True:
        for i in times:
            if answer % i == 0:
                n -= 1
        if n > 0:
            answer += 1
        else:
            break

    return answer


print(solution(6,[2, 10]))