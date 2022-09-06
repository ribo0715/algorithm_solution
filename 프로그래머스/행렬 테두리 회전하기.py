# 행렬 테두리 회전하기
"""
이 행렬에서 직사각형 모양의 범위를 여러 번 선택
-> 테두리 부분에 있는 숫자들을 시계방향으로 회전

각 회전은 (x1, y1, x2, y2)인 정수 4개로 표현
-> x1 행 y1 열부터 x2 행 y2 열까지의 영역에 해당하는 직사각형에서 테두리에 있는 숫자들을 한 칸씩 시계방향으로 회전

"""


# def print_grid(grid, rows, columns):
#     for row in range(rows):
#         print(grid[row])

def solution(rows, columns, queries):
    answer = []
    grid = []

    num = 1
    for row in range(rows):
        grid.append(list(range(num, num + columns)))
        num += columns

    for query in queries:
        x1, y1, x2, y2 = query
        x1, y1, x2, y2 = x1 - 1, y1 - 1, x2 - 1, y2 - 1
        minimum = 10000

        temp = grid[x1][y1]
        for x in range(x1, x2):
            grid[x][y1] = grid[x + 1][y1]
        for y in range(y1, y2):
            grid[x2][y] = grid[x2][y + 1]
        for x in reversed(range(x1, x2)):
            grid[x + 1][y2] = grid[x][y2]
        for y in reversed(range(y1, y2)):
            grid[x1][y + 1] = grid[x1][y]
        grid[x1][y1 + 1] = temp

        minimum = min(minimum, min(grid[x1][y1:y2 + 1]))
        minimum = min(minimum, min(grid[x2][y1:y2 + 1]))
        for x in range(x1 + 1, x2):
            minimum = min(minimum, grid[x][y1])
            minimum = min(minimum, grid[x][y2])

        answer.append(minimum)
        # print_grid(grid, rows, columns)
    return answer