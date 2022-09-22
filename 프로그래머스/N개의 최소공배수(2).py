# N개의 최소공배수
"""
유클리드 알고리즘(유클리드 호제법) 이용
https://velog.io/@limeorange/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-Python-N%EA%B0%9C%EC%9D%98-%EC%B5%9C%EC%86%8C%EA%B3%B5%EB%B0%B0%EC%88%98
"""


# a, b의 최소공배수를 반환
def get_least(a, b):
    A, B = a, b
    while b > 0:
        a, b = b, a % b

    greatest = a # 최대공약수
    return A * B // greatest


def solution(arr):
    arr.sort()

    temp = arr[0]
    for i in range(len(arr) - 1):
        temp = get_least(temp, arr[i + 1])

    answer = temp
    return answer