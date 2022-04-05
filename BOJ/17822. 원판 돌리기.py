# 17822. 원판 돌리기

"""
반지름이 1, 2, ..., N인 원판이 크기가 작아지는 순으로 바닥에 놓여있다
원판의 반지름이 i이면, 그 원판을 i번째 원판

각각의 원판에는 M개의 정수가 적혀있고, i번째 원판에 적힌 j번째 수의 위치는 (i, j)로 표현

2 ≤ i ≤ N-1
2 ≤ j ≤ M-1

원판의 회전은 독립적으로 이루어진다

총 T번 회전
원판의 회전 방법은 미리 정해져 있고, i번째 회전할때 사용하는 변수는 xi, di, ki
번호가 xi의 배수인 원판을 di방향으로 ki칸 회전
di가 0인 경우는 시계 방향, 1인 경우는 반시계 방향

원판에 수가 남아 있으면, 인접하면서 수가 같은 것을 모두 찾는다
그러한 수가 있는 경우에는 원판에서 인접하면서 같은 수를 모두 지운다
없는 경우에는 원판에 적힌 수의 평균을 구하고, 평균보다 큰 수에서 1을 빼고, 작은 수에는 1을 더한다

원판을 T번 회전시킨 후 원판에 적힌 수의 합 구하기
"""

# deque 형태로 각 원판을 표현 -> 시계 반시계 에 따라 뒤, 앞에서 뺌


# xi, di, ki 에 대한 회전
def rotate_disc(xi, di, ki): # 번호가 xi의 배수인 원판을 di방향으로 ki칸 회전
    # print("###", xi, "의 배수인 원판 시작 ###")
    for i in range(N):
        if (i + 1) % xi == 0: # 번호가 xi의 배수인 원판에 대해, i번째
            # print(i, "번째 원판")
            for _ in range(ki): # ki칸 회전
                # di가 0인 경우는 시계 방향, 1인 경우는 반시계 방향
                if di == 0: # 시계 방향 -> 뒤에서 pop, 앞에 붙여줌
                    disc[i].appendleft(disc[i].pop())

                else: # 반시계 방향 -> 맨앞에서 pop, 뒤에 붙여줌
                    disc[i].append(disc[i].popleft())

            # print("After", i, "번째 rotate")
            # print(disc)

    if get_disc_total() != 0:
        find_adjacent_num()
        # print("After 인접 수 지우기")
        # print(disc)

# 원판에 수가 남은 경우, 인접한 수에 대한 작업 수행
def find_adjacent_num(): # i번 원판
    target = deque() # 지워야 할 원판 위치 저장 -> (i, j) 형태로 저장
    # 겹치는 거 들어갈테니, 마지막에 deque(set(target)) 을 해주면 될 듯?
    for i in range(N): # 원판에 수가 남은 경우
        # 인접하면서 같은 수 지움
        for m in range(M): # 같은 원판 내 인접한 수
            if m == 0: # M - 1, 1
                if disc[i][m] == disc[i][M - 1] != 0:
                    target.append((i, m))
                    target.append((i, M - 1))

                if disc[i][m] == disc[i][1] != 0:
                    target.append((i, m))
                    target.append((i, 1))

            elif m == M - 1: # M - 2, 0
                if disc[i][m] == disc[i][M - 2] != 0:
                    target.append((i, m))
                    target.append((i, M - 2))

                if disc[i][m] == disc[i][0] != 0:
                    target.append((i, m))
                    target.append((i, 0))

            else: # m - 1, m + 1
                if disc[i][m] == disc[i][m - 1] != 0:
                    target.append((i, m))
                    target.append((i, m - 1))

                if disc[i][m] == disc[i][m + 1] != 0:
                    target.append((i, m))
                    target.append((i, m + 1))

        # 인접한 원판의 인접한 수
        if i == 0: # 1
            for j in range(M):
                if disc[i][j] == disc[i + 1][j] != 0:
                    target.append((i, j))
                    target.append((i + 1, j))

        elif i == N - 1: # N - 2
            for j in range(M):
                if disc[i][j] == disc[N - 2][j] != 0:
                    target.append((i, j))
                    target.append((N - 2, j))

        else: # i - 1, i + 1
            for j in range(M):
                if disc[i][j] == disc[i - 1][j] != 0:
                    target.append((i, j))
                    target.append((i - 1, j))

                if disc[i][j] == disc[i + 1][j] != 0:
                    target.append((i, j))
                    target.append((i + 1, j))

    # target 에 들어있는 위치들을 0으로 바꿈
    target = deque(set(target)) # 중복 지워줌
    for x in target:
        target_x, target_y = x
        disc[target_x][target_y] = 0
    # print("target:", target)
    if not target: # 인접하면서 같은 수가 없는 경우
        average = get_average_disc() # 평균
        compare_vs_average(average)

    # 인접한 수가 같은게 없는 경우 -> 원판 위의 값들 평균 +/- 1 을 해줌
    else: # 수가 없으면 그냥 넘어감
        return

def get_average_disc():
    total = 0
    count = 0
    for i in range(N):
        for value in disc[i]:
            if value != 0:
                total += value
                count += 1

    average = total / count
    return average

def compare_vs_average(average):
    # print("평균 :", average)
    for i in range(N):
        for j in range(M):
            if disc[i][j] != 0:
                if disc[i][j] > average:
                    disc[i][j] -= 1
                elif disc[i][j] < average:
                    disc[i][j] += 1

def get_disc_total():
    total = 0
    for i in range(N):
        total += sum(disc[i])

    return total

import sys
input = sys.stdin.readline
from collections import deque

if __name__ == "__main__":
    N, M, T = map(int, input().split())
    disc = deque() # 원판

    for i in range(N): # i번째 원판
        disc_i = list(map(int, input().split())) # 12시가 마지막
        disc.append(deque(disc_i)) # deque형태로 넣음

    # print(disc)

    rotations = deque()
    for i in range(T): # 회전
        rotation = list(map(int, input().split()))
        rotations.append(deque(rotation))

    for i in range(T):
        xi, di, ki = rotations[i]

        # 배수에 있는 원판들을 회전
        rotate_disc(xi, di, ki)

        # 인접한 값 확인
        # find_adjacent_num(i)

    # print("final")
    # print(disc)
    total = get_disc_total()
    print(total)
