# 약수의 개수와 덧셈
"""
left부터 right까지의 모든 수들에 대해 약수의 개수 확인
-> 짝수개면 +, 홀수개면 -

약수의 갯수를 어떻게 알 수 있을까?
-> 소인수분해 해서 구하는 공식? 그거 말고는 없을까?
-> 짝,홀 판단만 할 수 있는 방법은?
-> 소수?

-> 범위가 1000 이내이므로 그냥 약수 갯수를 구해봐도 괜찮을듯?
"""


# num이 약수를 짝수개를 가지면 True반환, 홀수개를 가지면 False반환
def has_even_nums(num):
    count = 0
    for i in range(1, num + 1):
        if num % i == 0:
            count += 1

    if count % 2 == 0:
        return True
    else:
        return False


def solution(left, right):
    answer = 0

    for num in range(left, right + 1):
        if has_even_nums(num):
            answer += num
        else:
            answer -= num

    return answer