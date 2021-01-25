"""겹치는 구간을 병합하라"""
from typing import List

intervals = [[1,3], [2,6],[8,10],[15,18]]



def merge(intervals: List[List[int]]) -> List[List[int]]:
    merged = []
    for i in sorted(intervals, key=lambda x : x[0]):
        if merged and i[0] <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], i[1])
        else:
            merged += i,
    return merged



print(merge(intervals))