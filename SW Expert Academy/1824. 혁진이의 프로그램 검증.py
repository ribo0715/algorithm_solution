# 1824. 혁진이의 프로그램 검증
"""
정지하지 못하는 경우를 어떻게 판단할 수 있을까? -> 위치와 방향이 같은 경우가 반복된 경우? -> (위치, 방향)에 대해 visited로 저장하면 될까?
-> "?" 때문에 이동 방향이 랜덤하게 되는 경우는 어떡하지...
-> 메모리에 저장되어있는 값도 신경써줘야할 것 같은데 -> 메모리에 있는 값도 함께 방문여부에서 생각

"@"에서부터 거꾸로 이동해서 출발지점에 도착할 수 있는지 확인? -> 메모리에 저장되어 있는 값을 알 수 없기 때문에 어려울 것 같음

정지할 수 있으면 "YES", 아니면 "NO"
"""

from collections import deque

# 상 하 좌 우 이동
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

if __name__ == "__main__":
    T = int(input())

    for test_case in range(1, T + 1):
        R, C = map(int, input().split())

        command = [[] for _ in range(R)]
        for i in range(R):
            command[i] = list(input())

        answer = "NO"

        start_r, start_c = 0, 0 # 현재 위치
        start_direction = 3 # 처음 이동 방향 : 오른쪽
        start_memory_value = 0 # 메모리에 저장된 정수

        visited = set()
        visited.add((start_r, start_c, start_direction, start_memory_value)) # (위치, 방향, 메모리값) 방문 표시

        q = deque()
        q.append((start_r, start_c, start_direction, start_memory_value))

        while q:
            cur_r, cur_c, cur_direction, cur_memory_value = q.popleft()

            next_direction = cur_direction
            next_memory_value = cur_memory_value

            cur_command = command[cur_r][cur_c]
            # print("현재 위치 :", (cur_r, cur_c), "/ 방향 :", cur_direction, "/ 메모리 값 :", cur_memory_value, "/ 커맨드 :",cur_command)

            if cur_command in ["^", "v", "<", ">"]:
                next_direction = ["^", "v", "<", ">"].index(cur_command)
                next_r = (cur_r + dr[next_direction]) % R  # 바깥으로 넘어가면 반대로
                next_c = (cur_c + dc[next_direction]) % C  # 바깥으로 넘어가면 반대로

                if (next_r, next_c, next_direction, next_memory_value) not in visited:
                    visited.add((next_r, next_c, next_direction, next_memory_value))
                    q.append((next_r, next_c, next_direction, next_memory_value))

            elif cur_command == "_":
                if cur_memory_value == 0:
                    next_direction = 3
                else:
                    next_direction = 2

                next_r = (cur_r + dr[next_direction]) % R  # 바깥으로 넘어가면 반대로
                next_c = (cur_c + dc[next_direction]) % C  # 바깥으로 넘어가면 반대로

                if (next_r, next_c, next_direction, next_memory_value) not in visited:
                    visited.add((next_r, next_c, next_direction, next_memory_value))
                    q.append((next_r, next_c, next_direction, next_memory_value))

            elif cur_command == "|":
                if cur_memory_value == 0:
                    next_direction = 1
                else:
                    next_direction = 0

                next_r = (cur_r + dr[next_direction]) % R  # 바깥으로 넘어가면 반대로
                next_c = (cur_c + dc[next_direction]) % C  # 바깥으로 넘어가면 반대로

                if (next_r, next_c, next_direction, next_memory_value) not in visited:
                    visited.add((next_r, next_c, next_direction, next_memory_value))
                    q.append((next_r, next_c, next_direction, next_memory_value))

            elif cur_command == "?": # 네 방향으로 모두 이동해봄
                for n in range(4):
                    next_direction = n
                    next_r = (cur_r + dr[next_direction]) % R  # 바깥으로 넘어가면 반대로
                    next_c = (cur_c + dc[next_direction]) % C  # 바깥으로 넘어가면 반대로

                    if (next_r, next_c, next_direction, next_memory_value) not in visited:
                        visited.add((next_r, next_c, next_direction, next_memory_value))
                        q.append((next_r, next_c, next_direction, next_memory_value))

            elif cur_command == ".":
                next_r = (cur_r + dr[next_direction]) % R  # 바깥으로 넘어가면 반대로
                next_c = (cur_c + dc[next_direction]) % C  # 바깥으로 넘어가면 반대로

                if (next_r, next_c, next_direction, next_memory_value) not in visited:
                    visited.add((next_r, next_c, next_direction, next_memory_value))
                    q.append((next_r, next_c, next_direction, next_memory_value))

            elif cur_command == "@":
                answer = "YES"
                break
                # print("#{} {}".format(test_case, "YES"))

            elif "0" <= cur_command <= "9":
                next_r = (cur_r + dr[next_direction]) % R  # 바깥으로 넘어가면 반대로
                next_c = (cur_c + dc[next_direction]) % C  # 바깥으로 넘어가면 반대로

                next_memory_value = int(cur_command)

                if (next_r, next_c, next_direction, next_memory_value) not in visited:
                    visited.add((next_r, next_c, next_direction, next_memory_value))
                    q.append((next_r, next_c, next_direction, next_memory_value))

            elif cur_command == "+":
                next_r = (cur_r + dr[next_direction]) % R  # 바깥으로 넘어가면 반대로
                next_c = (cur_c + dc[next_direction]) % C  # 바깥으로 넘어가면 반대로

                next_memory_value = (next_memory_value + 1) % 16

                if (next_r, next_c, next_direction, next_memory_value) not in visited:
                    visited.add((next_r, next_c, next_direction, next_memory_value))
                    q.append((next_r, next_c, next_direction, next_memory_value))

            elif cur_command == "-":
                next_r = (cur_r + dr[next_direction]) % R  # 바깥으로 넘어가면 반대로
                next_c = (cur_c + dc[next_direction]) % C  # 바깥으로 넘어가면 반대로

                next_memory_value = (next_memory_value - 1) % 16

                if (next_r, next_c, next_direction, next_memory_value) not in visited:
                    visited.add((next_r, next_c, next_direction, next_memory_value))
                    q.append((next_r, next_c, next_direction, next_memory_value))

        print("#{} {}".format(test_case, answer))

