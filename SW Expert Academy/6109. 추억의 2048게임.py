# 6109. 추억의 2048게임
"""
left를 함수를 만들고, left을 제외한 다른것들은 회전시키고 left을 수행한 후 다시 돌려주는 식으로 수행
"""



# 시계 방향으로 90도 회전
def get_rotated(grid, N):
    rotated_grid = [[0 for _ in range(N)] for _ in range(N)]

    for x in range(N):
        for y in range(N):
            rotated_grid[y][N - 1 - x] = grid[x][y]

    return rotated_grid


def move_left(grid, N):
    for x in range(N):
        # 0을 제거해줌
        grid[x] = [k for k in grid[x] if k != 0]
        if not grid[x]: # 해당 줄이 전부 0인 경우, 넘어감
            continue

        temp = []
        prev = grid[x].pop(0)
        if not grid[x]:
            temp = [prev]

        while grid[x]:
            cur = grid[x].pop(0)
            # print("prev", prev, "cur", cur)
            if prev != cur:
                if prev != 0: # 이전거에서 합쳐져서 prev가 0인 경우는 제외
                    temp.append(prev)
                if not grid[x]:
                    temp.append(cur)
                prev = cur

            else: # 같으면 합쳐줌
                temp.append(prev + cur)
                prev = 0

            # print("grid[x] :", grid[x])
            # print("temp :", temp)
        # 뒤에는 0을 붙여줌
        grid[x] = temp + [0] * (N - len(temp))


def print_grid(grid, N):
    # grid 출력
    for x in range(N):
        # print(" ".join(grid[x])) # str형식으로 들어가야함 -> int값으로 들어가있어서 불가능
        for y in range(N):
            print(grid[x][y], end=" ")
        print()


if __name__ == "__main__":
    T = int(input())

    for test_case in range(1, T + 1):
        N, S = input().split()
        N = int(N)
        grid = []
        for _ in range(N):
            line = list(map(int, input().split()))
            grid.append(line)

        s_list = ["left", "down", "right", "up"]
        k = s_list.index(S) # S가 s_list에서 몇번째 값인지 -> k번 시계방향 회전, move_left, 4-k번 시계방향 회전(= 반시계방향 회전)

        for _ in range(k):
            grid = get_rotated(grid, N)

        # print_grid(grid, N)
        # print("==========")
        move_left(grid, N)
        # print_grid(grid, N)
        # print("==========")
        for _ in range(4 - k):
            grid = get_rotated(grid, N)

        print("#{}".format(test_case))
        # grid 출력
        print_grid(grid, N)