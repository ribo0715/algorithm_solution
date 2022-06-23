# 1258. [SW 문제해결 응용] 7일차 - 행렬찾기
"""
부분 행렬의 열의 개수는 서로 다르며 행렬의 행의 개수도 서로 다르다


"""



if __name__ == "__main__":
    T = int(input())

    for test_case in range(1, T + 1):
        n = int(input())
        grid = []
        for _ in range(n):
            line = list(map(int, input().split()))
            grid.append(line)

        visited = [[0 for _ in range(n)] for _ in range(n)]

        sub_matrix_list = [] # 부분행렬에 대한 정보들을 담음
        for i in range(n):
            for j in range(n):
                if visited[i][j]: # 이미 확인했으면 넘어감
                    continue

                if grid[i][j]: # 0이 아닌 수가 있는 경우 -> 어떤 부분 행렬의 가장 왼쪽 위에 위치
                    cur_row = 1 # 현재 부분 행렬의 행
                    cur_column = 1 # 현재 부분 행렬의 열

                    right = i + 1
                    down = j + 1
                    while True:
                        if right < n:
                            if grid[right][j]: # 오른쪽으로 이동
                                cur_row += 1
                                right += 1
                                continue
                        break

                    while True:
                        if down < n:
                            if grid[i][down]:
                                cur_column += 1
                                down += 1
                                continue
                        break

                    for row in range(cur_row):
                        for column in range(cur_column):
                            visited[i + row][j + column] = 1


                    # cur_row행, cur_column열 의 부분 행렬에 대한 정보(행의 크기, 열의 크기)를 넣음
                    sub_matrix_list.append([cur_row, cur_column])

        sub_matrix_list.sort() # 행이 작은 순으로 정렬
        sub_matrix_list.sort(key=lambda x:(x[0] * x[1]))

        answer = str(len(sub_matrix_list))
        for sub_matrix in sub_matrix_list:
            answer += " " + str(sub_matrix[0]) + " " + str(sub_matrix[1])

        print("#{} {}".format(test_case, answer))

"""
1
9
1 1 3 2 0 0 0 0 0
3 2 5 2 0 0 0 0 0
2 3 3 1 0 0 0 0 0
0 0 0 0 4 5 5 3 1
1 2 5 0 3 6 4 2 1
2 3 6 0 2 1 1 4 2
0 0 0 0 4 2 3 1 1
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
"""
