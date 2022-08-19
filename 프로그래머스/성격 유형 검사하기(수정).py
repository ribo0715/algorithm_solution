# 성격 유형 검사하기
"""
n개의 질문 -> 7개 선택지
질문에 따라 특정 유형에 점수가 부여됨

survey 각 원소의 첫번째 캐릭터가 비동의에 대해 부여받는 성격 유형

choices 각 원소의 값에 따라 특정 유형에 점수를 부여

각 지표에서 더 점수가 높은 성격 유형으로 결정, 동점은 사전순으로 빠른 유형으로
"""

from collections import defaultdict


def solution(survey, choices):
    answer = ''
    n = len(survey)
    dict = defaultdict(int)
    for i in range(n):
        choice = choices[i]

        if 1 <= choice <= 3:  # 비동의 -> survey의 첫 캐릭터에 점수 부여
            target = survey[i][0]
            dict[target] += abs(choice - 4)  # 4점과 떨어진 정도만큼 점수 부여
        elif 5 <= choice <= 7:  # 동의
            target = survey[i][1]
            dict[target] += abs(choice - 4)  # 4점과 떨어진 정도만큼 점수 부여

        # dict[target] += abs(choice - 4) # 4점과 떨어진 정도만큼 점수 부여 # 여기에 있으면 target 값이 정해지지 않은 경우에 문제가 런타임 에러가 발생할 수 있음

    if dict["R"] >= dict["T"]:
        answer += "R"
    else:
        answer += "T"

    if dict["C"] >= dict["F"]:
        answer += "C"
    else:
        answer += "F"

    if dict["J"] >= dict["M"]:
        answer += "J"
    else:
        answer += "M"

    if dict["A"] >= dict["N"]:
        answer += "A"
    else:
        answer += "N"

    return answer