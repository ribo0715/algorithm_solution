# 최솟값 만들기
"""
길이가 같은 배열 A, B
배열 A, B에서 각각 한 개의 숫자를 뽑아 두 수를 곱함
이러한 과정을 배열의 길이만큼 반복하며, 두 수를 곱한 값을 누적하여 더함
-> 최종적으로 누적된 값이 최소가 되도록

A에선 큰 순서대로, B에선 작은 순서대로 꺼내어 곱함
"""


def solution(A, B):
    answer = 0

    A.sort()
    B.sort()

    for _ in range(len(A)):
        from_A = A.pop(0)
        from_B = B.pop(-1)

        answer += from_A * from_B

    return answer