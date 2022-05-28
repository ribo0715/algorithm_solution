# 1861. 정사각형 방
"""
이동하려는 방이 존재해야 하고, 이동하려는 방에 적힌 숫자가 현재 방에 적힌 숫자보다 정확히 1 더 커야 한다.
처음 어떤 수가 적힌 방에서 있어야 가장 많은 개수의 방을 이동할 수 있는지
"""
# 상 하 좌 우 이동
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

if __name__ == "__main__":
    T = int(input())

    for test_case in range(1, T + 1):
        N = int(input())

        A = []
        for _ in range(N):
            line = list(map(int, input().split()))
            A.append(line)

        # 각 지점에서 시작했을때, 얼마나 더 이동할 수 있는지를 구함
        # A지점에서의 값이 x일때, B지점에서 다음으로 A지점으로 이동한 경우 B지점까지

        # 거꾸로 값이 1씩 줄어드는 방향으로 몇칸 움직일 수 있는지를 나타내면 어떨까? 이건 좀 별로인듯

        # 하나의 경로가 만들어진다면, 경로의 가장 첫번째가 중요함
        # 여러 경로들의 첫번째 시작 지점의 위치들을 저장

        visited = [[0 for _ in range(N)] for _ in range(N)]
        start_point_dic = {} # 경로의 시작지점 : count 를 담음

        for x in range(N):
            for y in range(N):
                # print((x, y), "시작")
                if visited[x][y] == 1: # 이미 방문한 지점이면
                    continue

                visited[x][y] = 1 # 방문표시

                start_num = A[x][y]
                cur_x, cur_y = x, y
                count = 1 # (x, y) 를 시작으로 해서 몇 개의 방을 갈 수 있는지

                flag = True
                finish = False
                while not finish and flag:
                    flag = False # 상 하 좌 우 로 이동할 수 없으면 flag == False

                    for i in range(4): # 상 하 좌 우에 이동할 수 있으면 이동
                        next_x = cur_x + dx[i]
                        next_y = cur_y + dy[i]

                        if 0 <= next_x < N and 0 <= next_y < N: # 경계 내
                            cur_num = A[cur_x][cur_y]
                            next_num = A[next_x][next_y]

                            if next_num == cur_num + 1: # 다음칸으로 이동할 수 있는 경우
                                visited[next_x][next_y] = 1  # 방문 표시

                                if next_num in start_point_dic: # (next_x, next_y) 에서의 경로 길이를 이미 구해놓은 경우, 해당 결과를 이용
                                    count += start_point_dic.pop(next_num) # 다음칸에서 시작하는 줄 알았던걸 현재부터로 업데이트해줌
                                    finish = True
                                else:
                                    count += 1
                                    cur_x, cur_y = next_x, next_y
                                    flag = True
                                break # 상하좌우 더 살피지 않고 바로 다음으로 이동

                start_point_dic[start_num] = count
                # print(count)

        # print(start_point_dic)
        temp = list(start_point_dic.items())
        temp.sort(key=lambda x: x[0])
        temp.sort(key = lambda x:x[1], reverse = True)
        # print(temp)

        max_start_num, max_count = temp[0]
        print("#{} {} {}".format(test_case, max_start_num, max_count))

"""
2
2
1 2
3 4
3
9 3 4
6 1 5
7 8 2
"""