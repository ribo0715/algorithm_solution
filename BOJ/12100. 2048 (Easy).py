# 12100 : 2048 (Easy)


# 전체 블록을 상하좌우 네 방향 중 하나로 이동
# 두 블록이 충돌하면 두 블록은 하나로 합쳐짐


# 최대 5번 이동해서 만들 수 있는 가장 큰 블록의 값

from collections import deque


# 현재 보드판의 상태를 받아, 네 방향으로 수행
def bfs(board, n):
    q = deque()
    q.append(board)

    count = 0

    while True:
        count += 1

        for _ in range(len(q)):  # count 값이 나뉘는 기준
            board = q.popleft()

            # 네 방향으로 이동한 결과들을 다시 큐에 넣음
            q.append(merge_up(board, n))
            q.append(merge_down(board, n))
            q.append(merge_right(board, n))
            q.append(merge_left(board, n))

        if count == 5:  # 5회 이동이 끝난 후, 최대값을 확인
            temp_max = 0

            while q:
                board = q.popleft()

                temp = get_max(board, n)

                if temp_max < temp:
                    temp_max = temp

            print(temp_max)
            break


# 최대값을 찾아봄
def get_max(board, n):
    temp = 0

    for i in range(n):
        if temp < max(board[i]):
            temp = max(board[i])

    return temp


def merge_up(board, n):
    temp = [[] for _ in range(n)]  # merge하는 방향으로 값들을 담을 배열

    for i in range(n):
        for j in range(n):
            if board[j][i] != 0:  # 빈칸은 제외
                temp[i].append(board[j][i])

    # 연속되는 값이 같은 경우, 값을 합침
    for i in range(n):
        for j in range(n):
            if j > len(temp[i]) - 2:  # 해당 줄을 다 마친 경우
                break

            if temp[i][j] == temp[i][j + 1]:  # 연속된 두 값이 같은 경우
                temp[i][j] += temp[i][j + 1]  # 둘을 합친 뒤,
                del (temp[i][j + 1])  # 하나는 지워줌

    board = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(len(temp[i])):
            board[j][i] = temp[i][j]

    return board  # merge 후의 보드판을 반환


def merge_down(board, n):
    temp = [[] for _ in range(n)]  # merge하는 방향으로 값들을 담을 배열

    for i in range(n):
        for j in range(n):
            if board[n - 1 - j][i] != 0:  # 빈칸은 제외
                temp[i].append(board[n - 1 - j][i])

    # 연속되는 값이 같은 경우, 값을 합침
    for i in range(n):
        for j in range(n):
            if j > len(temp[i]) - 2:  # 해당 줄을 다 마친 경우
                break

            if temp[i][j] == temp[i][j + 1]:  # 연속된 두 값이 같은 경우
                temp[i][j] += temp[i][j + 1]  # 둘을 합친 뒤,
                del (temp[i][j + 1])  # 하나는 지워줌

    board = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(len(temp[i])):
            board[n - 1 - j][i] = temp[i][j]

    return board  # merge 후의 보드판을 반환


def merge_right(board, n):
    temp = [[] for _ in range(n)]  # merge하는 방향으로 값들을 담을 배열

    for i in range(n):
        for j in range(n):
            if board[i][n - 1 - j] != 0:  # 빈칸은 제외
                temp[i].append(board[i][n - 1 - j])

    # 연속되는 값이 같은 경우, 값을 합침
    for i in range(n):
        for j in range(n):
            if j > len(temp[i]) - 2:  # 해당 줄을 다 마친 경우
                break

            if temp[i][j] == temp[i][j + 1]:  # 연속된 두 값이 같은 경우
                temp[i][j] += temp[i][j + 1]  # 둘을 합친 뒤,
                del (temp[i][j + 1])  # 하나는 지워줌

    board = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(len(temp[i])):
            board[i][n - 1 - j] = temp[i][j]

    return board  # merge 후의 보드판을 반환


def merge_left(board, n):
    temp = [[] for _ in range(n)]  # merge하는 방향으로 값들을 담을 배열

    for i in range(n):
        for j in range(n):
            if board[i][j] != 0:  # 빈칸은 제외
                temp[i].append(board[i][j])

    # 연속되는 값이 같은 경우, 값을 합침
    for i in range(n):
        for j in range(n):
            if j > len(temp[i]) - 2:  # 해당 줄을 다 마친 경우
                break

            if temp[i][j] == temp[i][j + 1]:  # 연속된 두 값이 같은 경우
                temp[i][j] += temp[i][j + 1]  # 둘을 합친 뒤,
                del (temp[i][j + 1])  # 하나는 지워줌

    board = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(len(temp[i])):
            board[i][j] = temp[i][j]

    return board  # merge 후의 보드판을 반환


if __name__ == "__main__":

    # 첫째 줄에 보드의 크기 N (1 ≤ N ≤ 20)
    n = int(input())

    # 보드판의 블록 상태
    board = [[0] * n for _ in range(n)]

    # N개의 줄에는 게임판의 초기 상태
    for i in range(n):
        board[i] = list(map(int, input().split()))  # 띄어쓰기 단위로 나누어 저장

    bfs(board, n)
##    print(merge_down(board, n))

