# 23289. 온풍기 안녕!
import copy
from collections import deque
import sys
input = sys.stdin.readline

# 조사하는 칸이 모두 K 이상인지 검사
def check_over_K():
    for check_target in check_target_list:
        target_x, target_y = check_target

        if grid[target_x][target_y] < K:
            return False

    return True

# 벽을 어떻게 저장할지 -> 어느 지점과 어느 지점 사이의 벽


# 온풍기 바람의 이동을 어떻게 표현할지
def heater_on(x, y, d): # (x, y)에서 d방향으로 온풍기 킨 상황에서의 변화
    q = deque()
    q.append([x + dx[d], y + dy[d]])
    plus_heat = 5
    grid[x + dx[d]][y + dy[d]] += plus_heat
    visited = [[0 for _ in range(C)] for _ in range(R)]  # 방문 표시

    while q:
        plus_heat -= 1
        if plus_heat <= 0:
            return

        for _ in range(len(q)):
            curr_x, curr_y = q.popleft()

            # 앞쪽
            if d not in wall[curr_x][curr_y]:
                next_x = curr_x + dx[d]
                next_y = curr_y + dy[d]

                if 0 <= next_x < R and 0 <= next_y < C:
                    if visited[next_x][next_y] == 0:
                        q.append([next_x, next_y])
                        visited[next_x][next_y] = 1
                        grid[next_x][next_y] += plus_heat
                else: # 앞으로 더 진행되지 못하는 경우 끝
                    return

            # 오른쪽, 앞쪽
            if (d + 1) % 4 not in wall[curr_x][curr_y]: # 오른쪽으로 이동
                right_x = curr_x + dx[(d + 1) % 4]
                right_y = curr_y + dy[(d + 1) % 4]

                if 0 <= right_x < R and  0 <= right_y < C:
                    if visited[right_x][right_y] == 0:  # 해당 지점에서 이동을 이미 시도한 경우 넘어감
                        if d not in wall[right_x][right_y]: # 앞쪽으로 이동
                            next_x = right_x + dx[d]
                            next_y = right_y + dy[d]

                            if 0 <= next_x < R and  0 <= next_y < C:
                                if visited[next_x][next_y] == 0:
                                    q.append([next_x, next_y])
                                    visited[next_x][next_y] = 1
                                    grid[next_x][next_y] += plus_heat

            # 왼쪽, 앞쪽
            if (d - 1) % 4 not in wall[curr_x][curr_y]:  # 오른쪽으로 이동
                left_x = curr_x + dx[(d - 1) % 4]
                left_y = curr_y + dy[(d - 1) % 4]

                if 0 <= left_x < R and 0 <= left_y < C:
                    if visited[left_x][left_y] == 0:  # 해당 지점에서 이동을 이미 시도한 경우 넘어감
                        if d not in wall[left_x][left_y]:  # 앞쪽으로 이동
                            next_x = left_x + dx[d]
                            next_y = left_y + dy[d]

                            if 0 <= next_x < R and 0 <= next_y < C:
                                if visited[next_x][next_y] == 0:
                                    q.append([next_x, next_y])
                                    visited[next_x][next_y] = 1
                                    grid[next_x][next_y] += plus_heat

# 온도 조절
def control_temperature():
    global grid

    visited = [[0 for _ in range(C)] for _ in range(R)] # 방문 표시

    grid_after = copy.deepcopy(grid)
    # 모든 칸에 대해
    for x in range(R):
        for y in range(C):
            visited[x][y] = 1
            for i in range(4): # 4방향 확인
                temp_x = x + dx[i]
                temp_y = y + dy[i]

                if i not in wall[x][y]: # 해당 방향으로 벽이 없는 경우
                    if 0 <= temp_x < R and 0 <= temp_y < C:
                        if visited[temp_x][temp_y] == 0: # 해당 지점에서 이전에 확인하지 않은 경우
                            diff = abs(grid[x][y] - grid[temp_x][temp_y])

                            if grid[x][y] > grid[temp_x][temp_y]:
                                grid_after[x][y] -= diff // 4
                                grid_after[temp_x][temp_y] += diff // 4
                            else:
                                grid_after[x][y] += diff // 4
                                grid_after[temp_x][temp_y] -= diff // 4

    grid = grid_after



# 온도가 1 이상인 가장 바깥쪽 칸의 온도 1씩 감소
def decrease_outside_temperature():
    for y in range(C):
        if grid[0][y] >= 1:
            grid[0][y] -= 1

        if grid[R - 1][y] >= 1:
            grid[R - 1][y] -= 1

    for x in range(1, R - 1):
        if grid[x][0] >= 1:
            grid[x][0] -= 1

        if grid[x][C - 1] >= 1:
            grid[x][C - 1] -= 1


def test():
    chocolate = 0
    # print_grid()
    while not check_over_K(): # 조사하는 칸이 모두 K 이상 온도일 때 까지

        # print("#")
        if chocolate > 100:
            return 101

        for heater in heater_list: # 모든 온풍기에 대해
            heater_x, heater_y, heater_d = heater
            heater_on(heater_x, heater_y, heater_d) # 온풍기 바람 나옴

        control_temperature() # 온도 조절
        decrease_outside_temperature() # 바깥쪽 칸 온도 1 감소
        chocolate += 1
        # print_grid()

    return chocolate


# def print_grid():
#     print("grid")
#     for i in range(R):
#         print(grid[i])
#     print("================")


# 12시 3시 6시 9시 방향으로의 이동
# 오른쪽은 +1, 왼쪽은 -1
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

if __name__ == "__main__":
    R, C, K = map(int, input().split())

    grid = [[0 for _ in range(C)] for _ in range(R)] # 각 지점의 온도를 저장
    wall = [[[] for _ in range(C)] for _ in range(R)] # 각 지점에서 어떤 방향에 벽이 있는지 저장
    check_target_list = [] # 조사해야할 지점
    heater_list = [] # 온풍기 위치

    # 방의 정보 입력
    for x in range(R):
        line = list(map(int, input().split()))

        for y in range(C):
            if line[y] == 1: # 오른쪽
                heater_list.append([x, y, 1])
            elif line[y] == 2: # 왼쪽
                heater_list.append([x, y, 3])
            elif line[y] == 3: # 위쪽
                heater_list.append([x, y, 0])
            elif line[y] == 4: # 아래쪽
                heater_list.append([x, y, 2])
            elif line[y] == 5: # 온도 조사
                check_target_list.append([x, y])

    W = int(input()) # 벽의 개수
    for _ in range(W):
        x, y, t = map(int, input().split())
        x, y = x - 1, y - 1

        if t == 0: # (x - 1, y), (x, y) 사이에 벽
            wall[x][y].append(0)
            wall[x - 1][y].append(2)

        else: # (x, y), (x, y + 1) 사이에 벽
            wall[x][y].append(1)
            wall[x][y + 1].append(3)

    print(test())