# 19237. 어른 상어


# 각 지점에 담겨야할 정보 -> 누구의 냄새인지 몇초 남았는지

# 각 상어들의 정보 -> 현재 위치, 방향



# 모든 상어 이동
def all_sharks_move():
    reduce_smell() # 냄새 지속시간 줄임

    spread_smell() # 각 상어들이 현재 위치에 냄새를 뿌림

    for n in shark_q:
    # for n in range(1, M + 1): # 모든 상어들 이동
        shark_move(n)

    check_overlap_shark() # 겹치는 상어가 있는지 확인
    # print("shark_q :", shark_q)

# 전체 냄새 지속시간을 -1 해줌
def reduce_smell():
    for x in range(N):
        for y in range(N):
            if grid[x][y] != [0, 0]:
                grid[x][y][1] = grid[x][y][1] - 1
                if grid[x][y][1] == 0: # 냄새가 사라지는 경우
                    grid[x][y] = [0, 0] # (0, 0)으로 해줌


def check_overlap_shark():
    temp_grid = [ [0 for _ in range(N)] for _ in range(N) ] # 해당 위치에서 가장 작은 번호만 있도록 함
    i = 0
    while i != len(shark_q):
        n = shark_q[i]
    # for n in range(1, M + 1):
        shark_x, shark_y = shark_list[n][0], shark_list[n][1]

        # if [shark_x, shark_y] == [-1, -1]: # 쫓겨난 상어는 넘어감
        #     continue

        if temp_grid[shark_x][shark_y] == 0: # 상어가 아직 해당 위치에 없는 경우
            temp_grid[shark_x][shark_y] = n
            i += 1
        elif temp_grid[shark_x][shark_y] > n: # 더 큰 번호의 상어가 있는 경우, 쫓아냄
            target_num = temp_grid[shark_x][shark_y]
            # shark_list[target_num] = [-1, -1, -1]
            shark_q.remove(target_num)
            # print("target_num 제거,", target_num)

            temp_grid[shark_x][shark_y] = n
        else: # 더 작은 번호의 상어가 있는 경우, 쫓겨남
            # shark_list[n] = [-1, -1, -1]
            shark_q.remove(n)
            # print("target_num 제거,", n)


# n번째 상어 이동
def shark_move(n):
    # if shark_list[n] == [-1, -1, -1]: # 쫓겨난 상어인 경우 끝
    #     return

    shark_x, shark_y, shark_direction = shark_list[n] # n번 상어의 현재 위치, 방향

    for next_direction in priority[n][shark_direction]: # 현재 방향에 대한 우선순위에 따라 이동
        next_x = shark_x + dx[next_direction]
        next_y = shark_y + dy[next_direction]

        if 0 <= next_x < N and 0 <= next_y < N:
            if grid[next_x][next_y] == [0, 0]: # 해당 위치에 이동할 수 있으면 이동(아무 냄새가 없는 칸)
                shark_list[n] = next_x, next_y, next_direction
                return

    for next_direction in priority[n][shark_direction]:
        next_x = shark_x + dx[next_direction]
        next_y = shark_y + dy[next_direction]

        if 0 <= next_x < N and 0 <= next_y < N:
            if grid[next_x][next_y][0] == n: # 자신의 냄새가 있는 칸으로 이동
                shark_list[n] = next_x, next_y, next_direction
                return


# direction 값에 따른 위치 이동 : 위, 아래, 왼쪽, 오른쪽
dx = [0, -1, 1, 0, 0]
dy = [0, 0, 0, -1, 1]

# 현재 상어들의 위치에 냄새를 뿌림
def spread_smell():
    for n in shark_q:
    # for n in range(1, M + 1):
        shark_x, shark_y = shark_list[n][0], shark_list[n][1]

        # if [shark_x, shark_y] == [-1, -1]: # 상어가 쫓겨나면 shark_list[k] 를 (-1, -1, -1)로 바꿔줌
        #     continue

        grid[shark_x][shark_y] = [n, k] # n번 상어의 냄새, k의 지속시간




# 1번 상어만 남았는지 확인
def check_only_one():
    # print(shark_q)
    if len(shark_q) == 1 and shark_q[0] == 1:
        return True
    else:
        return False

    # if shark_list[1] == [-1, -1, -1]: # 1번 상어도 없으면 False
    #     return False
    #
    # for n in range(2, M + 1):
    #     if shark_list[n] != [-1, -1, -1]: # 다른 상어가 존재하면 False
    #         return False
    #
    # return True # 1번 상어만 있는 경우 True


import sys
input = sys.stdin.readline
from collections import deque



if __name__ == "__main__":
    N, M, k = map(int, input().split())

    grid = [ [ [0, 0] for _ in range(N)] for _ in range(N) ] # grid[i][j] : (i, j)에 있는 [냄새의 주인, 남은 시간]
    shark_list = [[] for _ in range(M + 1)] # shark_list[i] : [shark_x, shark_y, shark_direction]

    # 현재 남아있는 상어들에 대한 정보를 저장할까? -> deque에 현재 남아있는 상어의 번호를 저장
    shark_q = deque()

    for i in range(N): # 격자의 모습
        line = list(map(int, input().split()))

        for j in range(N):
            if line[j] != 0: # 상어가 위치
                shark_num = line[j]
                shark_list[shark_num] = [i, j]
                shark_q.append(shark_num)

    # print(shark_q)

    shark_direction = [0] + list(map(int, input().split())) # 각 상어의 방향을 담을 배열 -> shark_direction[i] : i번 상어의 방향
    for shark_num in range(1, M + 1):
        shark_list[shark_num].append(shark_direction[shark_num])

    priority = [ [ [] for _ in range(5) ] for _ in range(M + 1) ] # priority[i] : i번 상어의 우선순위
    for i in range(1, M + 1): # 각 상어의 방향 우선순위
        for j in range(1, 5): # 상어 당 4줄씩 -> 현재 방향에 따른 우선순위
            priority[i][j] = list(map(int, input().split())) # priority[i][j] : i번 상어가 j방향일 때의 우선순위

    # print("grid")
    # for i in range(N):
    #     print(grid[i])
    # for _ in range(27):

    time = 0
    # for _ in range(14):
    while not check_only_one():
        if time >= 1000: # 1000초가 넘는 경우 -1 출력
            print(-1)
            exit()

        all_sharks_move()
        time += 1

        # print("grid")
        # for i in range(N):
        #     print(grid[i])

    print(time)

