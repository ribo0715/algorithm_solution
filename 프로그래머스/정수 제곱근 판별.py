# 정수 제곱근 판별

def solution(n):
    answer = 0

    temp = n ** (1 / 2)

    if temp == int(temp):
        answer = (temp + 1) ** 2
    else:
        answer = -1

    return answer