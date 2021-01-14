"""시작점에서 도착점까지의 가장 저렴한 가격을 계산하되, K개의 경유지 이내에 도착하는 가격을 리턴하라. 
   경로가 존재하지 않을 경우 -1을 리턴하라"""
import collections
import heapq
from typing import List

n = 3
edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0
dst = 2
K = 1

def find_cheapest_price(flights: List[List[int]], src: int, dst: int, K:int) -> int:
    graph = collections.defaultdict(list)
    # 그래프 인접 리스트 구성
    for u, v, w in flights:
        graph[u].append((v,w))

    # 큐 변수: [(가격, 정점, 남은 가능 경유지 수)]
    Q = [(0, src, K)]

    # 우선순위 큐 최솟값 기주으로 도착점까지 최소 비용 판별
    while Q:
        price, node, k = heapq.heappop(Q)
        if node == dst:
            return price
        if k >= 0:
            for v, w in graph[node]:
                alt = price + w
                heapq.heappush(Q, (alt, v, k - 1))
    return -1

print(find_cheapest_price(edges, src, dst, K))