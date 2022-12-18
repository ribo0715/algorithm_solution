""" 5:49 ~ 5:58
x축 방향으로 a*k
y축 방향으로 b*k
원점과의 거리가 d를 넘지 않는 선 안에서(반지름이 d인 원 안에)

점이 총 몇개가 찍히는지 파악

k가 100만까지 가능한데, 전부 다 파악하면 안될듯
"""


def solution(k, d):
    answer = 0

    for x in range(0, d + 1, k):
        y = int((d ** 2 - x ** 2) ** (1 / 2))
        y = y // k + 1  # (a * k, 0) 에 찍히는 경우 + 1

        answer += y

    return answer