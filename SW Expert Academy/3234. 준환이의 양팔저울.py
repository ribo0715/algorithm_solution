# 3234. 준환이의 양팔저울
"""
무게추를 올리는 방법 -> 순서에도 영향 o
-> N이 작으므로 하나씩 해봐도 괜찮을듯

추를 올릴 때, 오른쪽 무게의 총합이 왼쪽 무게의 총합보다 더 커져서는 안됨
"""

from collections import deque
import copy

if __name__ == "__main__":
    T = int(input())

    for test_case in range(1, T + 1):
        N = int(input())
        line = list(map(int, input().split())) # 각 무게추 무게 input
        line.sort()

        answer = 0

        q = deque()

        # 처음엔 1개를 무조건 왼쪽에 올려야함
        for i in range(N):
            temp = copy.deepcopy(line)
            left = [temp.pop(i)]
            right = []

            q.append([temp, left, right])  # q에 [temp, left, right]를 저장

        total_method = deque()
        while q:
            temp, left, right = q.popleft()

            if not temp:
                answer += 1

            for i in range(len(temp)): # temp[i]를 담음
                next_temp = copy.deepcopy(temp)
                target = next_temp.pop(i)
                if sum(left) >= sum(right) + target: # 오른쪽에도 둘 수 있는 경우
                    q.append([next_temp, left, right + [target]])

                q.append([next_temp, left + [target], right])

        print("#{} {}".format(test_case, answer))


