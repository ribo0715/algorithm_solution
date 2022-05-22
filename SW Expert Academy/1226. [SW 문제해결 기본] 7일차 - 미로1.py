# 1226. [SW 문제해결 기본] 7일차 - 미로1

"""
미로 해결 방법이 있는지 확인 -> bfs
길을 따라 계속 이동 -> 더는 이동할 곳이 없으면 끝
"""

from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

if __name__ == "__main__":
    for _ in range(10):
        test_case = int(input())
        miro = []
        start_x, start_y = 0, 0

        for x in range(16):
            line = list(map(int, list(input()))) # string으로 "1111001111" 이런식으로 되어있는걸 [1, 1, 1, 1, ... , 1, 1] 로 바꿈
            miro.append(line)

            if 2 in line:
                start_x = x
                start_y = line.index(2)
        # print(start_x, start_y)
        q = deque()
        q.append([start_x, start_y])

        is_reachable = 0 # 도달 불가능함을 default로 설정

        while q:
            cur_x, cur_y = q.popleft()

            for i in range(4):
                next_x = cur_x + dx[i]
                next_y = cur_y + dy[i]

                if 0 <= next_x < 16 and 0 <= next_y < 16:
                    if miro[next_x][next_y] == 3:
                        is_reachable = 1
                        # print("hi")
                        break

                    elif miro[next_x][next_y] == 1:
                        continue

                    elif miro[next_x][next_y] == 0: # 이동 가능
                        miro[next_x][next_y] = 1
                        q.append([next_x, next_y])

            if is_reachable:
                break

        print("#{} {}".format(test_case, is_reachable))