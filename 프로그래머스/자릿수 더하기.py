# 자릿수 더하기

def solution(n):
    answer = 0

    while n:
        answer += n % 10
        n = n // 10

    return answer