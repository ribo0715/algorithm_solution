# 4613. 러시아 국기 같은 깃발
"""
위에서 몇 줄(한 줄 이상)은 모두 흰색으로 칠해져 있어야 한다.
다음 몇 줄(한 줄 이상)은 모두 파란색으로 칠해져 있어야 한다.
나머지 줄(한 줄 이상)은 모두 빨간색으로 칠해져 있어야 한다.
"""


# white, blue, red 줄로 색칠 -> 새로 칠해야 하는 칸의 개수 구함
def get_count(grid, M, white, blue, red):
    count = 0

    i = 0
    for _ in range(white):
        temp = grid[i].count("W")
        count += M - temp
        i += 1

    for _ in range(blue):
        temp = grid[i].count("B")
        count += M - temp
        i += 1

    for _ in range(red):
        temp = grid[i].count("R")
        count += M - temp
        i += 1

    return count



if __name__ == "__main__":
    T = int(input())

    for test_case in range(1, T + 1):
        N, M = map(int, input().split())
        grid = []

        for _ in range(N):
            line = list(input())
            grid.append(line)

        # w, b, r 의 가능한 경우의 수를 모두 구함
        # 0 ~ N-3 / 0 ~ N-3-w / 0 ~ N-3-w-b

        minimum = 2500
        for white in range(N - 2): # 0번째 줄 넘어서 추가 하얀줄
            for blue in range(N - 2 - white):
                red = N - 2 - white - blue
                # white + 1, blue + 1, red + 1 줄로 색칠
                cur_count = get_count(grid, M, white + 1, blue + 1, red)
                # print("{}, {}, {} 줄로 칠할때 cur_count = {}".format(white + 1, blue + 1, red, cur_count))
                minimum = min(minimum, cur_count)

        print("#{} {}".format(test_case, minimum))
