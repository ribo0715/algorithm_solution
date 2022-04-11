# 23290. 마법사 상어와 복제
import copy
from collections import deque
import sys
input = sys.stdin.readline

# 물고기들을 어떻게 관리할지 -> 각 위치마다 물고기들이 어떤 방향을 보고 있는지를 배열로 저장

# 상어 이동 -> 상 좌 하 우
def shark_move():
    global shark_x, shark_y

    q = deque()

    max_fish_num = -1

    for i in range(4): # 처음 4방향으로 이동
        next_x = shark_x + sx[i]
        next_y = shark_y + sy[i]

        if 0 <= next_x < 4 and 0 <= next_y < 4:
            fish_num = len(grid_after[next_x][next_y])
            q.append([i])

    for count in range(2): # 두번 더 이동
        for _ in range(len(q)):
            curr_q_list = q.popleft()

            curr_x, curr_y = shark_x, shark_y
            for k in range(len(curr_q_list)):
                curr_d = curr_q_list[k]
                curr_x = curr_x + sx[curr_d]
                curr_y = curr_y + sy[curr_d]

            for i in range(4): # 4방향으로 이동
                temp_q_list = copy.deepcopy(curr_q_list)
                next_x = curr_x + sx[i]
                next_y = curr_y + sy[i]

                if 0 <= next_x < 4 and 0 <= next_y < 4:
                    temp_q_list.append(i)
                    if count == 1: # 세번째 이동일 때
                        eating_fish_num = how_many_fish_shark_eat(temp_q_list)
                        if max_fish_num < eating_fish_num: # 지금까지 최대치보다 많은 경우, 업데이트하고 아래로 내려가 q에 넣어줌
                            max_fish_num = eating_fish_num
                        else: # 최대치보다 적은 경우, 넘어감
                            continue

                    q.append(temp_q_list)

    d1, d2, d3 = q.pop() # 가장 많이 물고기를 만난 경우의 이동
    d_list = [d1, d2, d3]
    shark_eat_fish(d_list) # 해당 이동으로 물고기를 처리


def how_many_fish_shark_eat(d_list):
    visited = [[0 for _ in range(4)] for _ in range(4)] # 방문표시
    visited[shark_x][shark_y] = 0

    next_x, next_y = shark_x, shark_y

    count = 0 # 만나서 제외시킬 물고기의 수
    for d in d_list:
        next_x = next_x + sx[d]
        next_y = next_y + sy[d]

        if len(grid_after[next_x][next_y]) >= 1 and visited[next_x][next_y] == 0: # 물고기가 있던 칸이라면
            count += len(grid_after[next_x][next_y])
            visited[next_x][next_y] = 1 # 방문표시

    return count


# 해당 이동 순서대로 이동을 할 때, 물고기를 없애고 냄새를 남김, 상어 현재 위치 변경
def shark_eat_fish(d_list):
    global shark_x, shark_y
    next_x, next_y = shark_x, shark_y

    for d in d_list:
        next_x = next_x + sx[d]
        next_y = next_y + sy[d]

        if len(grid_after[next_x][next_y]) >= 1: # 물고기가 있던 칸이라면
            grid_after[next_x][next_y] = [-1] # 물고기를 없애고, 냄새를 남김

    shark_x, shark_y = next_x, next_y


# 모든 격자의 냄새를 1 뺌
def smell_go_away():
    for x in range(4):
        for y in range(4):
            if grid[x][y][0] >= 1: # 냄새가 있는 경우
                grid[x][y][0] -= 1



# 상어 이동 방향 -> 상 좌 하 우
sx = [-1, 0, 1, 0]
sy = [0, -1, 0, 1]

# 모든 물고기 이동
def all_fishes_move():
    global grid_after

    # grid_after = copy.deepcopy(grid) # 이동한 물고기들을 추가로 저장
    grid_after = [[[] for _ in range(4)] for _ in range(4)] # 해당 위치로 이동한 물고기들을 담음
    for x in range(4):
        for y in range(4):
            if len(grid[x][y]) > 1: # 물고기가 존재하는 경우
                for i in range(1, len(grid[x][y])):
                    d = grid[x][y][i]
                    fish_move(x, y, d)


# 물고기들이 원래 있던 위치에 복제
def duplicate_fish():
    for x in range(4):
        for y in range(4):
            if grid_after[x][y]:
                if grid_after[x][y] == [-1]: # 냄새
                    grid[x][y][0] = 2
                else:
                    for d in grid_after[x][y]:
                        grid[x][y].append(d)


# (x, y)에서 방향이 d인 물고기 이동
def fish_move(x, y, d):
    next_x = x + dx[d]
    next_y = y + dy[d]

    if 0 <= next_x < 4 and 0 <= next_y < 4: # 구역 내
        if (shark_x, shark_y) == (next_x, next_y) or grid[next_x][next_y][0] >= 1: # 상어나 냄새가 있는 경우
            next_d = rotate_and_get_new_d(x, y, d) # 이동이 불가능한 경우, -1 반환

            if next_d == -1:
                grid_after[x][y].append(d)

            else:
                next_x = x + dx[next_d]
                next_y = y + dy[next_d]

                grid_after[next_x][next_y].append(next_d)

        else:
            grid_after[next_x][next_y].append(d)

    else: # 구역 밖
        next_d = rotate_and_get_new_d(x, y, d)

        if next_d == -1:
            grid_after[x][y].append(d)

        else:
            next_x = x + dx[next_d]
            next_y = y + dy[next_d]

            grid_after[next_x][next_y].append(next_d)


# (x, y)에서 d방향을 보고 있던 물고기를 방향을 돌려가며 이동방향을 찾음
def rotate_and_get_new_d(x, y, d):
    next_d = d
    for _ in range(7):
        next_d = (next_d - 1) % 8
        next_x = x + dx[next_d]
        next_y = y + dy[next_d]

        if 0 <= next_x < 4 and 0 <= next_y < 4: # 구역 내
            if (shark_x, shark_y) == (next_x, next_y) or grid[next_x][next_y][0] >= 1:  # 상어나 냄새가 있는 경우
                continue
            else:
                return next_d

    return -1 # 모든 방향으로 이동이 불가능한 경우


# 남은 물고기의 수 카운트
def count_total_fish_num():
    total_fish_num = 0
    for x in range(4):
        for y in range(4):
            total_fish_num += len(grid[x][y]) - 1

    return total_fish_num


# grid 상태 출력
def print_grid():
    for i in range(4):
        print(grid[i])

    print("grid_after")
    for i in range(4):
        print(grid_after[i])

    print("=============")

# ← ↖, ↑, ↗, →, ↘, ↓, ↙ 방향으로의 이동
# 반시계방향 : -1
dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

if __name__ == "__main__":
    M, S = map(int, input().split()) # 물고기 수, 마법 연습 횟수

    # 각 지점에는 상어, 물고기, 물고기 냄새 가 있을 수 있음
    grid = [[[0] for _ in range(4)] for _ in range(4)] # 각 지점에 물고기, 상어, 냄새를 담음
    # grid[x][y][0] -> 해당 지점의 물고기 냄새
    grid_after = copy.deepcopy(grid) # 이동 이후의 모습 -> 상어 이동 후, grid와 합쳐줘야함

    for i in range(M):
        fish_x, fish_y, d = map(int, input().split()) # 물고기 위치, 방향
        fish_x, fish_y, d = fish_x - 1, fish_y - 1, d - 1 # 입력값에서 1씩 줄여줌
        grid[fish_x][fish_y].append(d)

    shark_x, shark_y = map(int, input().split()) # 상어 위치
    shark_x, shark_y = shark_x - 1, shark_y - 1


    for _ in range(S): # S번 연습
        all_fishes_move() # 물고기들 이동

        shark_move() # 상어 이동

        smell_go_away() # 냄새 1 사라짐

        duplicate_fish() # 이동 전 물고기들의 위치에 복제

    print(count_total_fish_num())