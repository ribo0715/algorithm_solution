# 13460. 구슬 탈출 2_(2)
"""
직사각형 보드에 빨간 구슬과 파란 구슬을 하나씩 넣은 다음, 빨간 구슬을 구멍을 통해 빼내는 게임
파란 구슬이 구멍에 들어가면 안됨 -> 빨간 구슬과 동시에 들어가도 안됨

(파란구슬 이동 -> 빨간구슬 이동 -> 파란구슬 이동) 이런 방법으로 움직일까?

최소 몇 번 만에 빨간 구슬을 구멍을 통해 빼낼 수 있는지 반환
10번안에 성공하지 못하면 -1 반환

빨간구슬, 파란구슬의 위치를 저장 -> bfs
상, 하, 좌, 우 로 이동해감
"""


from collections import deque
import sys
input = sys.stdin.readline


if __name__ == "__main__":
    N, M = map(int, input().split()) # 세로, 가로
    rx, ry, bx, by = 0, 0, 0, 0 # 빨간구슬, 파란구슬의 위치

    board = []
    for i in range(N): # 보드의 모양
        line = list(input())
        if "R" in line:
            j = line.index("R")
            rx, ry = i, j
            line[j] = "."
        if "B" in line:
            j = line.index("B")
            bx, by = i, j
            line[j] = "."

        board.append(line)

    q = deque()
    q.append([rx, ry, bx, by])
    count = 0

    visited = []
    visited.append([rx, ry, bx, by])

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    # bfs
    while q and count < 10:
        count += 1
        # print(q)
        for _ in range(len(q)):
            cur_rx, cur_ry, cur_bx, cur_by = q.popleft()
            # print(cur_rx, cur_ry, cur_bx, cur_by, "에서 출발")
            for i in range(4): # 상 하 좌 우 로 이동
                next_rx, next_ry, next_bx, next_by = cur_rx, cur_ry, cur_bx, cur_by
                # 끝까지 이동
                while board[next_rx + dx[i]][next_ry + dy[i]] not in ["#", "O"]:  # 벽이나 구멍
                    next_rx += dx[i]
                    next_ry += dy[i]

                while board[next_bx + dx[i]][next_by + dy[i]] not in ["#", "O"]: # 벽이나 구멍
                    next_bx += dx[i]
                    next_by += dy[i]

                # print([next_rx, next_ry, next_bx, next_by])
                # if [next_rx, next_ry, next_bx, next_by] in visited:
                #     continue



                if board[next_bx + dx[i]][next_by + dy[i]] == "O": # 파란구슬이 빠진 경우
                    continue

                elif board[next_rx + dx[i]][next_ry + dy[i]] == "O": # 빨간구슬만 빠진 경우
                    print(count)
                    exit()

                elif [next_rx, next_ry] == [next_bx, next_by]: # 빨간구슬, 파란구슬이 같은 위치에 도달한 경우
                    move_r = abs(next_rx - cur_rx) + abs(next_ry - cur_ry)
                    move_b = abs(next_bx - cur_bx) + abs(next_by - cur_by)

                    if move_r < move_b: # 빨간구슬이 먼저 해당 지점에 도착 -> 파란구슬은 한칸 뒤로
                        next_bx -= dx[i]
                        next_by -= dy[i]
                    else:
                        next_rx -= dx[i]
                        next_ry -= dy[i]

                    if [next_rx, next_ry, next_bx, next_by] in visited:
                        continue

                    q.append([next_rx, next_ry, next_bx, next_by])
                    visited.append([next_rx, next_ry, next_bx, next_by])

                else:
                    if [next_rx, next_ry, next_bx, next_by] in visited:
                        continue

                    q.append([next_rx, next_ry, next_bx, next_by])
                    visited.append([next_rx, next_ry, next_bx, next_by])

    print(-1)
