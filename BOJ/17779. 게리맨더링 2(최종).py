# 17779. 게리맨더링 2

import sys
input = sys.stdin.readline

# 다섯 선거구로 조합을 나누는 방법
def divide_five_group_and_get_diff(x, y, d1, d2):
    group_num = [0 for _ in range(6)] # 각 그룹에 속한 인원 수를 저장 -> group_num[2] : 2번 선거구의 인원수
    grid = [[0 for _ in range(N)] for _ in range(N)]

    # 위치를 어떻게 분류해야하지... -> 5인 구역을 채워두고 나머지를 채운다
    for i in range(d1 + 1): # 왼쪽 아래 대각선으로
        grid[x + i][y - i] = 5
        grid[x + d2 + i][y + d2 - i] = 5

    for i in range(d2 + 1): # 오른쪽 아래 대각선으로
        grid[x + i][y + i] = 5
        grid[x + d1 + i][y - d1 + i] = 5

    for i in range(x + 1, x + d1 + d2):
        inside_group_5 = False
        for j in range(N):
            if grid[i][j] == 5:
                inside_group_5 = not inside_group_5

            if inside_group_5:
                grid[i][j] = 5 # 5번 그룹 내부임을 표시해줌

    # 각 그룹 별 속한 인원을 더해줌
    for r in range(N):
        for c in range(N):
            if grid[r][c] == 0:
                if r < x + d1 and c <= y:
                    group_num[1] += population_grid[r][c]

                elif r <= x + d2 and y < c:
                    group_num[2] += population_grid[r][c]

                elif x + d1 <= r and c < y - d1 + d2:
                    group_num[3] += population_grid[r][c]

                elif x + d2 < r and y - d1 + d2 <= c:
                    group_num[4] += population_grid[r][c]
            else:
                group_num[5] += population_grid[r][c]

    # 가장 많은 그룹과 가장 적은 그룹의 차 계산
    diff = max(group_num[1:]) - min(group_num[1:])

    return diff


if __name__ == "__main__":
    N = int(input())
    population_grid = []

    for _ in range(N):
        line = list(map(int, input().split()))
        population_grid.append(line)

    min_diff = 1e9
    for x in range(N):
        for y in range(N):
            for d1 in range(1, N + 1):
                for d2 in range(1, N + 1):
                    if 0 <= x < x + d1 + d2 < N and 0 <= y - d1 < y < y + d2 < N:
                        # print("x, y, d1, d2 :", x, y, d1, d2)
                        temp_diff = divide_five_group_and_get_diff(x, y, d1, d2)
                        # print("temp_diff :", temp_diff)
                        min_diff = min(min_diff, temp_diff)

    print(min_diff)

