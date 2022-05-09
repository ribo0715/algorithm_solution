# 무지의 먹방 라이브

from collections import deque

"""
deque 로 구현하면 될 것 같은데?

k초 후에 몇 번 음식을 먹는지를 구하면 됨

만약 더 섭취해야 할 음식이 없다면 -1


전체 min값만큼은 그냥 전체 한바퀴 쭉 돌려도 가능

"""


def solution(food_times, k):
    answer = 0

    time_q = deque(food_times)  # 현재 음식 섭취 남은 시간들을 담음
    num_q = deque([i for i in range(1, len(food_times) + 1)])  # 현재 음식의 번호 상태

    count = k  # 남은 음식 섭취 횟수

    while count > 0:
        if not time_q:
            break

        cur_min_time = min(time_q)

        min_time = min(time_q)

        # (time_q의 min값) * len(food_times) 만큼씩은 쭉쭉 빼도 됨
        if count >= min_time * len(time_q):
            count -= min_time * len(time_q)

            for i in range(len(time_q)):
                temp_time = time_q.popleft() - min_time
                if temp_time > 0:
                    num_q.append(num_q.popleft())
                    time_q.append(temp_time)
                else:
                    num_q.popleft()
            # print("time_q :", time_q)
            # print("num_q :", num_q)

        # time_q를 len(time_q)로 최대로 나눔
        else:
            temp_count = count // len(time_q)

            for i in range(len(time_q)):
                temp_time = (time_q.popleft() - temp_count)
                if temp_time > 0:
                    num_q.append(num_q.popleft())
                    time_q.append(temp_time)
                else:
                    num_q.popleft()

            for _ in range(count % len(time_q)):
                time_q.append(time_q.popleft())
                num_q.append(num_q.popleft())

            break

    if not num_q:
        return -1

    answer = num_q.popleft()

    return answer