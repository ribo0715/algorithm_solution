# 21610. 마법사 상어와 비바라기

import sys
input = sys.stdin.readline
from collections import deque


# 모든 구름이 d방향으로 s칸 이동
def move_all_cloud(d, s):
    global cloud, visited

    for _ in range(len(cloud)):
        curr_cloud_x, curr_cloud_y = cloud.popleft()

        next_cloud_x = (curr_cloud_x + dx[d] * s) % N
        next_cloud_y = (curr_cloud_y + dy[d] * s) % N

        A[next_cloud_x][next_cloud_y] += 1 # 해당 지점에 비를 내림
        visited[next_cloud_x][next_cloud_y] = 1  # 해당 지점에 표시
        cloud.append([next_cloud_x, next_cloud_y])


# 각 구름에서 비를 내림 -> 구름 움직일때 같이 수행하도록 수정
# def rain_from_cloud():
#     for curr_cloud in cloud:
#         curr_cloud_x, curr_cloud_y = curr_cloud
#         A[curr_cloud_x][curr_cloud_y] += 1 # 바구니에 물 + 1


# 물복사버그 마법 -> 대각선으로 거리 1인 칸에 물이 담긴 바구니 수만큼 추가로 증가
def water_copy_bug():
    global cloud, visited

    while cloud:
        target_x, target_y = cloud.popleft()
        count = 0
        for i in range(4): # 각 지점의 대각선 확인
            d = 2 + i * 2
            temp_x = target_x + dx[d]
            temp_y = target_y + dy[d]

            if 0 <= temp_x < N and 0 <= temp_y < N: # 경계 내
                if A[temp_x][temp_y] > 0: # 물이 들어있는 경우
                    count += 1

        A[target_x][target_y] += count


# 바구니에 물이 2 이상인 곳에 구름이 생기고, 물의 양이 2 감소
def make_new_cloud():
    global cloud

    for x in range(N):
        for y in range(N):
            if not visited[x][y]: # 이전에 비를 내린 구름이 아니어야함
                if A[x][y] >= 2: # 물의 양이 2 이상
                    cloud.append([x, y]) # 구름이 생김
                    A[x][y] -= 2 # 물의 양 2 감소


# 전체 바구니의 물의 양 구함
def get_sum_A():
    total = 0
    for x in range(N):
        total += sum(A[x])

    return total

# 1부터 순서대로 ←, ↖, ↑, ↗, →, ↘, ↓, ↙ -> 대각선 : 2, 4, 6, 8
dx = [0] + [0, -1, -1, -1, 0, 1, 1, 1]
dy = [0] + [-1, -1, 0, 1, 1, 1, 0, -1]

# def print_A():
#     for i in range(N):
#         print(A[i])
#     print("==============")

if __name__ == "__main__":
    N, M = map(int, input().split())

    A = []
    move_list = []

    cloud = deque() # 구름의 위치를 담음
    cloud.append([N - 1, 0])
    cloud.append([N - 1, 1])
    cloud.append([N - 2, 0])
    cloud.append([N - 2, 1])

    for _ in range(N):
        line = list(map(int, input().split())) # 각 지점에 저장된 물의 양
        A.append(line)

    for _ in range(M):
        d, s = map(int, input().split()) # 방향, 거리

        visited = [[0 for _ in range(N)] for _ in range(N)] # 비를 내린 구름의 지점에 대해 1로 표시 -> 다음 구름 만들때 제외
        move_all_cloud(d, s)
        # rain_from_cloud() # -> move에 포함시켜서 같이 수행
        water_copy_bug()
        make_new_cloud()

        # move_list.append([d, s]) # -> 리스트에 넣고 빼면서 할 필요 없이, 그냥 바로바로 수행

    # print_A()

    # for move in move_list:
    #     d, s = move
    #
    #     move_all_cloud(d, s)
    #     rain_from_cloud()
    #     water_copy_bug()
    #     make_new_cloud()
    #     print_A()

    print(get_sum_A())