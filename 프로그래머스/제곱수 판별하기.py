def solution(n):
    answer = 2

    temp = n ** (1 / 2)

    if temp == int(temp):
        answer = 1

    return answer