# 20058. 마법사 상어와 파이어스톰
import copy
from collections import deque
import sys
input = sys.stdin.readline


# 2**L × 2**L 크기의 부분 격자로 나눔, 각 격자를 회전
def rotate_grid(L):
    before_A = copy.deepcopy(A) # 회전하기 전의 격자

    # 모든 격자들에 대해
    for grid_x in range(2 ** (N - L)):
        for grid_y in range(2 ** (N - L)):
            rotage_sub_grid(grid_x * (2 ** L), grid_y * (2 ** L), L, before_A)


# (x, y) 가 (0, 0)위치인 한 변의 길이 2 ** L 인 격자 회전
def rotage_sub_grid(x, y, L, before_A):
    side_length = 2 ** L

    for i in range(side_length):
        for j in range(side_length):
            A[x + j][y + side_length - 1 - i] = before_A[x + i][y + j]


# 얼음이 있는 칸을 확인하여 인접한 칸 수에 따라 얼음 양을 줄임
def melt_down_A():
    before_A = copy.deepcopy(A)

    for x in range(2 ** N):
        for y in range(2 ** N):
            if A[x][y] > 0: # 얼음이 있는 경우
                adjacent_or_melt(x, y, before_A) # 인접한 칸 확인


# 3개 이상의 얼음과 인접하지 않은 경우 1 줄어듬
def adjacent_or_melt(x, y, before_A):
    count = 0 # 인접한 얼음 수
    for i in range(4):
        temp_x = x + dx[i]
        temp_y = y + dy[i]

        if 0 <= temp_x < 2 ** N and 0 <= temp_y < 2 ** N: # 격자 내
            if before_A[temp_x][temp_y] > 0: # 얼음이 있는 경우
                count += 1

        if count >= 3: # 3개 이상과 인접 -> 끝
            return

    A[x][y] -= 1


# 남아있는 얼음의 합
def count_sum_A():
    count = 0
    for x in range(2 ** N):
        count += sum(A[x])

    return count



# 가장 큰 덩어리 찾기
def find_biggest_ice():
    visited = [[0 for _ in range(2 ** N)] for _ in range(2 ** N)]

    biggest_ice_size = 0

    for x in range(2 ** N):
        for y in range(2 ** N):
            if A[x][y] > 0 and visited[x][y] == 0: # 얼음이 있는 칸
                ice_size = 1 # 해당 위치가 속한 얼음의 크기
                q = deque()
                q.append([x, y])
                visited[x][y] = 1

                while q:
                    for _ in range(len(q)):
                        curr_x, curr_y = q.popleft()

                        for i in range(4):
                            next_x = curr_x + dx[i]
                            next_y = curr_y + dy[i]

                            if 0 <= next_x < 2 ** N and 0 <= next_y < 2 ** N:
                                if visited[next_x][next_y] == 0:
                                    visited[next_x][next_y] = 1 # 방문 기록

                                    if A[next_x][next_y] > 0: # 얼음인 경우
                                        ice_size += 1
                                        q.append([next_x, next_y])

                biggest_ice_size = max(biggest_ice_size, ice_size)

    return biggest_ice_size

# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# def print_A():
#     for i in range(2 ** N):
#         print(A[i])

if __name__ == "__main__":
    N, Q = map(int, input().split())

    A = []
    for _ in range(2 ** N):
        line = list(map(int, input().split()))
        A.append(line)

    L_list = list(map(int, input().split()))

    # print("L list:", L_list)
    for L in L_list:
        rotate_grid(L)
        melt_down_A()

    # print_A()
    print(count_sum_A())
    print(find_biggest_ice())


