# 무지의 먹방 라이브 (기본 deque 사용) -> 효율성 검사 시간 초과

from collections import deque

"""
deque 로 구현하면 될 것 같은데?

k초 후에 몇 번 음식을 먹는지를 구하면 됨

만약 더 섭취해야 할 음식이 없다면 -1


전체 min값만큼은 그냥 전체 한바퀴 쭉 돌려도 가능

"""

def solution(food_times, k):
    answer = 0

    q = deque()
    for i in range(1, len(food_times) + 1):
        q.append([i, food_times[i - 1]])
    # print(q)

    for _ in range(k):
        if not q:  # 다 먹은 경우
            return -1

        curr_food_num, curr_food_time = q.popleft()

        if curr_food_time > 1:
            next_food_time = curr_food_time - 1
            q.append([curr_food_num, next_food_time])

    if not q:
        return -1

    answer = q.popleft()[0]

    return answer