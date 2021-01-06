"""숫자 집합 candidates를 조합하여 합이 tartget이 되는 원소를 나열하라. 각 원소는 중복으로 낭려 가능하다."""
from typing import List

candidates, target = [2,3,6,7], 7

def combination_sum(candidates: List[int], target: int) ->List[List[int]]:
    result = []

    def dfs(csum, index, path):
        #종료 조건
        if csum < 0:
            return
        if csum == 0:
            result.append(path)

        for i in range(index, len(candidates)):
            dfs(csum - candidates[i], i, path + [candidates[i]])



    dfs(target, 0, [])
    return result


print(combination_sum(candidates, target))
