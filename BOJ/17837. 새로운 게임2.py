# 17837. 새로운 게임2
"""
말은 원판모양
하나의 말 위에 다른 말을 올릴 수 있다

체스판의 각 칸은 흰색, 빨간색, 파란색 중 하나로 색칠

말은 1번부터 K번까지 번호가 매겨져 있고, 이동 방향도 미리 정해져 있다 ->  위, 아래, 왼쪽, 오른쪽

턴 한 번은 1번 말부터 K번 말까지 순서대로 이동시키는 것
한 말이 이동할 때 위에 올려져 있는 말도 함께 이동

말의 이동 방향에 있는 칸에 따라서 말의 이동이 다름

턴이 진행되던 중에 말이 4개 이상 쌓이는 순간 게임이 종료

흰색인 경우
그 칸으로 이동
이동하려는 칸에 말이 이미 있는 경우에는 가장 위에 A번 말을 올려놓는다
A번 말의 위에 다른 말이 있는 경우에는 A번 말과 위에 있는 모든 말이 이동

빨간색인 경우
이동한 후에 A번 말과 그 위에 있는 모든 말의 쌓여있는 순서를 반대로 바꾼다
A, B, C가 이동하고, 이동하려는 칸에 말이 없는 경우에는 C, B, A가 된다

파란색인 경우
A번 말의 이동 방향을 반대로 하고 한 칸 이동
방향을 반대로 바꾼 후에 이동하려는 칸이 파란색인 경우에는 이동하지 않고 가만히 있는다

체스판을 벗어나는 경우에는 파란색과 같은 경우

게임이 종료되는 턴의 번호 구하기
그 값이 1,000보다 크거나 절대로 게임이 종료되지 않는 경우에는 -1을 출력
"""

# 각 위치에 놓여있는 말들을 표시

# i번째 말을 curr_x, curr_y -> next_x, next_y 로 이동
# 해당 말 위의 것들도 옮김, reverse = 1 이면 반대로 뒤집어서
def move_top(i, curr_x, curr_y, next_x, next_y, reverse):
    index = piece_top[curr_x][curr_y].index(i)
    # index 번째 이후로 다 이동
    count = len(piece_top[curr_x][curr_y]) - index
    # print("index :",index)
    # print("count :", count)
    for _ in range(count):
        target = 0
        if reverse: # 거꾸로 뒤집어 이동 -> 맨 위에서 부터 뺌
            target = piece_top[curr_x][curr_y].pop(-1)
        else: # index번째부터 끝까지 뺌
            target = piece_top[curr_x][curr_y].pop(index)

        piece_top[next_x][next_y].append(target)
        piece[target][0], piece[target][1] = next_x, next_y

# i 번호에 대해 해당 말을 찾아 이동하도록 하는 함수
def move_piece(i):
    # 해당 번호의 위치 확인
    # print("i :", i)
    curr_x, curr_y = piece[i][0], piece[i][1]

    # 방향과 이동하려는 칸 확인
    next_x = curr_x + dx[piece[i][2]]
    next_y = curr_y + dy[piece[i][2]]
    # print(i, "번쨰 : ", curr_x, curr_y, "->", next_x, next_y)
    # if 0 <= next_x < N and 0 <= next_y < N:

    if 0 <= next_x < N and 0 <= next_y < N and grid[next_x][next_y] == 0: # 흰
        # i번 말 위에 있는 말 모두 그대로 이동
        # print("흰색으로 이동")
        move_top(i, curr_x, curr_y, next_x, next_y, False)

    elif 0 <= next_x < N and 0 <= next_y < N and grid[next_x][next_y] == 1: # 빨
        # i번 말 위에 있는 말 순서를 뒤집어 이동
        # print("빨간색으로 이동")
        move_top(i, curr_x, curr_y, next_x, next_y, True)

    else: # 파 or 벗어나는 경우
        # 방향 반대로 한칸 이동, 파란색인 경우 가만히
        # print("파란색으로 이동 or 밖으로 벗어남")
        # 반대 방향으로 바꿔줌
        if piece[i][2] % 2 == 1: # 홀수 -> -1
            piece[i][2] -= 1
        else:
            piece[i][2] += 1

        next_x = curr_x + dx[piece[i][2]]
        next_y = curr_y + dy[piece[i][2]]

        if 0 <= next_x < N and 0 <= next_y < N and grid[next_x][next_y] == 0: # 흰.
            move_top(i, curr_x, curr_y, next_x, next_y, False)
            # print("-> 반대로 이동(흰)")
        elif 0 <= next_x < N and 0 <= next_y < N and grid[next_x][next_y] == 1:  # 빨
            # print("-> 반대로 이동(빨)")
            move_top(i, curr_x, curr_y, next_x, next_y, True)

        else: # 파 or 벗어나는 경우 -> 가만히 있음
            # print("-> 또 파란색 or 밖 : 가만히")
            next_x, next_y = curr_x, curr_y

    piece[i][0], piece[i][1] = next_x, next_y



    # 해당 말의 위에 있는 말들도 이동


    # 도착한 칸에 말이 4개 이상이 되면 종료


# 턴이 진행되던 중에 말이 4개 이상 쌓이는 순간 게임이 종료
# -> 매 이동을 마칠 때 확인


# 이동방향에 대한 dx, dy : →, ←, ↑, ↓
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

import sys
input = sys.stdin.readline

if __name__ == "__main__":
    N, K = map(int, input().split())
    grid = [] # 체스판 -> 색깔을 나타냄
    piece = [] # 말
    piece_top = [ [[] for _ in range(N)] for _ in range(N) ] # 체스판 -> 각 위치에 놓인 말의 순서를 나타냄

    for i in range(N): # 체스판의 정보 -> 0은 흰색, 1은 빨간색, 2는 파란색
        line = list(map(int, input().split()))
        grid.append(line)

    for i in range(K): # i번 말의 정보
        line = list(map(int, input().split())) # 행, 열의 번호, 이동 방향
        for j in range(len(line)):
            line[j] -= 1 # 0부터 시작하도록 1씩 빼줌
        piece.append(line)
        piece_top[line[0]][line[1]].append(i)

    # print("piece_top")
    # for i in range(N):
    #     print(piece_top[i])
    # print()

    # print("grid")
    # for i in range(N):
    #     print(grid[i])
    # print()
    #
    # print("piece")
    # for i in range(K):
    #     print(piece[i])

    for count in range(1, 1001): # 1000턴까지 시도
        # 1번 부터 K번까지 이동
        for i in range(K):
            # print(count, "턴,", i, "번째 piece_top Before")
            # for j in range(N):
            #     print(piece_top[j])
            # print()

            move_piece(i)

            # print(count, "턴,", i, "번째 piece_top After")
            # for j in range(N):
            #     print(piece_top[j])
            # print()

            # 이동된 지점에 말이 4개 이상 쌓이면 종료
            if len(piece_top[piece[i][0]][piece[i][1]]) >= 4:
                print(count)
                exit()

    print(-1)