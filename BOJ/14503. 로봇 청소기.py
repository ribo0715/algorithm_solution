# 14503. 로봇 청소기


# 현재 방향기준 왼쪽 방향 우선 탐색 -> (d - 1) % 4
# 왼쪽으로 돌면서 확인한 후, 모두 없다면 한칸 후진
# 후진도 못하는 경우 끝

if __name__ == "__main__":
    n, m = map(int, input().split()) # 세로, 가로 -> [n - 1][m - 1]
    board = [[] for _ in range(n)]
    
    r, c, d = map(int, input().split()) # 칸의 좌표 : (r, c), 바라보는 방향 : d
    # d = 위쪽 0 / 오른쪽 1 / 아래쪽 2 / 왼쪽 3

    # 각 방향에 따른 좌표의 변화량
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    
    for i in range(n):
        board[i] = list(map(int, input().split()))

    count = 0
    
    if board[r][c] == 0:
        count += 1
    

    while True:
        board[r][c] = -1 # 현재 위치를 청소

        flag = 0 # 청소할 공간을 찾으면 1
        
        for _ in range(4): # 왼쪽으로 돌면서 네 방향 확인
            d = (d - 1) % 4 # 왼쪽으로 회전
            
            if board[r + dx[d]][c + dy[d]] == 0: # 청소하지 않은 곳이라면, 전진
                r += dx[d]
                c += dy[d]
                count += 1 # 청소한 칸의 개수 + 1
                flag = 1 # 청소할 공간을 찾은 경우임을 알림
                break

        if flag == 0: # 모두 청소되어 있거나 벽인 경우
            if board[r - dx[d]][c - dy[d]] == 1: # 뒤쪽이 벽인 경우 끝
                print(count)
                break

            else: # 후진할 수 있는 경우, 후진
                r -= dx[d]
                c -= dy[d]
            
