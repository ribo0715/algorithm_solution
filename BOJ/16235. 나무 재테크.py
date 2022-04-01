# 16235. 나무 재테크


"""
칸은 (r, c)로 나타내며
r은 가장 위에서부터 떨어진 칸의 개수, c는 가장 왼쪽으로부터 떨어진 칸의 개수
r과 c는 1부터 시작

가장 처음에 양분은 모든 칸에 5만큼 들어있다

M개의 나무
같은 1×1 크기의 칸에 여러 개의 나무가 심어져 있을 수도 있다

봄에는 나무가 자신의 나이만큼 양분을 먹고, 나이가 1 증가
각각의 나무는 나무가 있는 1×1 크기의 칸에 있는 양분만 먹을 수 있다
하나의 칸에 여러 개의 나무가 있다면, 나이가 어린 나무부터 양분을 먹는다
땅에 양분이 부족해 자신의 나이만큼 양분을 먹을 수 없는 나무는 양분을 먹지 못하고 즉시 죽는다

여름에는 봄에 죽은 나무가 양분으로 변하게 된다
각각의 죽은 나무마다 나이를 2로 나눈 값이 나무가 있던 칸에 양분으로 추가

가을에는 나무가 번식
번식하는 나무는 나이가 5의 배수이어야 함
인접한 8개의 칸에 나이가 1인 나무가 생긴다

겨울에는 S2D2가 땅을 돌아다니면서 땅에 양분을 추가
각 칸에 추가되는 양분의 양은 A[r][c]

K년이 지난 후 상도의 땅에 살아있는 나무의 개수

"""

# 봄
# tree[i][j] 에서 값이 작은 순서로 food[i][j] 에서 1씩 뺌 -> tree[i][j].sort() 로 작은 순서로 정렬 후 수행
# food[i][j] = 0 이 되면, 남은 나무들은 없앰 -> 따로 저장을 해둬야겠다
# 해당 칸의 위치, 나무의 나이 를 저장해둠

# 여름
# tree[i][j] 에서 없앨 값들의 2로 나눈 값을 food[i][j] 에 더해줌

# 가을
# 나이가 5의 배수인 나무들에 대해, 주변 칸들에 나이 1인 나무를 추가

# 겨울
# food[i][j] += A[i][j]

N = 0 # 땅의 크기

# 1년에 대한 수행
def one_year_cycle(tree, food, A):
        died_tree = spring(tree, food)
        summer(died_tree, food)
        fall(tree)
        winter(food, A)
    
# 봄
# tree[i][j] 에서 값이 작은 순서로 food[i][j] 에서 1씩 뺌 -> tree[i][j].sort() 로 작은 순서로 정렬 후 수행
# food[i][j] = 0 이 되면, 남은 나무들은 없앰 -> 따로 저장을 해둬야겠다
# 해당 칸의 위치, 나무의 나이 를 저장해둠
def spring(tree, food):
    died_tree = [ [ [] for _ in range(N) ] for _ in  range(N) ] # 3차원 배열 -> 각 칸의 죽은 나무들의 나이
    
    for i in range(N):
        for j in range(N):
            tree[i][j].sort() # 작은 값 순서로 정렬

            for m in range(len(tree[i][j])):
                if food[i][j] < tree[i][j][m]: # 양분을 멋지 못하는 경우
                    for _ in range(len(tree[i][j]) - m):
                        died_tree[i][j].append(tree[i][j].pop(m))
                    break

                food[i][j] -= tree[i][j][m]
                tree[i][j][m] += 1

    return died_tree

# 여름
# tree[i][j] 에서 없앨 값들의 2로 나눈 값을 food[i][j] 에 더해줌
def summer(died_tree, food):
    for i in range(N):
        for j in range(N):
            for m in range(len(died_tree[i][j])):
                food[i][j] += died_tree[i][j][m] // 2


# 가을
# 나이가 5의 배수인 나무들에 대해, 주변 칸들에 나이 1인 나무를 추가
def fall(tree):
    for i in range(N):
        for j in range(N):
            for m in range(len(tree[i][j])):
                if tree[i][j][m] % 5 == 0:
                    breed(tree, i, j)


# (i, j) 의 주변 칸들에 나이 1인 나무를 추가
def breed(tree, i, j):
    if i - 1 >= 0:
        tree[i - 1][j].append(1)
        if j - 1 >= 0:
            tree[i - 1][j - 1].append(1)

        if j + 1 <= N - 1:
            tree[i - 1][j + 1].append(1)
            
    if i + 1 <= N - 1:
        tree[i + 1][j].append(1)
        if j - 1 >= 0:
            tree[i + 1][j - 1].append(1)

        if j + 1 <= N - 1:
            tree[i + 1][j + 1].append(1)
            
    if j - 1 >= 0:
        tree[i][j - 1].append(1)

    if j + 1 <= N - 1:
        tree[i][j + 1].append(1)


# 겨울
# food[i][j] += A[i][j]            
def winter(food, A):
    for i in range(N):
        for j in range(N):
            food[i][j] += A[i][j]
    


# 현재 전체 땅에 살아있는 나무의 개수를 구하는 함수
def count_trees(tree):
    count = 0
    
    for i in range(N):
        for j in range(N):
            count += len(tree[i][j])

    return count

# r, c -> 0부터 시작하도록 설정 -> (x, y) = (x - 1, y - 1)



# 나무들을 어떻게 저장하고 확인할 수 있을까
# 2차원 배열? -> 한 칸에 여러 개의 나무가 있는 경우 표현하기 어려운 문제점
# 3차원 배열로 해당 칸에 있는 나무를 다시 배열로 저장할 수 있을까? -> N<=10이면 괜찮을듯
# Tree[i][j] : (i, j)에 있는 나무들의 나이를 배열로 담아 저장



import sys
input = sys.stdin.readline

if __name__ == "__main__":
    N, M, K = map(int, input().split())

    A = [ [] for _ in range(N) ]
    
    for i in range(N):
        A[i] = list(map(int, input().split()))

    tree = [ [ [] for _ in range(N) ] for _ in  range(N) ] # 3차원 배열 -> 각 칸의 나무들의 나이
    food = [ [5 for _ in range(N)] for _ in range(N) ] # 2차원 배열 -> 각 칸의 총 양분
    
    for i in range(M):
        x, y, z = map(int, input().split()) # 나무의 위치 (x, y), 나무의 나이 z
        tree[x - 1][y - 1].append(z) # 해당 칸에 나이 z인 나무를 추가

    for _ in range(K):
        one_year_cycle(tree, food, A)
        
    print(count_trees(tree))
