# 자연수 뒤집어 배열로 만들기

def solution(n):
    answer = []

    while n:
        temp = n % 10
        answer.append(temp)
        n = n // 10

    return answer