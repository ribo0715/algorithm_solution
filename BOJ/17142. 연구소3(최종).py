import sys
import copy
from itertools import combinations
from collections import deque

input = sys.stdin.readline

# 상 하 좌 우 에 대한 움직임
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

#
def spread(lab, virus_list):
    times = [[-1 for _ in range(N)] for _ in range(N)] # 각 지점에 바이러스가 활성되는 시간을 담음
    visited = [[0 for _ in range(N)] for _ in range(N)] # 각 지점에 대한 방문 여부 표시

    q = deque()

    for virus in virus_list:
        virus_i, virus_j = virus[0], virus[1]
        times[virus_i][virus_j] = 0 # 처음 지점은 소요시간 0
        visited[virus_i][virus_j] = 1
        q.append((virus_i, virus_j))

    # print("visited Before")
    # for i in range(N):
    #     print(visited[i])

    while q:
        curr_i, curr_j = q.popleft()

        for x in range(4): # 상 하 좌 우
            next_i = curr_i + di[x]
            next_j = curr_j + dj[x]
            # print("next_i, next_j :", next_i, next_j)
            if 0 <= next_i < N and 0 <= next_j < N:
                if visited[next_i][next_j] == 0:
                    if lab[next_i][next_j] != 1:
                        visited[next_i][next_j] = 1 # 방문 표시
                        q.append((next_i, next_j))
                        times[next_i][next_j] = times[curr_i][curr_j] + 1 # 해당 지점 소요시간 + 1

                        if times[next_i][next_j] >= total_min_time: # 지금까지 해본 경우들에서의 가장 적은 소요시간을 넘어서는 경우 더 해볼 필요 X
                            # print("shit")
                            break
    # print("times")
    # for i in range(N):
    #     print(times[i])

    count = 0 # 방문한 지점들의 수
    # print("visited After")
    for i in range(N):
        # print(visited[i])
        count += visited[i].count(1)

    # print("count", count)

    result_time = 0
    if count == goal:
        for i in range(N):
            for j in range(N):
                # 바이러스가 있던 지점인 경우, 해당 지점의 소요시간은 넘어감
                if lab[i][j] != 1 and (i, j) not in total_virus_list:
                    result_time = max(result_time, times[i][j])

        # print(result_time)
        return result_time

    return 1e9





if __name__ == "__main__":
    N, M = map(int, input().split())

    lab = [[] for _ in range(N)] # 연구소 상태
    total_virus_list = deque()

    wall = 0 # 벽의 개수
    for i in range(N):
        lab[i] = list(map(int, input().split()))
        wall += lab[i].count(1) # 벽 개수 카운트
        for j in range(N):
            if lab[i][j] == 2:
                total_virus_list.append((i, j))

    goal = N * N - wall # 바이러스가 있을 수 있는 칸 수
    # print("goal", goal)
    total_min_time = 1e9

    # print("total_virus_list :", total_virus_list)
    # print("list(combinations(total_virus_list, M)) :", list(combinations(total_virus_list, M)))
    # M개를 활성시키는 경우의 수만큼 수행
    # print("len :", len(list(combinations(total_virus_list, M))))
    for virus_list in list(combinations(total_virus_list, M)):
        # print("virus :", virus_list)
        temp_time = spread(lab, virus_list)
        total_min_time = min(total_min_time, temp_time)

    if total_min_time == 1e9:
        print(-1)
        # print("hi")
    else:
        import sys
        import copy
        from itertools import combinations
        from collections import deque

        input = sys.stdin.readline

        # 상 하 좌 우 에 대한 움직임
        di = [-1, 1, 0, 0]
        dj = [0, 0, -1, 1]


        #
        def spread(lab, virus_list):
            times = [[-1 for _ in range(N)] for _ in range(N)]  # 각 지점에 바이러스가 활성되는 시간을 담음
            visited = [[0 for _ in range(N)] for _ in range(N)]  # 각 지점에 대한 방문 여부 표시

            q = deque()

            for virus in virus_list:
                virus_i, virus_j = virus[0], virus[1]
                times[virus_i][virus_j] = 0  # 처음 지점은 소요시간 0
                visited[virus_i][virus_j] = 1
                q.append((virus_i, virus_j))

            # print("visited Before")
            # for i in range(N):
            #     print(visited[i])

            while q:
                curr_i, curr_j = q.popleft()

                for x in range(4):  # 상 하 좌 우
                    next_i = curr_i + di[x]
                    next_j = curr_j + dj[x]
                    # print("next_i, next_j :", next_i, next_j)
                    if 0 <= next_i < N and 0 <= next_j < N:
                        if visited[next_i][next_j] == 0:
                            if lab[next_i][next_j] != 1:
                                visited[next_i][next_j] = 1  # 방문 표시
                                q.append((next_i, next_j))
                                times[next_i][next_j] = times[curr_i][curr_j] + 1  # 해당 지점 소요시간 + 1

                                if times[next_i][next_j] >= total_min_time:  # 지금까지 해본 경우들에서의 가장 적은 소요시간을 넘어서는 경우 더 해볼 필요 X
                                    # print("shit")
                                    break
            # print("times")
            # for i in range(N):
            #     print(times[i])

            count = 0  # 방문한 지점들의 수
            # print("visited After")
            for i in range(N):
                # print(visited[i])
                count += visited[i].count(1)

            # print("count", count)

            result_time = 0
            if count == goal:
                for i in range(N):
                    for j in range(N):
                        # 바이러스가 있던 지점인 경우, 해당 지점의 소요시간은 넘어감
                        if lab[i][j] != 1 and (i, j) not in total_virus_list:
                            result_time = max(result_time, times[i][j])

                # print(result_time)
                return result_time

            return 1e9


        if __name__ == "__main__":
            N, M = map(int, input().split())

            lab = [[] for _ in range(N)]  # 연구소 상태
            total_virus_list = deque()

            wall = 0  # 벽의 개수
            for i in range(N):
                lab[i] = list(map(int, input().split()))
                wall += lab[i].count(1)  # 벽 개수 카운트
                for j in range(N):
                    if lab[i][j] == 2:
                        total_virus_list.append((i, j))

            goal = N * N - wall  # 바이러스가 있을 수 있는 칸 수
            # print("goal", goal)
            total_min_time = 1e9

            # print("total_virus_list :", total_virus_list)
            # print("list(combinations(total_virus_list, M)) :", list(combinations(total_virus_list, M)))
            # M개를 활성시키는 경우의 수만큼 수행
            # print("len :", len(list(combinations(total_virus_list, M))))
            for virus_list in list(combinations(total_virus_list, M)):
                # print("virus :", virus_list)
                temp_time = spread(lab, virus_list)
                total_min_time = min(total_min_time, temp_time)

            if total_min_time == 1e9:
                print(-1)
                # print("hi")
            else:
                print(total_min_time)
        print(total_min_time)