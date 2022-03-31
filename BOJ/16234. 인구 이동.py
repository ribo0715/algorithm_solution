# 16234. 인구 이동


# 전체 칸을 확인하면서 인구 차이가 L ~ R 인 그룹들을 모음
def make_groups(grid, N, L, R):
    flag = True # 다시 수행해야할지를 나타냄
    dates = 0
    
    while flag:
        flag = False
        visited = [[0 for _ in range(N)] for _ in range(N)] # 해당 위치를 확인한 경우, 1로 바꿔줌

        for i in range(N):
            for j in range(N):
                # 확인한 곳이면 넘어감
                if visited[i][j] == 1:
                    continue

                count = 1
                union_list = [(i, j)] # 해당 칸을 리스트에 넣음
                visited[i][j] = 1 # 해당 칸 방문 표시
                union_list += find_union(grid, N, L, R,  visited, i, j)

                # union_list에 있는 칸들을 계속해서 확인해나가며 리스트에 추가, visited에도 추가
                while len(union_list) > 1:
                    if count == len(union_list): # union_list에 추가된 게 없으면, 더이상 확인하지 않음
                        break

                    for _ in range(len(union_list) - count):
                        temp_i, temp_j = union_list[count][0], union_list[count][1]
                        temp_union_list = find_union(grid, N, L, R, visited, temp_i, temp_j)
                        union_list += temp_union_list
                        count += 1

                if count > 1:
                    share_union(grid, union_list)
                    flag = True # 연합을 진행한 경우 다음날까지 확인

        if flag:
            dates += 1

    print(dates)
                    


# (i, j)의 인접한 칸을 확인하여 차이가 L~R 인곳들의 위치를 찾아 리스트에 넣어 반환
def find_union(grid, N, L, R, visited, i, j):
    union_list = []
    
    if i + 1 <= N - 1: # 오른쪽
        if L <= abs(grid[i][j] - grid[i + 1][j]) <= R and visited[i + 1][j] == 0:
            union_list.append((i + 1, j))
            visited[i + 1][j] = 1
            
    if i - 1 >= 0: # 왼쪽
        if L <= abs(grid[i][j] - grid[i - 1][j]) <= R and visited[i - 1][j] == 0:
            union_list.append((i - 1, j))
            visited[i - 1][j] = 1

    if j + 1 <= N - 1: # 아래
        if L <= abs(grid[i][j] - grid[i][j + 1]) <= R and visited[i][j + 1] == 0:
            union_list.append((i, j + 1))
            visited[i][j + 1] = 1

    if j - 1 >= 0: # 위
        if L <= abs(grid[i][j] - grid[i][j - 1]) <= R and visited[i][j - 1] == 0:
            union_list.append((i, j - 1))
            visited[i][j - 1] = 1

    return union_list


# 연합내의 칸들을 평균내어 값을 변경해줌
def share_union(grid, group):
    count = len(group) # 연합에 속한 칸 수
    total_num = 0
    
    for  A in group:
        i, j = A[0], A[1]
        total_num += grid[i][j] # 연합 총 인구수

    average_num = total_num // count # 평균 인구수

    for  A in group:
        i, j = A[0], A[1]
        grid[i][j] = average_num # 평균 인구수로 바꿔줌






import sys
input = sys.stdin.readline

if __name__ == "__main__":
    N, L, R = map(int, input().split())

    grid = [[] for _ in range(N)]
    for i in range(N):
        grid[i] = list(map(int, input().split()))

    make_groups(grid, N, L, R)
        










