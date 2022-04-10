# 23288. 주사위 굴리기 2

from collections import deque
import sys
input = sys.stdin.readline


# 주사위의 전개도
"""
주사위 전개도의 각 위치에 대한 dice배열에서의 index 
  1
3 0 2
  4
  5

초기 각 위치의 값
  2
4 1 3
  5
  6
"""

# 각 방향으로의 이동에 따른 전개도 변화 -> 아래방향, 오른쪽방향으로의 이동
def move_right():
    temp = dice[0]
    dice[0] = dice[3]
    dice[3] = dice[5]
    dice[5] = dice[2]
    dice[2] = temp

def move_left():
    for _ in range(3):
        move_right()

def move_up():
    temp = dice[0]
    dice[0] = dice[4]
    dice[4] = dice[5]
    dice[5] = dice[1]
    dice[1] = temp

def move_down():
    for _ in range(3):
        move_up()


# (x, y) 칸과 같은 값을 갖는 인접한 칸 수를 구함 -> 해당 칸에서의 점수
def get_score(x, y):
    # print("x, y =", x, y)
    target_value = grid[x][y] # 현재 주사위가 있는 칸의 수
    q = deque()
    q.append([x, y])

    visited = [[0 for _ in range(M)] for _ in range(N)] # 방문한 위치 1로 표시
    visited[x][y] = 1
    count = 1

    while q:
        curr_x, curr_y = q.popleft()

        for i in range(4): # 네 방향으로 확인
            next_x = curr_x + dx[i]
            next_y = curr_y + dy[i]

            if 0 <= next_x < N and 0 <= next_y < M:
                if visited[next_x][next_y] == 0:
                    if grid[next_x][next_y] == target_value:
                        # print("(", next_x, ",", next_y, ") 방문")
                        q.append([next_x, next_y]) # q에 넣어줌
                        visited[next_x][next_y] = 1 # 방문표시
                        count += 1

    # print("(x, y) : (", x, ",", y, ") target_value :", target_value, "count :", count)
    score = target_value * count

    return score


# 도착한 칸의 값과 주사위의 아랫면의 값을 비교하여 방향 결정
def move_dice():
    global d, dice_x, dice_y

    next_dice_x = dice_x + dx[d]
    next_dice_y = dice_y + dy[d]

    # 이동 방향에 칸이 없는 경우 방향을 반대로 함
    if next_dice_x < 0 or N <= next_dice_x or next_dice_y < 0 or M <= next_dice_y:
        d = (d + 2) % 4

    if d == 0:
        move_up()
    elif d == 1:
        move_right()
    elif d == 2:
        move_down()
    else:
        move_left()

    dice_x += dx[d]
    dice_y += dy[d]


def set_direction():
    global d

    A = dice[-1]
    B = grid[dice_x][dice_y]

    if A > B:
        d = (d + 1) % 4
    elif A < B:
        d = (d - 1) % 4


# 12시 3시 6시 9시 방향으로의 이동
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

if __name__ == "__main__":
    dice = [1, 2, 3, 4, 5, 6] # 시작할 때 주사위 전개도의 상태
    N, M, K = map(int, input().split())

    grid = []

    for _ in range(N):
        line = list(map(int, input().split()))
        grid.append(line)

    d = 1 # 초기 방향 : 3시 방향
    dice_x, dice_y = 0, 0 # 주사위 시작위치 (0, 0)
    total_score = 0

    for _ in range(K):
        move_dice()
        total_score += get_score(dice_x, dice_y)
        # print(get_score(dice_x, dice_y))
        set_direction()

    print(total_score)