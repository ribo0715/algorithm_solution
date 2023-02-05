
"""
세로선 개수 N(넓이 N-1), 높이 H
놓인 가로선 개수 M
M개의 가로선 위치 (a, b) -> a번 가로선 위, b, b+1 세로선 사이 연결

풀이)
dfs로 해당 상태에서 하나씩 사다리 두는 곳을 늘려가면서 확인

* 하나의 가로선을 추가한다는 것의 의미는?
-> 가로선이 a, a+1번째 세로줄 사이에 들어가게 되면,
해당 지점을 지나가던 두개의 결과가 바뀌게 되는 것
-> 두개를 추가한 상황에서 최종 결과가 두개보다 많이 다른 경우는 하나를 더 추가하더라도 불가능
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


# 아녀
def dfs():
    



if __name__ == "__main__":
    N, M, H = map(int, input().split())

    ladders = [[0 for _ in range(N)] for _ in range(H)] # 1인 곳에는 가로선이 있는 곳

    for _ in range(M):
        a, b = map(int, input().split())
        ladders[a - 1][b - 1] = 1 # 가로선 표시

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


