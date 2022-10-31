# 부족한 금액 계산하기

def solution(price, money, count):
    answer = -1

    need = 0

    for k in range(1, count + 1):
        need += price * k

    answer = need - money
    if answer >= 0:
        return answer
    else:
        return 0
