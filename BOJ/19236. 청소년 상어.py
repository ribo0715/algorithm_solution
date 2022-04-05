# 19236. 청소년 상어

"""
4×4크기의 공간
한 칸에는 물고기가 한 마리 존재
각 물고기는 번호와 방향을 가지고 있다

번호는 1보다 크거나 같고, 16보다 작거나 같은 자연수
방향은 8가지 방향(상하좌우, 대각선) -> 1~8

청소년 상어는 (0, 0)에 있는 물고기를 먹고, (0, 0)에 들어가게 된다
상어의 방향은 (0, 0)에 있던 물고기의 방향과 같다

물고기는 번호가 작은 물고기부터 순서대로 이동
이동할 수 있는 칸은 빈 칸과 다른 물고기가 있는 칸
이동할 수 없는 칸은 상어가 있거나, 공간의 경계를 넘는 칸

각 물고기는 방향이 이동할 수 있는 칸을 향할 때까지 방향을 45도 반시계 회전
물고기가 다른 물고기가 있는 칸으로 이동할 때는 서로의 위치를 바꾸는 방식으로 이동

물고기의 이동이 모두 끝나면 상어가 이동
상어는 방향에 있는 칸으로 이동할 수 있는데, 한 번에 여러 개의 칸을 이동할 수 있다

상어가 물고기가 있는 칸으로 이동했다면, 그 칸에 있는 물고기를 먹고, 그 물고기의 방향을 가지게 된다

상어가 먹을 수 있는 물고기 번호의 합의 최댓값을 구해보자
-> 상어가 먹을 수 있는 물고기의 경우들에 대해 모두 수행해 나가야할 듯
"""

# 상어가 먹잇감을 찾음 -> 가능한 (target_x, target_y) 쌍을 모두 반환



def shark_find_fish(grid, shark_x, shark_y, shark_direction):
    target_case = []
    i = 1
    while True:
        target_x = shark_x + dx[shark_direction] * i
        target_y = shark_y + dy[shark_direction] * i

        if 0 <= target_x < 4 and 0 <= target_y < 4:
            if grid[target_x][target_y] != 0: # 빈칸이 아닌 경우
                target_case.append((target_x, target_y))
        else: # 경계 밖까지 도달 -> 끝
            break

        i += 1

    return target_case


# 상어가 먹잇감을 먹음
def shark_catch_fish(grid, fish_list, shark_x, shark_y, target_x, target_y, total_point):
    target_fish_num = grid[target_x][target_y]
    shark_direction = fish_list[target_fish_num][1]
    fish_list[target_fish_num] = [(-1, -1), 0]
    grid[shark_x][shark_y] = 0
    grid[target_x][target_y] = -1 # 상어가 이동
    total_point += target_fish_num

    # print(target_fish_num, "번호의 물고기를 먹음!")

    shark_x, shark_y = target_x, target_y
    # print(target_x, target_y, "에 있는 물고기를 먹었다!!")
    return shark_x, shark_y, shark_direction, total_point



# 1번부터 모든 물고기 이동
def all_fishes_move(grid, fish_list):
    # print("물고기 모두 이동하기 전")
    # for i in range(4):
    #     print(grid[i])
    # print()
    for fish_num in range(1, 17): # 1번~16번 순서대로
        (fish_x, fish_y) = fish_list[fish_num][0]
        fish_direction = fish_list[fish_num][1]
        # print(fish_num, "번 물고기 위치 :",fish_x, ",", fish_y)
        if (fish_x, fish_y) == (-1, -1): # 해당 번호의 물고기가 없는 경우
            continue

        fish_move(grid, fish_list, fish_x, fish_y, fish_direction)

        # for i in range(4):
        #     print(grid[i])
    # print("물고기 모두 이동한 후")
    # for i in range(4):
    #     print(grid[i])
    # print()

def fish_move(grid, fish_list, fish_x, fish_y, fish_direction):
    # 해당 물고기의 방향 확인
    target_x = fish_x + dx[fish_direction]
    target_y = fish_y + dy[fish_direction]

    turn = False
    if 0 <= target_x < 4 and 0 <= target_y < 4: # 공간의 경계 안
        if grid[target_x][target_y] != -1: # 상어가 있는 칸이 아닌 경우
            exchange_location(grid, fish_list, fish_x, fish_y, target_x, target_y) # 해당 위치와 바꿔줌

        else: # 상어가 있는 칸
            turn = True
    else: # 경계 밖으로의 이동 -> 45도 반시계 회전 -> fish_direction % 8 + 1
        turn = True

    if turn: # 회전이 필요한 경우
        turn_direction = fish_direction
        for n in range(1, 8): # n번 회전
            turn_direction = turn_direction % 8 + 1
            target_x = fish_x + dx[turn_direction]
            target_y = fish_y + dy[turn_direction]

            if 0 <= target_x < 4 and 0 <= target_y < 4:  # 공간의 경계 안
                if grid[target_x][target_y] != -1:  # 상어가 있는 칸이 아닌 경우
                    fish_num = grid[fish_x][fish_y]
                    fish_list[fish_num][1] = turn_direction # 현재 물고기의 방향을 바꿔줌

                    exchange_location(grid, fish_list, fish_x, fish_y, target_x, target_y)  # 해당 위치와 바꿔줌
                    break


def exchange_location(grid, fish_list, fish_x, fish_y, target_x, target_y):
    fish_num = grid[fish_x][fish_y]
    fish_direction = fish_list[fish_num][1]
    target_num = grid[target_x][target_y] # 빈칸인 경우, 0
    target_direction = fish_list[target_num][1] # 빈칸인 경우, 0

    fish_list[fish_num][0] = (target_x, target_y)
    fish_list[target_num][0] = (fish_x, fish_y)

    grid[fish_x][fish_y] = target_num
    grid[target_x][target_y] = fish_num
    # fish_list[fish_num][1] = target_direction
    # fish_list[target_num][1] = fish_direction


# fish_direction값에 따라 이동할 방향 1~8
#        ↑, ↖, ←, ↙, ↓, ↘, →, ↗
dx = [0, -1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 0, -1, -1, -1, 0, 1, 1, 1]

import sys
input = sys.stdin.readline
from collections import deque
import copy

if __name__ == "__main__":
    grid = [ [0 for _ in range(4) ] for _ in range(4) ] # 해당 위치에 있는 물고기 번호 저장
    fish_list = [ [] for _ in range(17)] # fish_list[i] -> i번 물고기의 위치, 방향 저장
    fish_list[0] = [(-1, -1), 0]
    for x in range(4):
        line = list(map(int, input().split()))
        for y in range(4):
            fish_num, fish_direction = line[2 * y], line[2 * y + 1]
            grid[x][y] = fish_num
            # 각 물고기 번호
            fish_list[fish_num] = [(x, y), fish_direction]

    # for i in range(4):
    #     print(grid[i])
    # 0점 상태에서 상어가 (0, 0)에 있는 물고기를 먹으며 (0, 0)에 들어감
    shark_x, shark_y, shark_direction, total_point = shark_catch_fish(grid, fish_list, 0, 0, 0, 0, 0)

    # all_fishes_move(grid, fish_list)
    # target_case = shark_find_fish(grid, shark_x, shark_y, shark_direction)

    score_q = deque() # 끝날때까지의 점수들 저장
    q = deque() # grid, fish_list, shark_x, shark_y, shark_direction, total_point 를 담음
    q.append([grid, fish_list, shark_x, shark_y, shark_direction, total_point])
    while q:
        temp = q.popleft()
        temp_grid = copy.deepcopy(temp[0])
        temp_fish_list = copy.deepcopy(temp[1])
        temp_shark_x, temp_shark_y, temp_shark_direction, temp_total_point = temp[2], temp[3], temp[4], temp[5]
        # print("이번 턴 상어 위치 temp_shark_x", temp_shark_x, temp_shark_y)
        # print("이번 턴 temp_fish_list :", temp_fish_list)
        # print("물고기들 이동 시작")
        # for i in range(4):
        #     print(temp_grid[i])
        # print()
        all_fishes_move(temp_grid, temp_fish_list) # 물고기들 이동
        # print("물고기들 이동 끝")
        # for i in range(4):
        #     print(temp_grid[i])
        # print()
        target_case = shark_find_fish(temp_grid, temp_shark_x, temp_shark_y, temp_shark_direction) # 먹을 물고기 찾음

        if not target_case: # 먹이를 찾지 못한 경우
            # print("먹이를 찾지 못함!")
            # for i in range(4):
            #     print(temp_grid[i])
            # print("현재까지 먹은 물고기 번호의 합 :", temp_total_point)

            score_q.append(temp_total_point)

        # print("상어가 먹을 수 있는 target_case", target_case)
        for (target_x, target_y) in target_case:
            # print("상어가 먹을 물고기 위치 :", target_x, ",", target_y)
            ttemp_grid = copy.deepcopy(temp_grid)
            ttemp_fish_list = copy.deepcopy(temp_fish_list)
            ttemp_shark_x, ttemp_shark_y, ttemp_total_point = temp_shark_x, temp_shark_y, temp_total_point
            next_shark_x, next_shark_y, next_shark_direction, next_total_point = shark_catch_fish(ttemp_grid, ttemp_fish_list, ttemp_shark_x, ttemp_shark_y, target_x, target_y, ttemp_total_point)
            q.append([ttemp_grid, ttemp_fish_list, next_shark_x, next_shark_y, next_shark_direction, next_total_point])
            # print("ttemp_fish_list", ttemp_fish_list)
            # print("현재까지 상어가 먹은 물고기 번호 합 :", next_total_point)

    # print(score_q)
    print(max(score_q))



