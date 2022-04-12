# 21609. 상어 중학교

from collections import deque
import copy
import sys
input = sys.stdin.readline

# 가장 큰 그룹을 찾음 -> visited에 표시해가면서 크기를 확인해나감
def find_biggest_group_and_remove():
    global grid, score

    visited = [[0 for _ in range(N)] for _ in range(N)]

    max_group_count = 0
    max_group = deque()
    max_zero_count = 0

    for x in range(N):
        for y in range(N):
            if visited[x][y] == 1:
                continue

            group_num = grid[x][y]
            if group_num >= 1: # 일반 블록인 경우 -> 그룹 확인
                q = deque()
                q.append([x, y])

                index = 0
                zero_count = 0 # 그룹에 속한 무지개 블록의 수 -> 조건 확인 중요!

                while index < len(q):
                    curr_x, curr_y = q[index]

                    for i in range(4): # 상 하 좌 우 로 퍼져가면서 확인
                        next_x = curr_x + dx[i]
                        next_y = curr_y + dy[i]

                        if 0 <= next_x < N and 0 <= next_y < N:
                            if [next_x, next_y] not in q:
                                if grid[next_x][next_y] in [group_num, 0]:
                                    if grid[next_x][next_y] == group_num:
                                        visited[next_x][next_y] = 1
                                    else:
                                        zero_count += 1
                                    q.append([next_x, next_y])

                    index += 1
                group_count = len(q)

                if group_count > max_group_count: # 기준 블록의 행, 열이 가장 큰 것
                    max_group_count = group_count
                    max_group = q
                    max_zero_count = zero_count
                elif group_count == max_group_count:
                    if zero_count >= max_zero_count:
                        max_group_count = group_count
                        max_group = q
                        max_zero_count = zero_count

    # print(max_group)

    if max_group_count >= 2:
        while max_group:
            x, y = max_group.popleft()
            grid[x][y] = -2 # 빈칸

        score += max_group_count ** 2

        # print(max_group_count ** 2, "점이 추가되었습니다.")

# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 중력
def drop_down_by_gravity():
    global grid
    after_grid = [[-2 for _ in range(N)] for _ in range(N)]

    # 각 열에서 현재 최대로 내려갈 수 있는 지점
    limit = [N - 1 for _ in range(N)]

    for x in reversed(range(N)):
        for y in range(N):
            if grid[x][y] == -1: # 위치 고정
                after_grid[x][y] = -1
                limit[y] = x - 1

            elif grid[x][y] >= 0: # 비어있지 않은 경우
                after_grid[limit[y]][y]= grid[x][y]
                limit[y] -= 1

    grid = after_grid


# 반시계 방향으로 회전
def rotate_grid():
    global grid
    temp_grid = copy.deepcopy(grid)

    for x in range(N):
        for y in range(N):
            temp_grid[N - 1 - y][x] = grid[x][y]

    grid = temp_grid


# def print_grid():
#     print("===== grid =====")
#     for x in range(N):
#         print(grid[x])
#     print("================")

if __name__ == "__main__":
    N, M = map(int, input().split())

    score = 0 # 점수
    grid = []
    for _ in range(N):
        line = list(map(int, input().split()))
        grid.append(line)


    while True:
        curr_score = score
        # print("1")
        # print_grid()
        find_biggest_group_and_remove()
        # print("2")
        # print_grid()
        drop_down_by_gravity()
        # print("3")
        # print_grid()
        rotate_grid()
        # print("4")
        # print_grid()
        drop_down_by_gravity()
        # print("5")
        # print_grid()
        # print("현재까지", score, "점 입니다.")
        if score == curr_score:
            break

    print(score)