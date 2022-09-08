# 이진 변환 반복하기
"""
1. x의 모든 0을 제거
-> x = x.replace("0", "")

2. x의 길이 c -> c를 2진법으로 표현
-> str(format(len(x), "b"))

s가 "1"이 될때까지 이진 변환 수행
-> [이진 변환의 횟수, 제거된 0의 개수] 반환
"""


def delete_zero(x):
    count_zero = x.count("0")
    x = x.replace("0", "")  # x.replace("0", "") 해주는걸로 x가 바로 변화되지 않음

    return count_zero, x


def to_binary(x):
    length = len(x)

    return str(format(length, "b"))


def solution(s):
    answer = []
    conversion_count = 0
    total_deleted_zero_count = 0

    while s != "1":
        conversion_count += 1

        deleted_zero_count, s = delete_zero(s)
        total_deleted_zero_count += deleted_zero_count

        s = to_binary(s)

    answer = [conversion_count, total_deleted_zero_count]
    return answer