# 20061. 모노미노도미노 2
"""
보드는 빨간색 보드, 파란색 보드, 초록색 보드가 그림과 같이 붙어있는 형태
좌표 (x, y)에서 x는 행, y는 열

이 게임에서 사용하는 블록은 타일 하나 또는 두 개가 가로 또는 세로로 붙어있는 형태

블록을 놓을 위치를 빨간색 보드에서 선택하면,
그 위치부터 초록색 보드로 블록이 이동하고,
파란색 보드로 블록이 이동
->  다른 블록을 만나거나 보드의 경계를 만나기 전까지 계속해서 이동

초록색 보드에서 어떤 행이 타일로 가득 차 있다면, 그 행의 타일은 모두 사라진다
사라진 이후에는 초록색 보드에서 사라진 행의 위에 있는 블록이 사라진 행의 수만큼 아래로 이동

파란색의 경우는 열이 타일로 가득 차 있으면, 그 열의 타일이 모두 사라진다
사라진 이후에는 파란색 보드에서 사라진 열의 왼쪽에 있는 블록이 사라진 열의 수만큼 오른쪽으로 이동

한 행이나 열이 타일로 가득 차서 사라지면 1점을 획득

초록색 보드의 0, 1번 행과 파란색 보드의 0, 1번 열은 그림에는 연한색으로 표현되어 있는 특별한 칸

초록색 보드의 0, 1번 행에 블록이 있으면, 블록이 있는 행의 수만큼 아래 행에 있는 타일이 사라지고
초록색 보드의 모든 블록이 사라진 행의 수만큼 아래로 이동

행이나 열이 타일로 가득찬 경우와 연한 칸에 블록이 있는 경우가 동시에 발생하는 경우
행이나 열이 타일로 가득 찬 경우가 없을 때까지 점수를 획득하는 과정이 모두 진행된 후,
연한 칸에 블록이 있는 경우를 처리

블록을 놓은 위치가 순서대로 주어졌을 때, 얻은 점수와 초록색 보드와 파란색 보드에 타일이 있는 칸의 개수를 모두 구해보자

"""
import sys
input = sys.stdin.readline


# 게임 보드를 나타낼 방법 -> 색깔별로 2차원 배열 -> red[4][4], blue[4][6], green[6][4]

# t 인 블록을 (x, y)에 놓았을때, 작업 수행
def put_block(t, x, y):
    put_in_blue(t, x)
    put_in_green(t, y)

    blue_point = check_blue()
    green_point = check_green()

    # 연한 칸 확인
    check_light_blue()
    check_light_green()

    # print("=======")
    # print("blue")
    # for i in range(4):
    #     print(blue[i])
    # print("=======")
    # print("green")
    # for i in range(6):
    #     print(green[i])
    # print("=======")
    return blue_point + green_point

def check_light_blue():
    count = 0
    for y in range(2):
        for x in range(4):
            if blue[x][y] == 1: # 블록이 있는 경우
                count += 1
                break

    target_line_y = []
    for i in range(count):
        target_line_y.append(5 - i)
    remove_line_y(target_line_y)

def check_light_green():
    count = 0
    for x in range(2):
        for y in range(4):
            if green[x][y] == 1:
                count += 1
                break

    target_line_x = []
    for i in range(count):
        target_line_x.append(5 - i)
    remove_line_x(target_line_x)

def put_in_blue(t, x):
    temp_y = 0
    if t == 3: # t = 3일 떄, (x + 1)도
        # blue의 맨 오른쪽(5)부터 확인
        for y in range(6):
            if blue[x][y] == blue[x + 1][y] == 0: # 둘 다 0으로 빈 경우
                temp_y = y
            else:
                break
        blue[x][temp_y] = 1
        blue[x + 1][temp_y] = 1


    else: # t = 1, 2일 때 -> x만
        for y in range(6):
            if blue[x][y] == 0:
                temp_y = y
            else:
                break
        blue[x][temp_y] = 1
        if t == 2:
            blue[x][temp_y - 1] = 1


def put_in_green(t, y):
    temp_x = 0
    if t == 2: # t = 2일 때, (y + 1)도
        # blue의 맨 오른쪽(5)부터 확인
        for x in range(6):
            if green[x][y] == green[x][y + 1] == 0:  # 둘 다 0으로 빈 경우
                temp_x = x
            else:
                break
        green[temp_x][y] = 1
        green[temp_x][y + 1] = 1


    else:  # t = 1, 2일 때 -> x만
        for x in range(6):
            if green[x][y] == 0:
                temp_x = x
            else:
                break
        green[temp_x][y] = 1
        if t == 3:
            green[temp_x - 1][y] = 1


def check_blue():
    target_line_y = [] # blue에서 지워줘야할 line y를 저장
    for y in reversed(range(6)):
        can_get_point = True
        for x in range(4):
            if blue[x][y] == 0:
                can_get_point = False
                break

        if can_get_point:
            target_line_y.append(y)

    # print("target_line_y", target_line_y)
    remove_line_y(target_line_y)
    blue_point = len(target_line_y) # 얻을 점수
    return blue_point

def check_green():
    target_line_x = []
    for x in reversed(range(6)):
        can_get_point = True
        for y in range(4):
            if green[x][y] == 0:
                can_get_point = False
                break

        if can_get_point:
            target_line_x.append(x)

    # print("target_line_x", target_line_x)
    remove_line_x(target_line_x)
    green_point = len(target_line_x)
    return green_point

def remove_line_y(target_line_y):
    target_line_y = sorted(target_line_y)
    for target_y in target_line_y:
        # print("y 줄 지운다!! 점수 추가")
        for x in range(4):
            for y in reversed(range(target_y)): # 한칸씩 땡김
                blue[x][y + 1] = blue[x][y]
            blue[x][0] = 0

def remove_line_x(target_line_x):
    target_line_x = sorted(target_line_x)
    for target_x in target_line_x:
        # print("x 줄 지운다!! 점수 추가")
        for y in range(4):
            for x in reversed(range(target_x)): # 한칸씩 땡김
                green[x + 1][y] = green[x][y]
            green[0][y] = 0


def count_all_square():
    count = 0
    for x in range(4):
        count += sum(blue[x])

    for x in range(6):
        count += sum(green[x])

    return count


if __name__ == "__main__":
    # 게임 보드
    blue = [ [0 for _ in range(6)] for _ in range(4) ]
    green = [ [0 for _ in range(4)] for _ in range(6) ]

    total_point = 0 # 점수

    N = int(input())

    for i in range(N):
        t, x, y = map(int, input().split())
        # t = 1 -> 그 위치,    t = 2 -> 가로,    t = 3 -> 세로
        # print(t, x, y)
        total_point += put_block(t, x, y)



    print(total_point)
    print(count_all_square())


    # 첫째 줄에 블록을 모두 놓았을 때 얻은 점수를 출력

    # 둘째 줄에는 파란색 보드와 초록색 보드에서 타일이 들어있는 칸의 개수를 출력