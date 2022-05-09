# k진수에서 소수 개수 구하기
"""
n을 k진수로 만들었을때, 0을 제외한 구간들을 확인
소수가 존재하면
중복되어도 다 셈
"""


# 해당 수가 소수인지 확인
def is_prime_num(num):
    if num < 2:
        return False

    # 2부터 늘려가며 나눴을때 나머지가 있는지 확인
    for i in range(2, int(num ** (1 / 2)) + 1):  # num 의 제곱근까지만 확인해도 됨 -> 중요
        if num % i == 0:
            return False

    return True


# n을 k진수로 만들고 str형식으로 반환
def make_n_to_k_num(n, k):
    num_str = ""

    while True:
        curr = n % k
        n = n // k
        num_str = str(curr) + num_str
        if n == 0:
            break

    return num_str


def solution(n, k):
    answer = 0

    # n을 k진수의 str형식으로 만들고 0으로 split
    k_num_str = make_n_to_k_num(n, k)
    # print(k_num_str)

    for num in k_num_str.split("0"):  # 0으로 분리
        if num == "":
            continue

        # print(num, "이 소수일까?")
        if is_prime_num(int(num)):
            # print(num, "은 소수")
            answer += 1

    return answer