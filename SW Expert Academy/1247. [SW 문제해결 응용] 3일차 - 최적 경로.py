# 1247. [SW 문제해결 응용] 3일차 - 최적 경로
"""
회사에서 출발하여 N명의 고객을 모두 방문하고 집으로 돌아오는 경로 중 가장 짧은 것

회사와 집의 좌표가 주어지고, 2명에서 10명 사이의 고객 좌표

최단 경로의 이동거리 -> 어떻게 알 수 있을까...
"""
from collections import deque
from itertools import combinations
import copy


def get_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


if __name__ == "__main__":
    T = int(input())

    for test_case in range(1, T + 1):
        answer = 0
        N = int(input()) # 고객의 수 -> 2~10명이므로 그냥 다 해봐도 괜찮을 듯
        line = list(map(int, input().split()))

        company_x, company_y = line[:2]
        home_x, home_y = line[2:4]
        customer_list = line[4:]
        customer_num = len(customer_list) // 2
        loc_dic = {}
        for i in range(customer_num):
            loc_dic[i] = customer_list[2 * i : 2 * (i + 1)] # 각 번호의 고객의 위치를 담음

        # 차라리 각 경로간의 거리를 모두 다 구해놓는게 나을듯?
        path_list = list(combinations([i for i in range(customer_num)], 2))
        path_dic = {}
        for path in path_list: # 각 경로들에 대해 거리를 구해둠
            start, end = path
            start_x, start_y = loc_dic[start]
            end_x, end_y = loc_dic[end]
            distance = get_distance(start_x, start_y, end_x, end_y)

            path_dic[(start, end)] = distance
            path_dic[(end, start)] = distance

        for i in range(customer_num):
            target_x, target_y = loc_dic[i]
            path_dic[(11, i)] = get_distance(company_x, company_y, target_x, target_y) # 회사에서
            path_dic[(i, 12)] = get_distance(home_x, home_y, target_x, target_y) # 집으로



        q = deque()
        # [현재까지의 경로, 현재까지 이동 거리, 아직 방문하지 않은 지점]
        q.append([[11], 0, [i for i in range(customer_num)]]) # 회사에서 시작

        for _ in range(customer_num): # 모두 방문
            # print(len(q))
            for _ in range(len(q)):
                visited_path, cur_distance, not_visited = q.popleft()
                cur = visited_path[-1] # 현재 위치 cur에서 다음으로 이동
                for target in not_visited:
                    plus_distance = path_dic[(cur, target)]
                    next_path = copy.deepcopy(visited_path) + [target]
                    next_distance = cur_distance + plus_distance
                    next_not_visited = copy.deepcopy(not_visited)
                    next_not_visited.remove(target)

                    q.append([next_path, next_distance, next_not_visited])

        min_distance = 1e9
        # print(q)
        while q:
            visited_path, cur_distance, not_visited = q.popleft()
            cur = visited_path[-1]

            cur_distance += path_dic[(cur, 12)]

            min_distance = min(cur_distance, min_distance)

        answer = min_distance

        print("#{} {}".format(test_case, answer))
