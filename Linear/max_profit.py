# 한번의 거래로 낼 수 있는 최대 이익을 산출하라.
import sys
from typing import List

nums = [7, 1, 5, 3, 6, 4]

def max_profit(prices: List[int]) -> int:
    max_price = 0

    for i, price in enumerate(prices):
        for j in range(i, len(prices)):
            max_price = max(prices[j] - price , max_price)
    return max_price

print(max_profit(nums))

def max_profit2(prices: List[int]) -> int:
    profit = 0
    min_price = sys.maxsize

    # 최솟값과 최대값을 계속 갱신
    for price in prices:
        min_price = min(min_price, price)
        profit = max(profit, price - min_price)
    return profit