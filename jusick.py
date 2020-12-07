def solution(prices):
    answer = []

    for i in range(len(prices)-1):
        num = prices.pop(0)
        none_price = 0
        for i in prices:
            if num > i:
                none_price += 1
                break
            else:
                none_price += 1
        answer.append(none_price)
    return answer


print(solution([1, 2, 3, 2, 3]))
