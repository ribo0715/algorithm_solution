# 1211. [SW 문제해결 기본] 2일차 - Ladder2
"""
바닥까지 가장 짧은 이동 거리를 갖는 시작점 x(복수 개인 경우 가장 큰 x좌표)를 반환
"""


if __name__ == "__main__":
    T = 10

    for test_case in range(1, T + 1):
        test_case_num = int(input())

        grid = []
        start_y_list = [] # 맨 위 시작지점의 index를 담을 리스트

        for _ in range(100):
            line = list(map(int, input().split()))
            grid.append(line)

        for i in range(100):
            if grid[0][i] == 1:
                # print(i)
                start_y_list.append(i)

        min_count = 1e9
        answer = 0

        for start_y in start_y_list:
            cur_x, cur_y = 0, start_y
            count = 0
            already_end = False
            while cur_x < 99: # 맨 아래에 도착할때까지 이동
                if already_end: # 이미 min_count 보다 커진 경우 -> 굳이 더이상 하지 않아도 됨
                    break

                # 왼쪽으로 이동할 수 있으면 계속 이동
                if cur_y > 0:
                    if grid[cur_x][cur_y - 1] == 1:
                        while True:
                            if cur_y > 0:
                                if grid[cur_x][cur_y - 1] == 1:
                                    cur_y -= 1
                                    count += 1
                                    # print(cur_x, "줄에서 왼쪽으로 계속 이동중~")
                                    if count > min_count:
                                        already_end = True
                                        break
                                else:
                                    break
                            else:
                                break

                        cur_x += 1
                        continue

                # 오른쪽으로 이동할 수 있으면 계속 이동
                if cur_y < 99:
                    if grid[cur_x][cur_y + 1] == 1:
                        while True:
                            if cur_y < 99:
                                if grid[cur_x][cur_y + 1] == 1:
                                    cur_y += 1
                                    count += 1
                                    # print(cur_x, "줄에서 오른쪽으로 계속 이동중~")
                                    if count > min_count:
                                        already_end = True
                                        break
                                else:
                                    break
                            else:
                                break
                        cur_x += 1
                        continue

                # 아래로 내려감
                cur_x += 1

            if min_count >= count:
                min_count = count
                answer = start_y

        print("#{} {}".format(test_case, answer))

