# 같은 숫자는 싫어
"""
연속으로 나타나는 숫자 제거
"""


def solution(arr):
    answer = []

    prev = arr[0]  # 이전 숫자를 담을 변수
    answer.append(prev)  # 가장 첫번째 원소는 바로 answer에 넣음

    for cur in arr:
        if prev != cur:  # 현재 숫자가 이전과 다른 경우
            answer.append(cur)
            prev = cur  # 현재 숫자(cur)를 prev에 담음

    return answer