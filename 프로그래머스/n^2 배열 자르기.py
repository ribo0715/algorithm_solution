# n^2 배열 자르기

def solution(n, left, right):
    answer = []

    for i in range(left, right + 1):
        x = i // n
        y = i % n

        # x행 y열에 위치한 숫자
        if x >= y:  # ex) 5행 2열 -> 5
            answer.append(x + 1)
        else:
            answer.append(y + 1)

    return answer

