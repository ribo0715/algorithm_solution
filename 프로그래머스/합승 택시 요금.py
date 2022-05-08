# 합승 택시 요금

from collections import defaultdict
from collections import deque

"""
S -> X, X -> A, X -> B

길을 어떻게 저장할지 -> 딕셔너리? ex) 3 : [2, 15] -> 3 - 2 길 연결, 요금 15
bfs -> 현재 가장 낮은 요금보다 크면 더이상 진행하지 않음
"""


# start에서 end까지 이동할 최소요금
def get_min_fare(start, end, road_dic):
    if start == end:
        return 0

    q = deque()  # 현재 위치와 현재까지의 요금을 담음
    q.append([start, 0])

    visited_dic = {}  # 각 지점에 도착했던 경우의 최저요금
    visited_dic[end] = 1e9

    while q:
        curr_spot, curr_fare = q.popleft()

        # curr_spot에서 이동가능한 지점들로 이동해봄
        for next_spot, plus_fare in road_dic[curr_spot]:
            next_fare = curr_fare + plus_fare

            # 현재까지 최저요금을 이미 넘어선 경우 더이상 진행 X
            if next_fare > visited_dic[end]:  # 현재까지의 최저요금을 이미 넘어선 경우
                continue  # 넘어감

            if next_spot in visited_dic:
                if visited_dic[next_spot] > next_fare:
                    visited_dic[next_spot] = next_fare  # 업데이트하고 다시 확인
                    q.append([next_spot, next_fare])
            else:
                visited_dic[next_spot] = next_fare
                q.append([next_spot, next_fare])

    return visited_dic[end]


def solution(n, s, a, b, fares):
    answer = 0

    road_dic = defaultdict(list)
    for fare in fares:
        road_dic[fare[0]].append([fare[1], fare[2]])
        road_dic[fare[1]].append([fare[0], fare[2]])

    # A, B에서 모두 도달 가능한 곳이 아니면 제외하고 생각했으면 더 성능이 좋아질까?

    total_min_fare = 1e9
    for target in range(1, n + 1):
        fare1 = get_min_fare(s, target, road_dic)
        fare2 = get_min_fare(a, target, road_dic)
        fare3 = get_min_fare(b, target, road_dic)

        total_curr_fare = fare1 + fare2 + fare3

        total_min_fare = min(total_min_fare, total_curr_fare)

    answer = total_min_fare

    return answer