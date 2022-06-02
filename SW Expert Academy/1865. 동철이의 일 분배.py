# 1865. 동철이의 일 분배
"""
직원들에게 해야 할 일을 하나씩 배분
“주어진 일이 모두 성공할 확률”의 최댓값을 구하는 프로그램

max_heap 을 이용하면 어떨까

dfs로 풀어보기
"""


def dfs(cur_index, cur_percent):
    global max_percent

    if cur_percent <= max_percent: # 이미 max보다 작은 경우 -> 더 이상 해볼 필요가 없음
        return
    if cur_index == N: # 모든 직원들에게 일을 다 나눠준 경우 -> 확률 확인
        max_percent = max(max_percent, cur_percent)
        return

    for i in range(N):
        if not visited[i]: # i번째 일(아직 방문하지 않은 일)에 대해 cur_index번째 직원이 수행
            next_index = cur_index + 1
            next_percent = cur_percent * P[cur_index][i] * 0.01

            visited[i] = 1 # i번째 일 수행함을 표시 -> 방문표시
            dfs(next_index, next_percent)
            visited[i] = 0 # i + 1 번째 일에 대해 수행하는 걸 시도하기전에 i번째 일에 대해 수행함을 표시한걸 돌려둠


if __name__ == "__main__":
    T = int(input())

    for test_case in range(1, T + 1):
        N = int(input()) # 1 ~ 16 -> 전체 확률 개수 최대 256개 -> 그냥 전부 다 sort해도 괜찮을듯
        P = []
        for i in range(N):
            line = list(map(int, input().split())) # 0 ~ 100 정수로 퍼센트를 표현
            P.append(line)

        visited = [0 for _ in range(N)] # 방문확인

        max_percent = 0 # 현재까지 최대 확률을 업데이트 해나감
        dfs(0, 1)

        # 소수점 6번째
        print("#{} {:.6f}".format(test_case, max_percent * 100))
