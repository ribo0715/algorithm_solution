# 15685. 드래곤 커브

"""
x축 → 방향,  y축 ↓ 방향

K(K > 1)세대 드래곤 커브는 K-1세대 드래곤 커브를 끝 점을 기준으로 90도 시계 방향 회전 시킨 다음, 그것을 끝 점에 붙인 것

크기가 100×100인 격자 위에 드래곤 커브가 N개

1×1인 정사각형의 네 꼭짓점이 모두 드래곤 커브의 일부인 정사각형의 개수를 구하기


격자의 좌표는 (x, y)로 나타내며, 0 ≤ x ≤ 100, 0 ≤ y ≤ 100만 유효한 좌표

첫째 줄에 드래곤 커브의 개수 N(1 ≤ N ≤ 20)

N개의 줄에는 드래곤 커브의 정보 -> 정보는 네 정수 x, y, d, g
x와 y는 드래곤 커브의 시작 점 -> 0 ≤ x, y ≤ 100

d는 시작 방향 -> 0 ≤ d ≤ 3
전 후 좌 우

g는 세대 -> 0 ≤ g ≤ 10

"""


# 좌표를 어떻게 표현할지
##grid = [[0 for _ in range(100)] for _ in range(100)]


# 시계방향으로 90도 돌리는 걸 어떻게 표현할 수 있을까
# 어떤 드래곤 커브를 90도 돌리는 함수

from collections import deque

def make_curve(x, y, d, g):
    # (x, y) 에서 d방향으로 시작하는 g세대 커브
    curve = deque() # 커브에 속한 점들을 담을 큐

    # 0세대
    curve.append((x, y))
    curve.append((x + dx[d], y + dy[d]))

    for _ in range(g): # g세대 까지 만들어감
        center = curve[-1] # 커브의 끝점 -> 기준으로 시계방향 90도 회전
        center_x = center[0]
        center_y = center[1]
        
        length = len(curve)
        for i in range(1, length): # 현재 커브 위의 점들을 회전
            target = curve[length - 1 -  i]
            target_x = target[0]
            target_y = target[1]

            offset_x = target_x - center_x
            offset_y = target_y - center_y

            target_rotated = (center_x - offset_y, center_y + offset_x)
            curve.append(target_rotated)

    return curve
##        """
##        0 : x +
##        1: y -
##        2: x -
##        3: y +
##
##        끝점기준 시계방향 90도 -> offset 기준 (-y, x) + 기준점
##
##        """

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

# n 개의 드래곤 커브를 담아둘 리스트
# grid에 해당 드래곤 커브의 번호로 자리 표시
# -> 0이 아닌 숫자가 있는 곳은 드래곤 커브가 존재하는 곳

# grid를 받아 드래곤 커브의 일부인 정사각형 갯수 세기
def calc_square(grid):
    count = 0
    
    for x in range(100):
        for y in range(100):
            if grid[x][y] + grid[x + 1][y] + grid[x][y + 1] + grid[x + 1][y + 1] == 4 :
                count += 1

    return count



def curve_to_grid(grid, curve): # 커브를 좌표에 표현
    while curve:
        x, y = curve.pop()

        grid[x][y] = 1



import sys
input = sys.stdin.readline


if __name__ == "__main__":
    # 좌표를 어떻게 표현할지
    grid = [[0 for _ in range(101)] for _ in range(101)]

    n = int(input())

    for i in range(n):
        x, y, d, g = map(int, input().split()) # x, y -> grid[x][y]

        curve = make_curve(x, y, d, g)
        curve_to_grid(grid, curve)

        


    
    print(calc_square(grid))















    
