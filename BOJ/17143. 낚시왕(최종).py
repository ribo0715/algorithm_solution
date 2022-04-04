# 17143. 낚시왕(최종)


def catch_shark(c, grid):
    shark_size = 0

    for r in range(R):
        if grid[r][c] != 0:
            shark_size = grid[r][c][2]
            grid[r][c] = 0
            break

    return shark_size


def sharks_move(grid):
    ##    print("Before grid")
    ##    for i in range(R):
    ##        print(grid[i])

    temp = [[0 for _ in range(C)] for _ in range(R)]  # 상어들이 움직이고 난 위치

    for r in range(R):
        for c in range(C):
            if grid[r][c] == 0:  # 빈칸인 경우
                continue
            else:  # 상어가 있는 경우
                s, d, z = grid[r][c]
                temp_r, temp_c = r, c

                ##                print("Before r, c =", r,c)
                if 1 <= d <= 2:
                    for _ in range(s % (2 * (R - 1))):
                        if d == 1:  # 위
                            if temp_r == 0:
                                d = 2
                                temp_r += 1
                            else:
                                temp_r -= 1

                        elif d == 2:  # 아래
                            if temp_r == R - 1:
                                d = 1
                                temp_r -= 1
                            else:
                                temp_r += 1

                elif 3 <= d <= 4:
                    for _ in range(s % (2 * (C - 1))):
                        if d == 3:  # 오른쪽
                            if temp_c == C - 1:
                                d = 4
                                temp_c -= 1
                            else:
                                temp_c += 1

                        elif d == 4:  # 왼쪽
                            if temp_c == 0:
                                d = 3
                                temp_c += 1
                            else:
                                temp_c -= 1

                ##                print("After r, c =", r,c)
                # r, c 로 상어가 이동한 상태
                ##                grid[prev_r][prev_c] = 0

                if temp[temp_r][temp_c] == 0:  # 해당 위치에 아직 다른 상어가 존재하지 않는 경우
                    temp[temp_r][temp_c] = (s, d, z)
                ##                    print("빈자리!", r, c)

                else:  # 다른 상어가 이미 존재하고 있는 경우
                    ##                    print(temp_r,",",temp_c,"에서 상어 먹힘")
                    if temp[temp_r][temp_c][2] < z:  # 잡아먹을 수 있는 크기의 상어가 존재
                        temp[temp_r][temp_c] = (s, d, z)
    ##                    else: # 잡아먹히는 경우
    ##                        temp[r][c] =

    ##    print("After")
    ##    for i in range(R):
    ##        print(temp[i])

    return temp


import sys

input = sys.stdin.readline

if __name__ == "__main__":
    R, C, M = map(int, input().split())
    grid = [[0 for _ in range(C)] for _ in range(R)]  # 상어의 위치를 나타낼 배열

    for _ in range(M):
        # (r, c)는 상어의 위치, s는 속력, d는 이동 방향, z는 크기
        r, c, s, d, z = map(int, input().split())
        # d가 1인 경우는 위, 2인 경우는 아래, 3인 경우는 오른쪽, 4인 경우는 왼쪽
        grid[r - 1][c - 1] = (s, d, z)

    sum = 0
    for c in range(C):
        sum += catch_shark(c, grid)
        grid = sharks_move(grid)

    print(sum)

