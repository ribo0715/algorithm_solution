# 광고 삽입
"""
누적 재생시간이 가장 큰 구간

log 30만개 -> log를 어떻게 저장해놓을 수 있을까
-> 초단위로? -> 길이 40만정도 배열..? -> 아닌 것 같음

logs를 sort -> 시작 시간 순서로
-> 앞으로 더 땡길 수 있으면 더 땡김
-> 이것도 아닌 것 같은데...

adv_time 에 대해 시작시간, 끝시간 계산?
"""


# HH:MM:SS 형식을 초로 계산
def make_time_to_second(time):
    hh = int(time[0:2])
    mm = int(time[3:5])
    ss = int(time[6:8])

    result = hh * 3600 + mm * 60 + ss

    return result


def make_second_to_time(second):
    hh = second // 3600
    second = second % 3600
    mm = second // 60
    second = second % 60
    ss = second

    result = str(hh).zfill(2) + ":" + str(mm).zfill(2) + ":" + str(ss).zfill(2)

    return result


def solution(play_time, adv_time, logs):
    play_time = make_time_to_second(play_time)
    adv_time = make_time_to_second(adv_time)

    count_list = [0 for _ in range(play_time + 1)]  # 각 시각에 재생 기록이 몇 번 있는지를 나타냄

    for log in logs:
        start_time, end_time = log.split("-")
        start_time = make_time_to_second(start_time)
        end_time = make_time_to_second(end_time)

        count_list[start_time] += 1
        count_list[end_time] -= 1

    for _ in range(2):  # 누적합 계산 이후 구간합 계산
        for i in range(len(count_list) - 1):  # 누적합 계산 -> 각 초에 몇 명이 재생했는지
            count_list[i + 1] += count_list[i]


    max_start_time = 0  # 최대가 될 때 시작 시간
    max_count = count_list[adv_time] # 00:00:00 부터 시작하는 경우를 default 최대로 두고 시작

    for start_time in range(play_time - adv_time):
        end_time = start_time + adv_time
        cur_count = count_list[end_time] - count_list[start_time]

        if max_count < cur_count:
            max_count = cur_count
            max_start_time = start_time + 1

    answer = make_second_to_time(max_start_time)
    return answer
