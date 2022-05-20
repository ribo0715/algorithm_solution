# 1249. [SW 문제해결 응용] 4일차 - 보급로

from collections import deque

# 상 하 좌 우 로의 이동
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

if __name__ == "__main__":
    T = int(input())

    for test_case in range(1, T + 1): # 테스트케이스마다 수행
        N = int(input())
        grid = [[0 for _ in range(N)] for _ in range(N)]
        # print(grid)
        for i in range(N):
            line = input()
            # print(line)
            for j in range(N):
                grid[i][j] = int(line[j])


        q = deque() # 현재 위치, 해당 위치에 도달하기까지 경로에 대한 총 복구시간
        q.append([0, 0, 0])

        total_grid = [[1e9 for _ in range(N)] for _ in range(N)] # 각 지점에 도착하기까지 걸린 최소 복구 시간

        while q:
            curr_x, curr_y, curr_time = q.popleft()

            for i in range(4):
                next_x = curr_x + dx[i]
                next_y = curr_y + dy[i]

                if 0 <= next_x < N and 0 <= next_y < N: # grid 내에 있는 경우
                    next_time = curr_time + grid[next_x][next_y]

                    temp_time = total_grid[next_x][next_y]
                    if temp_time > next_time: # 현재까지 최소 복구 시간인 경우
                        total_grid[next_x][next_y] = next_time

                        q.append([next_x, next_y, next_time])

        min_time = total_grid[N - 1][N - 1]

        print("#" + str(test_case), min_time)
