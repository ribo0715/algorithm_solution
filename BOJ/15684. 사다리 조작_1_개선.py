
"""
세로선 개수 N(넓이 N-1), 높이 H
놓인 가로선 개수 M
M개의 가로선 위치 (a, b) -> a번 가로선 위, b, b+1 세로선 사이 연결

풀이) -> 시간초과
가로선의 위치들을 입력받은 뒤, 추가로 둘 수 있는 위치들을 찾아냄

(가로선들의 위치가 담긴 상태) 를 받아, 해당 상태에서 추가할 수 있는 곳에 추가한 상태를 다시 넣어가도록
3개를 추가하는 것 까지만 확인하고 되지 않은 경우, -1 반환

개선)
모든 지점들에 대해 확인하는 것이 아니라, 구역별로 같은 결과를 내는 곳들을 묶어 확인하면 어떨까?

"""

from collections import deque

# 가로선 상태를 받아, 각 결과가 어떻게 나오는지 확인
# i번에서 출발해서 i번으로 모두 도착하면 True
def test(cur_list, N, H):
    for i in range(1, N + 1):
        y = i # 첫째줄, i번째 칸에서 시작 -> H번째 줄까지 내려가야함
        for x in range(1, H + 1):
            if [x, y - 1] in cur_list: # 왼쪽으로 이동
                y -= 1
            elif [x, y] in cur_list: # 오른쪽으로 이동
                y += 1

        if y != i: # i번으로 도착하지 않은 경우 바로 False
            return False

    return True


def get_next_list(cur_list, N, H):
    able_list = []
    for x in range(1, H + 1):
        for y in range(1, N + 1):
            if [x, y] in cur_list:
                continue
            elif [x, y - 1] in cur_list:
                continue
            elif [x, y + 1] in cur_list:
                continue
            else: # 추가 가능한 지점들을 담음
                able_list.append([x, y])

    return able_list


if __name__ == "__main__":
    N, M, H = map(int, input().split())

    ladders = [[1 for _ in range(N)] for _ in range(H)] # 1인 곳에는 가로선을 둘 수 있는 위치

    # 가로선의 위치를 담음
    temp_list = []
    for _ in range(M):
        a, b = map(int, input().split())
        temp_list.append([a, b])
    # temp_list.sort() # 굳이 안해도 될 듯

    q = deque()
    q.append(temp_list)

    for added_num in range(4):
        for _ in range(len(q)):
            cur_list = q.popleft() # 현재 상태

            # 현재 상태에서 해보고 되면 몇개를 추가한 상황인지 반환
            if test(cur_list, N, H):
                print(added_num)
                exit()
            # 안되면 현재 상태에서 추가할 수 있는 위치에 추가해서 다시2 0 3 q에 넣음
            else:
                next_able_list = get_next_list(cur_list, N, H)
                for next_able in next_able_list:
                    next_list = cur_list + [next_able]
                    q.append(next_list)

    print("-1")


