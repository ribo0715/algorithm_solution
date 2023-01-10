"""
6가지 경우로 나뉠 수 있음
각 경우에 대해 평행이 되는지 확인
"""


def solution(dots):
    answer = 0

    temp_list = [[0, 1, 2, 3], [0, 2, 1, 3], [0, 3, 1, 2], [1, 2, 0, 3], [1, 3, 0, 2], [2, 3, 0, 1]]

    for temp in temp_list:
        a, b, c, d = temp

        x1, y1 = dots[a]
        x2, y2 = dots[b]
        x3, y3 = dots[c]
        x4, y4 = dots[d]

        if abs((x2 - x1) / (y2 - y1)) == abs((x4 - x3) / (y4 - y3)):
            answer = 1
            break

    return answer