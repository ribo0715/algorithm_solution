# 19238. 스타트 택시
import sys
input = sys.stdin.readline
from collections import deque

# 현재 택시에서 가장 가까운 승객의 위치를 찾아 [x위치, y위치, 거리] 반환 -> 남은 승객에 도달할 수 없는 경우, [-1, -1, -1] 반환
def find_nearest_passenger():
    global fuel, texi_x, texi_y
    if [texi_x, texi_y] in start: # 택시와 승객이 같은 위치인 경우, 거리 = 0
        return [texi_x, texi_y, 0]

    q = deque()
    q.append([texi_x, texi_y])  # 택시의 현재 위치에서 시작
    distance = 0 # 가장 가까운 승객까지의 거리

    visited = [ [0 for _ in range(N + 1)] for _ in range(N + 1)] # 방문 확인

    q_nearest_passenger = deque()  # 최소거리로 도달 가능한 승객들을 담을 큐 -> 여러명인 경우 sort해줘서 승객을 골라줌
    while q:
        distance += 1 # 거리를 1씩 늘려나가면서 확인
        for _ in range(len(q)):
            curr_x, curr_y = q.popleft()

            for i in range(4): # 상하좌우로 뻗어가며 확인
                next_x = curr_x + dx[i]
                next_y = curr_y + dy[i]

                if 1 <= next_x <= N and 1 <= next_y <= N: # 구역 내에 있는지
                    if grid[next_x][next_y] >= 2: # 승객의 위치인 경우
                        q_nearest_passenger.append([next_x, next_y])
                        visited[next_x][next_y] = 1
                        continue
                    if visited[next_x][next_y] == 0 and grid[next_x][next_y] != 1:# 벽 제외
                        q.append([next_x, next_y])
                        visited[next_x][next_y] = 1

        if q_nearest_passenger: # 최소거리로 도달가능한 승객을 찾은 경우
            nearest_passenger_x, nearest_passenger_y  = sorted(q_nearest_passenger)[0] # 가장 행, 열 번호가 작은 승객 위치 반환
            texi_x, texi_y = nearest_passenger_x, nearest_passenger_y
            fuel -= distance
            return [nearest_passenger_x, nearest_passenger_y, distance]

    return [-1, -1, -1] # 어느 승객에도 도달하지 못하는 경우


# 해당 승객의 목적지까지의 거리 계산 -> bfs로 길이를 1씩 늘려감
def get_distance_to_destination(passenger_x, passenger_y):
    global texi_x, texi_y, fuel

    index = start.index([passenger_x, passenger_y])
    destination_x, destination_y = end[index]

    q = deque()
    q.append([passenger_x, passenger_y])
    distance = 0

    visited = [ [0 for _ in range(N + 1)] for _ in range(N + 1)] # 방문 확인

    while q and fuel > distance:
        distance += 1
        for _ in range(len(q)):
            curr_x, curr_y = q.popleft()

            for i in range(4): # 상하좌우
                next_x = curr_x + dx[i]
                next_y = curr_y + dy[i]

                if [next_x, next_y] == [destination_x, destination_y]: # 목적지인 경우
                    start.pop(index)  # start, end 에서 지워줌
                    end.pop(index)
                    grid[passenger_x][passenger_y] = -1 # grid에서도 해당 승객 제거
                    texi_x, texi_y = destination_x, destination_y
                    fuel -= distance
                    return distance

                if 1 <= next_x <= N and 1 <= next_y <= N:  # 구역 내에 있는지
                    if visited[next_x][next_y] == 0 and grid[next_x][next_y] != 1:  # 벽 제외
                        q.append([next_x, next_y])
                        visited[next_x][next_y] = 1

    return -1 # 목적지에 도달하지 못하는 경우


# 상 하 좌 우 확인
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

if __name__ == "__main__":
    N, M, fuel = map(int, input().split())

    grid = [0] # 지도 상태를 나타냄 -> 0은 빈칸, 1은 벽
    for i in range(N):
        line = [0] + list(map(int, input().split()))
        grid.append(line)

    texi_x, texi_y = map(int, input().split()) # 택시의 행 번호와 열 번호

    start = [] # i번 승객의 출발지 : start[i]
    end = [] # i번 승객의 목적지 : end[i]
    for i in range(M): # 승객의 출발지, 목적지 위치
        start_x, start_y, end_x, end_y = map(int, input().split())
        grid[start_x][start_y] = i + 2 # 승객의 번호를 grid에 담음
        start.append([start_x, start_y])
        end.append([end_x, end_y])

    while fuel > 0 and start: # 연료도 있고, 태워야할 승객도 있는 경우
        nearest_passenger_x, nearest_passenger_y, distance_1 = find_nearest_passenger()
        if distance_1 == -1: # 연료가 부족했거나 어느 승객에도 도달하지 못하는 경우
            break

        distance_2 = get_distance_to_destination(nearest_passenger_x, nearest_passenger_y)
        if distance_2 == -1: # 연료가 부족했거나 목적지에 도달하지 못하는 경우
            break

        # 한 승객을 목적지로 성공적으로 이동시키면, 그 승객을 태워 이동하면서 소모한 연료 양의 두 배가 충전
        fuel += distance_2 * 2

    if start: # 남은 손님이 있는 경우
        print(-1)
    else:
        print(fuel)
