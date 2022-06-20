# 실패율
"""
스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어 수

전체 스테이지의 개수 N
게임을 이용하는 사용자가 현재 멈춰있는 스테이지의 번호가 담긴 배열 stages

딕셔너리로 각 스테이지 번화(key)에 대한 실패율(value)을 저장
-> 실패율(value)를 기준으로 정렬

k번 스테이지에 도달 -> k - 1 번째 스테이지까지 클리어

각 스테이지를 클리어한 플레이어의 수를 저장할 배열
k번 스테이지의 실패율 -> k번 스테이지에 도달한 플레이어 수 / k + 1번 스테이지 도달한 플레이어 수
"""

import operator


def solution(N, stages):
    answer = []

    arr = [0] * (N + 2)
    dic = {}

    for stage in stages:
        # stage - 1 번 스테이지까지 클리어
        arr[0] += 1
        arr[stage] -= 1

    for i in range(1, N + 1):
        arr[i] += arr[i - 1]

        if arr[i - 1] == 0:
            dic[i] = 0
        else:
            dic[i] = 1 - arr[i] / arr[i - 1]  # i - 1번 스테이지를 클리어한 플레이어 수 / i번 스테이지 클리어한 플레이어 수

    sorted_dic = sorted(dic.items(), key=operator.itemgetter(1), reverse=True)
    # print(sorted_dic)
    for stage in sorted_dic:
        answer.append(stage[0])

    return answer