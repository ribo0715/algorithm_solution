# 숫자의 표현
"""
완전탐색 -> 1부터 시작해서 확인
"""


def solution(n):
    answer = 0

    for i in range(1, n + 1):
        cur_sum = 0
        for j in range(i, n + 1):
            cur_sum += j
            if cur_sum == n:
                answer += 1
                break
            elif cur_sum > n:
                break

    return answer