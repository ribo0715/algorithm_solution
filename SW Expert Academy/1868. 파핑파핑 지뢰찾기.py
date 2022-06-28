# 1868. 파핑파핑 지뢰찾기

from collections import deque

# 12시부터 시계방향으로 8방향
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

if __name__ == "__main__":
    T = int(input())

    for test_case in range(1, T + 1):
        click_count = 0

        N = int(input())
        grid = []
        safe = 0 # 지뢰가 없는 칸의 수 -> .

        for _ in range(N):
            line = list(input())
            safe += line.count(".") # 지뢰가 아닌 칸의 수를 셈
            grid.append(line)

        click_count = safe

        # temp : 지뢰가 주변에 없는 칸 -> 0 , 지뢰가 주변에 있는 칸 -> 1 , 지뢰 -> -1
        temp = [[0 for _ in range(N)] for _ in range(N)]
        for x in range(N):
            for y in range(N):
                if grid[x][y] == "*":
                    temp[x][y] = -1 # 지뢰
                    for i in range(8):
                        next_x = x + dx[i]
                        next_y = y + dy[i]

                        if 0 <= next_x < N and 0 <= next_y < N:
                            if grid[next_x][next_y] == ".":
                                temp[next_x][next_y] = 1 # 지뢰 주변에 위치

        visited = [[0 for _ in range(N)] for _ in range(N)] # 방문 표시
        for x in range(N):
            for y in range(N):
                if temp[x][y] == 0: # 주변에 지뢰가 없는 곳에서 시작
                    if visited[x][y]:
                        continue

                    visited[x][y] = 1
                    q = deque()
                    q.append([x, y])
                    while q:
                        cur_x, cur_y = q.popleft()
                        for i in range(8): # 주변으로 확장해나감
                            next_x = cur_x + dx[i]
                            next_y = cur_y + dy[i]

                            if 0 <= next_x < N and 0 <= next_y < N:
                                if not visited[next_x][next_y]:
                                    if temp[next_x][next_y] == 0: # 0이면, 해당 칸도 주변에 지뢰가 없는 칸이므로 해당 칸에서 이어서 확장
                                        q.append([next_x, next_y])
                                    visited[next_x][next_y] = 1
                                    click_count -= 1 # [x, y]를 클릭했을때 해당 칸까지도 확장되므로 click_count를 줄여줌

        print("#{} {}".format(test_case, click_count))