# 음양 더하기
"""
해당하는 sign이 true이면 양수, false이면 음수
-> 총 합
"""


def solution(absolutes, signs):
    answer = 0

    for i in range(len(absolutes)):
        if signs[i]:
            answer += absolutes[i]
        else:
            answer += absolutes[i] * (-1)

    return answer