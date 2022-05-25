# 3124. 최소 스패닝 트리 - Trim 알고리즘
"""
모든 정점들을 연결하는 부분 그래프 중에서 그 가중치의 합이 최소인 트리

1) Prim 알고리즘 -> 정점들을 기준으로 어떤 정점에서 가장 가중치가 낮은 쪽으로 이동해가며 연결 -> heap 이용
2) Kruskal 알고리즘 -> 간선들을 가중치 기준으로 정렬 -> 작은 것부터 연결해가면서 서브그래프의 root를 바꿔감

1
7 9
0 1 29
1 2 16
2 3 12
3 4 22
4 5 27
5 0 10
6 1 15
6 3 18
6 4 25
"""

import heapq
from collections import defaultdict

if __name__ == "__main__":
    T = int(input())

    for test_case in range(1, T + 1):
        V, E = map(int, input().split()) # 정점의 개수 V(1≤V≤100,000)와 간선의 개수 E(1≤E≤200,000)
        routes = defaultdict(list) #

        for _ in range(E):
            A, B, C = map(int, input().split()) # A번 정점과 B번 정점이 가중치 C인 간선으로 연결되어 있다
            routes[A].append((C, B)) # A에서 B로 이동할 때 C만큼 가중치를 가진 간선
            routes[B].append((C, A)) # B에서 A로 이동할 때 C만큼 가중치를 가진 간선

        start_v = list(routes.keys())[0]
        next_route_list = routes[start_v] # 현재 정점의 위치에서 이동 가능한
        heapq.heapify(next_route_list)

        visited = set()  # 방문 표시
        visited.add(start_v)
        # print(start_v, "번 정점에서 시작")
        answer = 0

        while next_route_list:
            weight, next_v = heapq.heappop(next_route_list)

            if next_v not in visited:
                # print(next_v, "번 정점으로 이동 => 가중치", weight, "만큼 더함")
                visited.add(next_v)
                answer += weight

                for route in routes[next_v]:
                    if route[1] not in visited: # 이전에 방문했던 곳들은 다시 방문하지 않도록
                        heapq.heappush(next_route_list, route)

                # next_route_list = routes[next_v]
                # heapq.heapify(next_route_list)

        # print(visited)
        print("#{} {}".format(test_case, answer))