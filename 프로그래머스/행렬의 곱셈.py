# 행렬의 곱셈

def solution(arr1, arr2):
    answer = [[]]

    a, b = len(arr1), len(arr1[0])
    c = len(arr2[0])

    # answer은 (a x c) 구조
    answer = [[0 for _ in range(c)] for _ in range(a)]

    for x in range(a):
        for y in range(c):
            for z in range(b):
                answer[x][y] += arr1[x][z] * arr2[z][y]

    return answer