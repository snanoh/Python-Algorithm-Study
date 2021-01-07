"""[from, to]로 구성된 항공권 목록을 이용해 JFK에서 출발하는 여행 일정을 구성하라.
여러 일정이 있는 경우 사전 어휘순으로 방문한다."""
import collections
from typing import List

tikets = [["MUC","LHR"], ["JFK","MUC"], ["SFO","SJC"],["LHR","SFO"]]
tikets2 = [["JFK","SFO"], ["JFK","ATL"], ["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]

def find_itinerary(tikets: List[List[str]]) -> List[str]:
    graph = collections.defaultdict(list)
    # 그래프 순서대로 구성
    for a, b in sorted(tikets):
        graph[a].append(b)

    route = []
    def dfs(a):
        # 첫 번째 값을 읽어 어휘 순 방문
        while graph[a]:
            dfs(graph[a].pop(0))
        route.append(a)

    dfs('JFK')
    # 다시 뒤집어 어휘 순 결과로
    return route[::-1]


def find_itinerary2(tikets: List[List[str]]) -> List[str]:
    graph = collections.defaultdict(list)
    # 그래프 순서대로 구성
    for a, b in sorted(tikets):
        graph[a].append(b)

    route, stack = [], ['JFK']
    while stack:
        # 반복으로 스택을 구성하되 막히는 부분에서 풀어내는 처리
        while graph[stack[-1]]:
            stack.append(graph[stack[-1]].pop(0))
        route.append(stack.pop())

    # 다시 뒤집어 어휘 순 결과로
    return route[::-1]



#print(find_itinerary(tikets2))
print(find_itinerary2(tikets2))


