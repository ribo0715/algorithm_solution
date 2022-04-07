# 20056. 마법사 상어와 파이어볼

import sys
input = sys.stdin.readline

def all_fireballs_move():
    global grid
    next_grid = [[[] for _ in range(N)] for _ in range(N)]

    for x in range(N):
        for y in range(N):
            if grid[x][y]: # 해당 지점에 파이어볼이 있는 경우
                for fireball in grid[x][y]: # 각각의 파이어볼에 대해 수행
                    m, s, d = fireball
                    next_x = (x + dx[d] * s) % N
                    next_y = (y + dy[d] * s) % N

                    next_grid[next_x][next_y].append([m, s, d])

    grid = next_grid

def combine_fireballs():
    for x in range(N):
        for y in range(N):
            if len(grid[x][y]) >= 2:
                sum_m = 0 # 합쳐진 질량
                sum_s = 0 # 합쳐진 속력
                temp_d = grid[x][y][0][2] # 첫번째 파이어볼의 방향을 우선 담음
                odd_even_same = True # 모두 홀,짝이 같은지
                for fireball in grid[x][y]:
                    m, s, d = fireball
                    sum_m += m
                    sum_s += s
                    if temp_d % 2 != d % 2: # 이전의 파이어볼과 홀,짝이 다른 경우 False
                        odd_even_same = False
                    temp_d = d
                next_m = sum_m // 5
                next_s = sum_s // len(grid[x][y])

                grid[x][y].clear() # 합쳐진 파이어볼을 나눔
                if next_m != 0: # 질량이 0이 된 경우 소멸
                    if odd_even_same: # 모두 홀,짝이 같은 경우 -> 0, 2, 4, 6 방향
                        for i in range(4):
                            grid[x][y].append([next_m, next_s, 2 * i])
                    else: # -> 1, 3, 5, 7 방향
                        for i in range(4):
                            grid[x][y].append([next_m, next_s, 2 * i + 1])


def get_sum_fireballs_m():
    sum_m = 0
    for x in range(N):
        for y in range(N):
            if grid[x][y]:
                for fireball in grid[x][y]:
                    sum_m += fireball[0]

    return sum_m




# 12시 방향부터 시계방향으로
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

if __name__ == "__main__":
    N, M, K = map(int, input().split())

    grid = [[[] for _ in range(N)] for _ in range(N)] # 해당 지점의 파이어볼의 정보들을 저장
    for i in range(M): # 파이어볼의 정보
        r, c, m, s, d = map(int, input().split())
        grid[r - 1][c - 1].append([m, s, d]) # 질량, 속력, 방향

    for _ in range(K):
        all_fireballs_move()
        combine_fireballs()

    print(get_sum_fireballs_m())