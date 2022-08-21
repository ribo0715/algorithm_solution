# 최소직사각형
"""
모든 명함들이 들어갈 수 있도록 하는 최소 지갑의 크기
-> 가로, 세로 길이가 담긴 sizes를 읽으면서 더 긴쪽 길이를 A에, 짧은쪽 길이를 B에 저장
-> 긴쪽 길이에서 최대값, 짧은쪽 길이에서 최대값
"""


def solution(sizes):
    answer = 0

    max_a, max_b = 0, 0

    for size in sizes:
        a = max(size)
        b = min(size)

        max_a = max(max_a, a)
        max_b = max(max_b, b)

    answer = max_a * max_b

    return answer
