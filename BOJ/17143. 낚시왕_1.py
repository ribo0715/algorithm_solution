# 17143. 낚시왕_1
"""
r x c 격자 => grid
r : 세로 길이, c : 가로 길이

낚시왕 - 맨 오른쪽 끝을 넘어가면 이동 끝
낚시왕 이동 -> 가까운 상어 잡음 -> 상어 이동
=> for king_loc in range(c): 로 전체 상황 확인

상어 이동
-> 칸/초, 경계를 넘으면 방향 반대로 이동
=> 상어의 현재 위치 (r, c), 속력 s, 방향 d, 크기 z 를 받아 1초 뒤 상태를 반환
=> 전체 상어들에 대해 이동시킨 후, 위치가 겹치는 경우 크기가 가장 큰 놈만 남기도록

각 상어들을 grid에서 관리하는 것이 좋을까?
따로 상어들의 상태를 두고 관리하는 것이 좋을까?
=> grid 각 칸에 상어가 위치한 경우,
(크기, 속력, 방향)을 담음

이동 후, 한 칸에 여러 상어가 있게 되면, 가장 큰 상어가 다 잡아먹어 없앰

낚시왕이 잡은 상어 크기의 합 => total_catch_shark_size
"""


def catch_shark(c):



def shark_move(shark_list):



if __name__ == "__main__":
    R, C, M = map(int, input().split())
    grid = [[[] for _ in range(C)] for _ in range(R)]

    for _ in range(M): # 상어 M마리의 정보 입력
        r, c, s, d, z = map(int, input().split())

    total_catch_shark_size = 0

    for cur_c in range(C - 1): # 낚시왕 이동
        catch_shark(cur_c) # cur_c 열에 있는 가장 가까운 상어를 잡음

        shark_move() # 상어 이동

    catch_shark(C - 1) # 마지막 칸에 도착한 상태에서, 상어를 잡음. 이후에는 상어를 굳이 이동시키지 않음

    print(total_catch_shark_size)

