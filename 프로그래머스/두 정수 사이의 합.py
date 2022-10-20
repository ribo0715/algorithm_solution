# 두 정수 사이의 합

def solution(a, b):
    answer = 0

    if a == b:
        return a
    else:
        a, b = min(a, b), max(a, b)

    for num in range(a, b + 1):
        answer += num

    return answer