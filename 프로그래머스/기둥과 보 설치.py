# 기둥과 보 설치

# 기둥(세로)인 경우
def make_column(rows, columns, x, y):
    if y == 1:  # 바닥
        columns[y][x] = 1

    elif columns[y - 1][x] == 1:  # 다른 기둥 위
        columns[y][x] = 1

    # 보의 한쪽 끝 부분 위
    elif rows[y][x] == 1 or rows[y][x - 1] == 1:
        columns[y][x] = 1

    else:
        return False

    return True


# 기둥 제거
def remove_column(rows, columns, x, y):
    columns[y][x] = 0  # 기둥을 우선 없애봄
    # 주변 보 확인 -> 기둥을 지워도 해당 보를 놓을 수 있는지
    if rows[y + 1][x] == 1:  # 위 오른쪽 보
        if not make_row(rows, columns, x, y + 1):
            columns[y][x] = 1
            return

    if rows[y + 1][x - 1] == 1:  # 위 왼쪽 보
        if not make_row(rows, columns, x - 1, y + 1):
            columns[y][x] = 1
            return

    if columns[y + 1][x] == 1:  # 위 기둥
        if not make_columns(rows, columns, x, y + 1):
            columns[y][x] = 1
            return

    print("정삭적으로 기둥(column) 제거")


# 보(가로)인 경우
def make_row(rows, columns, x, y):
    # 한쪽 끝 부분이 기둥 위에 있음
    if columns[y - 1][x] == 1 or columns[y - 1][x + 1] == 1:
        rows[y][x] = 1

    # 양쪽 끝 부분이 다른 보와 동시에 연결
    elif rows[y][x - 1] == rows[y][x + 1] == 1:
        rows[y][x] = 1

    else:
        return False

    return True


# 보 제거
def remove_row(rows, columns, x, y):
    rows[y][x] = 0
    # 없어도 유지가 되는지 확인
    if columns[y][x] == 1:  # 왼쪽 위 기둥
        if not make_columns(rows, columns, x, y):
            rows[y][x] = 1
            return

    if columns[y][x + 1] == 1:  # 오른쪽 위 기둥
        if not make_columns(rows, columns, x + 1, y):
            rows[y][x] = 1
            return

    if rows[y][x - 1] == 1:  # 왼쪽 보
        if not make_row(rows, columns, x - 1, y):
            rows[y][x] = 1
            return

    if rows[y][x + 1] == 1:  # 오른쪽 보
        if not make_row(rows, columns, x + 1, y):
            rows[y][x] = 1
            return

    print("정삭적으로 보(row) 제거")


def get_result(rows, columns, n):
    result = []

    for i in range(n + 1):
        for j in range(n + 1):
            if columns[j + 1][i + 1] == 1:
                result += [[i, j, 0]]
            if rows[j + 1][i + 1] == 1:
                result += [[i, j, 1]]

    return result


# def print_(rows, columns, n):
#     print("보")
#     for i in reversed(range(1, n + 2)):
#         print(rows[i][1:n + 1])
#     print("기둥")
#     for i in reversed(range(1, n + 1)):
#         print(columns[i][1:n + 2])


def solution(n, build_frame):
    answer = [[]]

    # 상 하 좌 우 바깥쪽으로 한칸씩 늘려서 저장 -> 이후 조건 검사하기 편하도록
    rows = [[0 for _ in range(n + 2)] for _ in range(n + 3)]  # 현재 보 상태
    columns = [[0 for _ in range(n + 3)] for _ in range(n + 2)]  # 현재 기둥 상태

    for cur_build_frame in build_frame:
        x, y, a, b = cur_build_frame  # x, y 를 둘 다 +1 해주어 index를 확인
        # (x, y) -> [y][x]
        if a == 0 and b == 0:
            # continue
            remove_column(rows, columns, x + 1, y + 1)

        elif a == 0 and b == 1:
            make_column(rows, columns, x + 1, y + 1)

        elif a == 1 and b == 0:
            # continue
            remove_row(rows, columns, x + 1, y + 1)

        else:
            make_row(rows, columns, x + 1, y + 1)

    # print_(rows, columns, n)

    answer = get_result(rows, columns, n)
    return answer