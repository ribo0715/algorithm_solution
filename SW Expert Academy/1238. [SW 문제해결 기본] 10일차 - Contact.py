# 1238. [SW 문제해결 기본] 10일차 - Contact
"""
비상연락망과 연락을 시작하는 당번에 대한 정보
-> 가장 나중에 연락을 받게 되는 사람 중 번호가 가장 큰 사람
"""
import copy
from collections import defaultdict
from collections import deque

if __name__ == "__main__":
    T = 10
    for test_case in range(1, T + 1):
        length, start = map(int, input().split())

        line = list(map(int, input().split()))

        dic = defaultdict(list)
        for i in range(length // 2):
            from_num = line[2 * i]
            to_num = line[2 * i + 1]
            dic[from_num].append(to_num)

        visited = [start]

        q = deque()
        q.append(start)
        latest = []
        count = 1
        while q:
            latest = copy.deepcopy(list(q))  # 이번에 연락을 받는 사람들의 번호

            for _ in range(len(q)):
                cur = q.popleft()
                for next in dic[cur]:
                    if next not in visited:
                        q.append(next)
                        visited.append(next)

            count += 1

        answer = sorted(latest)[-1]
        print("#{} {}".format(test_case, answer))

