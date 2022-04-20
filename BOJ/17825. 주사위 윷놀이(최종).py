# 17825. 주사위 윷놀이

"""
처음에는 시작 칸에 말 4개

화살표의 방향대로만 이동
말이 파란색 칸에서 이동을 시작하면 파란색 화살표를 타야 하고
이동하는 도중이거나 파란색이 아닌 칸에서 이동을 시작하면 빨간색 화살표를 타야 한다

말이 도착 칸으로 이동하면 주사위에 나온 수와 관계 없이 이동을 마친다

게임은 10개의 턴

매 턴마다 1부터 5까지 한 면에 하나씩 적혀있는 5면체 주사위를 굴리고
도착 칸에 있지 않은 말을 하나 골라 주사위에 나온 수만큼 이동

말이 이동을 마치는 칸에 다른 말이 있으면 그 말은 고를 수 없다
이동을 마치는 칸이 도착 칸이면 고를 수 있다

말이 이동을 마칠 때마다 칸에 적혀있는 수가 점수에 추가

주사위에서 나올 수 10개를 미리 알고 있을 때, 얻을 수 있는 점수의 최댓값을 구해보자

"""

# 게임판을 어떻게 나타낼 수 있을까

# piece -> 말들의 현재 위치를 저장
import copy
from collections import deque
import sys
input = sys.stdin.readline

# bfs 방법으로 늘려가는 게 좋을듯 -> 현재 말들의 위치를 나타내는 배열들로
def bfs():
    piece = [0, 0, 0, 0] # 각 말의 위치를 담을 배열 -> sort하여 같은 상태를 구별하도록
    q = deque()
    q.append(piece)

    q_score = deque() # 현재까지 점수
    q_score.append(0)


    for i in range(10): # 주사위 10번
        # print("===========================")
        # print((i+1), "번째 주사위 값 :", dice_numbers[i])

        visited = deque()

        for _ in range(len(q)):
            piece = q.popleft()
            score = q_score.popleft()

            # print()
            # print("현재 piece :", piece)
            # print("현재 점수 :", score)
            # print()
            for j in range(4): # 말 4개
                if piece[j] == -1: # 도착한 말은 이동 X
                    continue

                destination = get_destination(piece[j], dice_numbers[i])
                # print("target :", piece[j], "-> destination :", destination)
                # 이동할 위치에 다른 말이 있는 경우, 고를 수 없음
                if destination in piece and destination != -1: # 도착으로 이동하는 경우는 가능
                    # print("-> 이동할 수 없음 -> 탈락")
                    continue

                temp_piece = copy.deepcopy(piece)
                temp_piece[j] = destination

                temp_piece = sorted(temp_piece)

                if temp_piece in visited:
                    # print("-> 이미 존재하는 piece :", temp_piece)
                    same_piece_score = q_score[q.index(temp_piece)]

                    # 점수가 이미 있는 것보다 높은 경우는 넣어줌 -> 이 부분이다!
                    if destination >= 100:
                        plus_score = destination // 10
                    elif destination == -1:  # 도착지점
                        plus_score = 0
                    else:
                        plus_score = destination

                    if score + plus_score > same_piece_score:
                        # print("But, 더 점수가 높은 경우가 존재! 합산점수 :", score + plus_score)
                        # q_score[q.index(temp_piece)] = score + plus_score # -> 값을 바꿔주는게 아니라, 뒤에 넣어줘야함
                        q.append(temp_piece)
                        q_score.append(score + plus_score)



                if temp_piece not in visited:
                    # print("q에 집어넣을 piece :", temp_piece)
                    q.append(temp_piece)
                    visited.append(temp_piece)

                    if destination >= 100:
                        plus_score = destination // 10
                    elif destination == -1: # 도착지점
                        plus_score = 0
                    else:
                        plus_score = destination
                    q_score.append(score + plus_score)
                    # print("추가점수 :", plus_score, "점 -> 합산점수 :", score + plus_score)

        # print()
        # print("주사위", (i+1), "번 던졌을때 가능한 위치들 목록")
        # print(visited)
        # print("현재까지 합산 점수 목록")
        # print(q_score)
        # print()

    # print("최대 점수 :", max(q_score))
    print(max(q_score))

# 중간에 있는 숫자들은 10을 곱하여 표시하는 건 어떨까 -> 같은 숫자와 구별하기 위함



# 현재 위치 start에서 n칸 이동할 때 도착 위치를 구하는 함수
def get_destination(start, n):
    end = start
    if 100 <= start <= 190: # 10, 13, 16, 19
        x = (220 - start) // 30 # 250 까지 이동할 칸

        if n >= x: # 250 자리를 지나갈 수 있는 경우
            end = 250
            end += 50 * (n - x)
        else:
            end += 30 * n

    elif 200 <= start <= 240: # 20, 22, 24
        x = (260 - start) // 20 # 250 까지 이동할 칸 수

        if n >= x: # 250 자리를 지나갈 수 있는 경우
            end = 250
            end += 50 * (n - x)
        else:
            end += 20 * n

    elif start in (250, 300, 350, 400): # 25, 30, 35, 40
        end += 50 * n


    elif 260 <= start <= 280 or start == 30: # 30, 28, 27, 26
        if start == 30:
            start = 290
            # print("here,", start)

        x = (start - 250) // 10

        if n >= x: # 250 자리를 지나갈 수 있는 경우
            end = 250
            end += 50 * (n - x)
        else:
            end = start - 10 * n

    else: # 2씩 증가 -> 40이상이 되면 도착
        end += 2 * n

        if end > 40: # 바깥쪽 길로 가서 도착
            # 도착
            end = -1
            # print("바깥쪽 길로 가서 도착 -> 끝")

        if end in (10, 20, 40):
            end *= 10


    if end > 400: # 도착
        end = -1
        # print("안쪽 길로 가서 도착 -> 끝")

    return end




if __name__ == "__main__":
    # 첫째 줄에 주사위에서 나올 수 10개가 순서대로 주어진다
    dice_numbers = list(map(int, input().split())) # 1 ~ 5

    bfs()

