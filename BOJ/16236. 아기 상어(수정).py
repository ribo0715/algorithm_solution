# 16236. 아기 상어(수정)


# 현재 상어에서 가장 가까운 물고기를 찾아, 이동거리, 물고기 위치 반환
def find_nearest(grid, shark_i, shark_j, shark_size):
    q = deque()  # 확인해볼 위치들을 담음
    q.append((shark_i, shark_j))

    visited = deque()  # 확인해본 위치들을 담음
    visited.append((shark_i, shark_j))

    target_fish = []  # 최단 거리에 있는 물고기들을 담을 리스트 -> sort() 로 하나를 고름
    distance = 0  # 상어의 이동거리
    found_fish = False

    while True:
        if not q:  # 모든 위치를 확인했지만, 찾지 못한 경우
            return -1, 0, 0

        for _ in range(len(q)):
            temp_i, temp_j = q.popleft()

            if 1 <= grid[temp_i][temp_j] <= 6 and grid[temp_i][temp_j] < shark_size:  # 물고기에 도달
                found_fish = True  # 먹을 수 있는 물고기를 찾았음을 나타냄
                # 이번 이동거리까지는 수행하여 그중 가장 위, 왼쪽 지점을 골라야함
                target_fish.append((temp_i, temp_j))

            if temp_i - 1 >= 0 and not (temp_i - 1, temp_j) in visited:
                if grid[temp_i - 1][temp_j] <= shark_size:
                    q.append((temp_i - 1, temp_j))
                visited.append((temp_i - 1, temp_j))

            if temp_i + 1 < N and not (temp_i + 1, temp_j) in visited:
                if grid[temp_i + 1][temp_j] <= shark_size:
                    q.append((temp_i + 1, temp_j))
                visited.append((temp_i + 1, temp_j))

            if temp_j - 1 >= 0 and not (temp_i, temp_j - 1) in visited:
                if grid[temp_i][temp_j - 1] <= shark_size:
                    q.append((temp_i, temp_j - 1))
                visited.append((temp_i, temp_j - 1))

            if temp_j + 1 < N and not (temp_i, temp_j + 1) in visited:
                if grid[temp_i][temp_j + 1] <= shark_size:
                    q.append((temp_i, temp_j + 1))
                visited.append((temp_i, temp_j + 1))

        if found_fish:
            break

        distance += 1

    target_fish.sort()
    target_i, target_j = target_fish[0]

    return distance, target_i, target_j


from collections import deque
import sys

input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    grid = [[] for _ in range(N)]
    shark_i, shark_j = 0, 0
    shark_size = 2

    for i in range(N):
        grid[i] = list(map(int, input().split()))

        for j in range(N):
            if 1 <= grid[i][j] <= 6:  # 물고기
                size = grid[i][j]

            elif grid[i][j] == 9:  # 아기 상어
                shark_i, shark_j = i, j

    times = 0
    count = 0

    while True:
        distance, target_i, target_j = find_nearest(grid, shark_i, shark_j, shark_size)

        if distance == -1:  # 먹을 수 없는 경우
            print(times)
            break

        else:
            ##            print("이동")
            ##            print("distance :", distance)
            target_size = grid[target_i][target_j]
            ##            print("target_size :", target_size)
            ##            print("shark_size :", shark_size)
            times += distance  # 이동시간만큼 시간 추가
            ##            print("shark_i :", shark_i, "shark_j :", shark_j)
            grid[shark_i][shark_j] = 0
            shark_i, shark_j = target_i, target_j  # 상어 위치 이동
            grid[shark_i][shark_j] = 9

            count += 1

            if count == shark_size:  # 크기만큼 먹으면
                shark_size += 1
                count = 0  # 초기화
