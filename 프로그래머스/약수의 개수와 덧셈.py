# 약수의 개수와 덧셈
"""
left부터 right까지의 모든 수들에 대해 약수의 개수 확인
-> 짝수개면 +, 홀수개면 -
"""


# num이 약수를 짝수개를 가지면 True반환, 홀수개를 가지면 False반환
def has_even_nums(num):
    return


def solution(left, right):
    answer = 0

    for num in range(left, right + 1):
        if has_even_nums(num):
            answer += num
        else:
            answer -= num

    return answer