from itertools import permutations


def solution(numbers):
    answer = 0

    perm_numbers = make_number_list(numbers)

    for num in perm_numbers:
        if is_prime_num(num):
            answer += 1

    return answer


# numbers 문자열을 받아 가능한 숫자들의 조합을 만드는 함수
def make_number_list(numbers):
    num_list = [num for num in numbers]  # 문자열에서 하나씩 숫자를 떼어냄

    perm_list = []

    for i in range(1, len(numbers) + 1):
        perm_list += list(permutations(num_list, i))

    perm_numbers = [int(("").join(perm)) for perm in perm_list]  # 문자열 조합을 이어주고, int로

    perm_numbers = list(set(perm_numbers))

    return perm_numbers


# 해당 숫자가 소수인지 판별하는 함수
def is_prime_num(num):
    if num <= 1:
        return False

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True