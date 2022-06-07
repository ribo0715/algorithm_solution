# 1227. [SW 문제해결 기본] 7일차 - 미로2
"""
주어진 미로의 출발점으로부터 도착지점까지 갈 수 있는 길이 있는지 판단

start부터 상 하 좌 우로 이동
-> 방문한 곳은 grid[x][y] = 1 로 바꿔버림
"""

from collections import deque


def bfs(grid, start_x, start_y):
    q = deque()
    q.append([start_x, start_y])

    while q:
        cur_x, cur_y = q.popleft()

        for i in range(4): # 상 하 좌 우 로의 이동
            next_x = cur_x + dx[i]
            next_y = cur_y + dy[i]

            if 0 <= next_x < 100 and 0 <= next_y < 100: # grid 내
                if grid[next_x][next_y] == "0":
                    q.append([next_x, next_y])
                    grid[next_x][next_y] = "1" # 방문표시
                elif grid[next_x][next_y] == "3": # 도착지점
                    return 1

    return 0


# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

if __name__ == "__main__":
    T = 10
    for test_case in range(1, T + 1):
        tc = int(input())
        grid = []

        start_x, start_y = 0, 0

        for i in range(100):
            line = list(input())
            if "2" in line:
                start_x = i
                start_y = line.index("2")
            grid.append(line)

        answer = bfs(grid, start_x, start_y)

        print("#{} {}".format(test_case, answer))
