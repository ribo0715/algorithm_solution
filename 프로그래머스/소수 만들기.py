# 소수 만들기
"""
주어진 숫자 중 3개를 더했을 때 소수
3개를 더한 수 sum 에 대해 소수인지 아닌지를 판단

0부터 3000까지 값에 대해 해당 값이 소수인지 판단을 한번 한 경우, 그 결과를 저장해두어도 좋을듯
"""

from itertools import combinations


def is_prime_num(num):
    # 2부터 (num - 1) 까지 나누어지는지 확인
    for i in range(2, num):
        if num % i == 0:
            return False

    return True


def solution(nums):
    answer = 0

    picked_three_list = list(combinations(nums, 3))
    for three_nums in picked_three_list:
        sum_of_three_nums = sum(three_nums)
        if is_prime_num(sum_of_three_nums):
            answer += 1

    return answer