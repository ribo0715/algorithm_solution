# 다음 큰 숫자
"""
n보다 큰 자연수
n의 다음 큰 숫자와 n은 2진수로 변환했을 때 1의 갯수가 같습니다.
조건 1, 2를 만족하는 수 중 가장 작은 수

-> n부터 1씩 더해가면서 2진수로 변환했을 때 1의 갯수를 파악
format(num, "b") -> num을 2진수로 변환했을 때 str 반환
"""


def solution(n):
    answer = 0

    n_binary = format(n, "b")
    n_count_1 = n_binary.count("1")

    num = n + 1
    while True:
        num_binary = format(num, "b")
        num_count_1 = num_binary.count("1")

        if n_count_1 == num_count_1:
            answer = num
            break

        num += 1

    return answer