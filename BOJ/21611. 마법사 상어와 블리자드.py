# 21611. 마법사 상어와 블리자드

import sys
input = sys.stdin.readline
from collections import deque

# 12시 3시 6시 9시 로의 이동 -> 왼쪽으로 회전하면서 이동할때 사용
dx_1 = [-1, 0, 1, 0]
dy_1 = [0, 1, 0, -1]


# 상 하 좌 우 방향 -> 마법의 방향
dx = [0] + [-1, 1, 0, 0]
dy = [0] + [0, 0, -1, 1]


# d방향, s거리만큼 마법 -> 해당 위치의 구슬들을 파괴 -> 자동으로 당겨짐
def blizard_magic(d, s):
    shark_x, shark_y = N // 2, N // 2
    count = 0 # 구슬을 파괴한 수 -> 파괴한 뒷 번호의 구슬에선 count만큼 땡겨서 확인해야함
    for i in range(s): # 거리만큼
        target_x = shark_x + dx[d] * (i + 1)
        target_y = shark_y + dy[d] * (i + 1)

        target_index = grid_index[target_x][target_y] - count

        if target_index < len(marble_q): # 해당 위치에 구슬이 놓여있는 경우
            # print(marble_q[target_index], "파괴")
            del marble_q[target_index] # 파괴

        count += 1

# 4개 이상 연속하는 구슬 폭발
def explode_and_change():
    global marble_q

    flag = True

    # print("폭발 함수 내")
    while flag:
        flag = False
        new_marble_q = deque() # 새로운 구슬

        prev_num = marble_q[0] # 이전에 확인한 구슬의 번호
        start_index = 0 # 번호가 연속되는 구슬 그룹의 시작 index
        count = 1
        curr_index = 1 # 확인할 index -> 처음부터 확인

        while True: # 끝에 도달할 때까지

            if curr_index == len(marble_q): # 마지막에 도달했을때
                if count > 4: # 길이가 4 이상인 경우 -> 지워줌
                    flag = True
                    exploded_marbles[prev_num] += count # 폭발한 구슬 개수 추가
                    for _ in range(count):
                        del marble_q[start_index]
                else:
                    new_marble_q.append(count)
                    new_marble_q.append(prev_num)
                break

            curr_num = marble_q[curr_index]
            if curr_num == prev_num: # 번호가 연속되는 경우
                count += 1
                curr_index += 1
            else: # 번호 연속이 끝난 경우
                if count >= 4: # 이전에 4번 이상 연속된 경우
                    flag = True
                    exploded_marbles[prev_num] += count # 폭발한 구슬 개수 추가
                    for _ in range(count):
                        del marble_q[start_index] # 연속된 구슬을 없애줌
                    curr_index = start_index + 1
                else: # 연속된게 끝났지만, 폭발하지 않은 경우 -> 변화
                    new_marble_q.append(count) # 이전 그룹의 개수
                    new_marble_q.append(prev_num) # 이전 그룹의 번호 로 변화

                    start_index = curr_index
                    curr_index += 1

                count = 1
                prev_num = curr_num

        if len(new_marble_q) >= N ** 2: # 길이를 넘어가는 경우 없앰
            over_count = len(new_marble_q) - N ** 2 + 1
            for _ in range(over_count):
                new_marble_q.pop()

        # print(marble_q)
    marble_q = new_marble_q


    # print("함수 끝")

def calc_result():
    result = 0
    for i in range(1,4):
        result += exploded_marbles[i] * i

    return result

if __name__ == "__main__":
    N, M = map(int, input().split())

    grid = []
    for i in range(N): # 구슬의 정보
        line = list(map(int, input().split()))
        grid.append(line)

    marble_q = deque() # 순서대로 구슬의 번호를 담음
    grid_index = [[-1 for _ in range(N)] for _ in range(N)] # 각 지점이 marble_q에서 몇번째 index 위치인지 -> 상어의 위치는 -1

    visited = [[0 for _ in range(N)] for _ in range(N)]
    curr_x, curr_y = N // 2, N // 2 # 상어 위치에서 시작
    d = 3 # 처음 시작할 때 왼쪽으로 이동
    count = 0
    while (curr_x, curr_y) != (0, 0): # grid를 길을 따라 돌며, grid_index 각 지점에 번호를 붙임
        visited[curr_x][curr_y] = 1
        curr_x = curr_x + dx_1[d]
        curr_y = curr_y + dy_1[d]

        grid_index[curr_x][curr_y] = count

        if grid[curr_x][curr_y] != 0:
            marble_q.append(grid[curr_x][curr_y]) # 구슬을 순서대로 담음

        if visited[curr_x + dx_1[(d - 1) % 4]][curr_y + dy_1[(d - 1) % 4]] == 0: # 왼쪽으로 꺽을 수 있으면 꺽음
            d = (d - 1) % 4

        count += 1




    # for i in range(N):
    #     print(grid_index[i])

    exploded_marbles = [0, 0, 0, 0] # [i] -> 폭발한 i번 구슬 개수
    # print(marble_q)
    # print("================")
    for _ in range(M): # 마법
        if not marble_q:
            break

        d, s = map(int, input().split()) # 방향, 거리

        blizard_magic(d, s)
        # print(marble_q)
        explode_and_change()

        # print(marble_q)
        # print("================")

    print(calc_result())