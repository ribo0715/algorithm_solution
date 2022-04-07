# 20057. 마법사 상어와 토네이도

import sys
input = sys.stdin.readline

# 토네이도가 (tornado_x, tornado_y)에서 i방향으로 이동할 때 모래 흩날리는 함수
def spread_sand(i):
    global tornado_x, tornado_y

    next_tornado_x = tornado_x + dx[i]
    next_tornado_y = tornado_y + dy[i]

    sand = A[next_tornado_x][next_tornado_y] # 흩날리게 될 모래의 양

    put_sand(next_tornado_x + dx[i] * 2, next_tornado_y + dy[i] * 2, int(sand * 0.05))

    put_sand(next_tornado_x + dx[i] + dx[(i + 1) % 4], next_tornado_y + dy[i] + dy[(i + 1) % 4], int(sand * 0.1))
    put_sand(next_tornado_x + dx[i] + dx[(i - 1) % 4], next_tornado_y + dy[i] + dy[(i - 1) % 4], int(sand * 0.1))

    put_sand(next_tornado_x + dx[(i + 1) % 4], next_tornado_y + dy[(i + 1) % 4], int(sand * 0.07))
    put_sand(next_tornado_x + dx[(i - 1) % 4], next_tornado_y + dy[(i - 1) % 4], int(sand * 0.07))

    put_sand(next_tornado_x + dx[(i + 1) % 4] * 2, next_tornado_y + dy[(i + 1) % 4] * 2, int(sand * 0.02))
    put_sand(next_tornado_x + dx[(i - 1) % 4] * 2, next_tornado_y + dy[(i - 1) % 4] * 2, int(sand * 0.02))

    put_sand(next_tornado_x + dx[(i + 1) % 4] + dx[(i + 2) % 4], next_tornado_y + dy[(i + 1) % 4] + dy[(i + 2) % 4], int(sand * 0.01))
    put_sand(next_tornado_x + dx[(i - 1) % 4] + dx[(i + 2) % 4], next_tornado_y + dy[(i - 1) % 4] + dy[(i + 2) % 4], int(sand * 0.01))

    a = sand - (int(sand * 0.05) + 2 * int(sand * 0.1) + 2 * int(sand * 0.07) + 2 * int(sand * 0.02) + 2 * int(sand * 0.01))
    # a = int(sand * 0.55)
    put_sand(next_tornado_x + dx[i], next_tornado_y + dy[i], a)

    tornado_x = next_tornado_x
    tornado_y = next_tornado_y
    A[tornado_x][tornado_y] = 0


# (target_x, target_y)에 sand만큼의 모래를 놓음 -> 격자 밖으로 나가는 경우 sand_out에 더해줌
def put_sand(target_x, target_y, sand):
    global sand_out

    if 0 <= target_x < N and 0 <= target_y < N:
        A[target_x][target_y] += sand
    else:
        sand_out += sand


# 토네이도가 반시계방향으로 이동
def move_tornado():
    global tornado_x, tornado_y

    i = 3 # 처음에 왼쪽으로 이동

    visited = [[0 for _ in range(N)] for _ in range(N)] # 방문확인
    # print_A()
    while (tornado_x, tornado_y) != (0, 0):
        visited[tornado_x][tornado_y] = 1
        spread_sand(i) # i 방향으로 이동

        # print_A()
        # 왼쪽으로 꺽을 수 있으면 꺽음, 아니면 직진
        if visited[tornado_x + dx[(i - 1) % 4]][tornado_y + dy[(i - 1) % 4]] == 0:
            i = (i - 1) % 4 # 왼쪽으로 꺽음


# def print_A():
#     for i in range(N):
#         print(A[i])
#     print("==================")

# 해당 방향 기준 오른쪽(+1), 왼쪽(-1), 뒤(+2)
# 12시 3시 6시 9시 방향으로 이동
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

if __name__ == "__main__":
    N = int(input())
    sand_out = 0 # 격자 밖으로 나가는 모래의 양

    A = [] # 각 지점에 있는 모래의 양
    for _ in range(N):
        line = list(map(int, input().split()))
        A.append(line)

    tornado_x, tornado_y = N // 2, N // 2 # 격자의 중앙에서 시작

    move_tornado()

    print(sand_out)


