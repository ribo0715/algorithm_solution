# 1251. [SW 문제해결 응용] 4일차 - 하나로
"""
우선 trim, kruskal 방법을 떠올림

1) 길이가 짧은 순서로 정렬해서 하는 방법

2) 각 점에서 가장 거리가 짧은 곳으로 연결
"""


def get_min(x_list, y_list, N, E):
    cost_list = []
    # 각 지점 사이의 거리들을 계산
    for i in range(N - 1):
        x1, y1 = x_list[i], y_list[i]
        for j in range(i + 1, N):
            x2, y2 = x_list[j], y_list[j]
            cost = calc_cost(x1, y1, x2, y2, E)

            cost_list.append([cost, i, j])

    cost_list.sort() # cost가 작은 순서대로 정렬 -> heapq 를 사용하면 성능이 더 좋아질 듯(수정해보기)

    # visited = set()
    total_min_cost = 0

    group = [i for i in range(N)] # 각 지점이 연결되어있는 그룹의 중심이 어디인지를 저장 -> 최초엔 자기 자신에 연결

    for temp_cost, temp_i, temp_j in cost_list:
        # if len(visited) == N:
        #     break

        # (0, 1)을 연결하고 (2, 3)을 연결해도 다 들어갔다고 파악하는 문제점
        # -> 각 set별로 나누고 합쳐지게 되면 합쳐야할까?
        # if temp_i in visited and temp_j in visited: # 두 점 다 연결된 경우
        #     continue
        # else:

        # 끝까지 다 해보지 않고 중간에 멈출 수 있는 방법이 없을까?

        group_i, group_j = temp_i, temp_j
        while group_i != group[group_i]:  # temp_j가 속한 그룹의 중심을 찾음
            group_i = group[group_i]

        while group_j != group[group_j]: # temp_j가 속한 그룹의 중심을 찾음
            group_j = group[group_j]

        if group_i != group_j: # 다른 그룹에 연결된 경우, 합쳐줌
            group[group_j] = group_i

            total_min_cost += temp_cost

            # print(temp_i, "번째", (x_list[temp_i], y_list[temp_i]), "와", temp_j, "번째", (x_list[temp_j], y_list[temp_j]), "연결 -> 비용 :", temp_cost)



    return round(total_min_cost) # 소수점 첫째 자리 반올림

    # 어디 어디를 연결한 것인지, 둘 다 visited에 있으면 넘김



def calc_cost(x1, y1, x2, y2, E):
    return E * ((x1 - x2) ** 2 + (y1 - y2) ** 2)


if __name__ == "__main__":
    T = int(input())

    for test_case in range(1, T + 1):
        answer = 0

        N = int(input())
        x_list = list(map(int, input().split()))
        y_list = list(map(int, input().split()))
        E = float(input())

        answer = get_min(x_list, y_list, N, E)

        print("#{} {}".format(test_case, answer))
