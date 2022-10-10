# 네트워크
"""
컴퓨터 개수 n
연결 정보 computers -> computers[i][j] -> i번과 j번이 연결되어있는지

총 네트워크의 개수 return

1번 컴퓨터부터 bfs로 가면 될 듯
네트워크가 만들어지면
"""

from collections import deque
from collections import defaultdict


def dfs(n, graph):
    visited = [0] * n  # i번을 확인했는지 체크
    network_count = 0

    for i in range(n):  # i번이 연결된 네트워크 확인
        if visited[i]:  # 방문한 경우 넘어감
            continue

        network_count += 1 # 네트워크 수 체크

        cur_visited = []  # 현재 방문한 컴퓨터 번호
        need_visited = deque()  # 방문해야할 컴퓨터 번호

        # 시작 노드 설정해주기
        need_visited.append(i)  # i번에서 시작

        # 방문이 필요한 리스트가 아직 존재한다면
        while need_visited:
            computer = need_visited.pop() # 시작 노드를 지정
            visited[computer] = 1  # i번 컴퓨터를 확인했는지 표시

            # 만약 방문한 리스트에 없다면
            if computer not in cur_visited:
                # 방문 리스트에 노드를 추가
                cur_visited.append(computer)
                # 인접 노드들을 방문 예정 리스트에 추가
                need_visited.extend(graph[computer])

    return network_count


def solution(n, computers):
    graph = defaultdict(list)
    for x in range(n):
        for y in range(x, n):
            if x != y and computers[x][y] == 1:
                graph[x].append(y)
                graph[y].append(x)

    answer = dfs(n, graph)

    return answer

