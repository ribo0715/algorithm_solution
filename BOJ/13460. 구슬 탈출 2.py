# 13460 : 구슬 탈출 2


# 한번 움직일때, 상하좌우 4가지 경우
# -> 10번 이동 -> 4^10 = 100만가지 경우 -> 다 해봐도 될듯
# 한번씩 이동횟수를 늘려가며 검색 수행 -> bfs

# 해당 이동으로 빨간구슬이 빼내지는지
# 동시에 빠지지면 안됨
# 같은 칸에 위치할 수 없음

# 각 구슬의 위치를 변수에 저장해둬도 괜찮을듯

from collections import deque

# 상, 하, 좌, 우 로 이동
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]


def bfs(red_i, red_j, blue_i, blue_j):
    q = deque()
    q.append((red_i, red_j, blue_i, blue_j))  # 두 구슬의 위치정보를 큐에 담음

    count = 0  # 이동 횟수

    while q:
        count += 1
        for _ in range(len(q)):  # count 값이 나뉘는 기준
            red_i, red_j, blue_i, blue_j = q.popleft()

            for n in range(4):
                next_red_i, next_red_j, next_blue_i, next_blue_j = red_i, red_j, blue_i, blue_j

                while True:  # 빨간구슬 이동
                    next_red_i += di[n]
                    next_red_j += dj[n]

                    if board[next_red_i][next_red_j] == '#':
                        next_red_i -= di[n]
                        next_red_j -= dj[n]
                        break
                    elif board[next_red_i][next_red_j] == 'O':
                        break

                while True:  # 파란구슬 이동
                    next_blue_i += di[n]
                    next_blue_j += dj[n]

                    if board[next_blue_i][next_blue_j] == '#':
                        next_blue_i -= di[n]
                        next_blue_j -= dj[n]
                        break
                    elif board[next_blue_i][next_blue_j] == 'O':
                        break

                if board[next_blue_i][next_blue_j] == 'O':  # 파란구슬이 골인한 경우
                    continue  # 제외

                if board[next_red_i][next_red_j] == 'O':  # 빨간구슬만 골인한 경우
                    print(count)
                    return

                if (next_red_i, next_red_j) == (next_blue_i, next_blue_j):  # 벽에 닿은뒤 같은 곳에 위치한 경우
                    if abs(next_red_i - red_i) + abs(next_red_j - red_j) > abs(next_blue_i - blue_i) + abs(next_blue_j - blue_j):
                        next_red_i -= di[n]
                        next_red_j -= dj[n]
                    else:
                        next_blue_i -= di[n]
                        next_blue_j -= dj[n]

                q.append((next_red_i, next_red_j, next_blue_i, next_blue_j))

        if count >= 10:  # 10회 이동을 했음에도 끝나지 못한 경우
            print(-1)
            return


if __name__ == "__main__":
    board = []
    red_i, red_j = 0, 0  # 빨간 구슬의 위치
    blue_i, blue_j = 0, 0  # 파란 구슬의 위치

    # n, m 을 입력받음
    n, m = map(int, input().split())

    # 전체 board의 상태를 입력받음
    for i in range(n):
        line = input()
        board.append(line)

    # R, B의 위치를 변수에 담아 저장
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'R':
                red_i, red_j = i, j
            elif board[i][j] == 'B':
                blue_i, blue_j = i, j

    # 각 방향으로 움직여보며 확인
    bfs(red_i, red_j, blue_i, blue_j)

