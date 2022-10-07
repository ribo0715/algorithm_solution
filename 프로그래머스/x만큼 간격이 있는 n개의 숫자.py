# x만큼 간격이 있는 n개의 숫자

def solution(x, n):
    answer = [x] * n

    for i in range(n):
        answer[i] *= (i + 1)

    return answer