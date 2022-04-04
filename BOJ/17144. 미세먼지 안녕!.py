# 17144. 미세먼지 안녕!

"""
집을 크기가 R×C인 격자판

공기청정기는 항상 1번 열에 설치되어 있고, 크기는 두 행을 차지

공기청정기가 설치되어 있지 않은 칸에는 미세먼지가 있고, (r, c)에 있는 미세먼지의 양은 Ar,c

미세먼지가 확산된다.
확산은 미세먼지가 있는 모든 칸에서 동시에 일어난다
(r, c)에 있는 미세먼지는 인접한 네 방향으로 확산
인접한 방향에 공기청정기가 있거나, 칸이 없으면 그 방향으로는 확산이 일어나지 않는다.
확산되는 양은 Ar,c/5
(r, c)에 남은 미세먼지의 양은 Ar,c - (Ar,c/5)×(확산된 방향의 개수)

위쪽 공기청정기의 바람은 반시계방향으로 순환
아래쪽 공기청정기의 바람은 시계방향으로 순환
바람이 불면 미세먼지가 바람의 방향대로 모두 한 칸씩 이동

공기청정기가 설치된 곳은 Ar,c가 -1

 T초가 지난 후 구사과 방에 남아있는 미세먼지의 양을 출력



"""



# 방에 있는 모든 미세먼지 확산
def diffusion(A):
    B = [ [0 for _ in range(C)] for _ in range(R) ] # 확산되는 미세먼지들을 담을 배열
##    print("Before diffusion")
##    for i in range(R):
##        print(A[i])
        
    for i in range(R):
        for j in range(C):
            if A[i][j] >= 5: # 확산될 수 있는 칸
                temp = A[i][j] // 5
                if i - 1 >= 0 and A[i - 1][j] != -1: # 상
                    B[i - 1][j] += temp
                    A[i][j] -= temp

                if i + 1 < R and A[i + 1][j] != -1: # 하
                    B[i + 1][j] += temp
                    A[i][j] -= temp

                if j - 1 >= 0 and A[i][j - 1] != -1: # 좌
                    B[i][j - 1] += temp
                    A[i][j] -= temp

                if j + 1 < C: # 우
                    B[i][j + 1] += temp
                    A[i][j] -= temp

    for i in range(R):
        for j in range(C):
            A[i][j] += B[i][j] # 확산된 미세먼지의 양을 더해줌
            
##    print("After diffusion")
##    for i in range(R):
##        print(A[i])
        
# 공기청정기로 인한 순환
def circulation(A):
##    print("Before circulation")
##    for i in range(R):
##        print(A[i])
        
    air_cleaner_up = 0
    air_cleaner_down = 0
    
    for i in range(R):
        if A[i][0] == -1: # 공기청정기의 위치
            air_cleaner_up = i
            air_cleaner_down = i + 1
            break

    # 위쪽 공기청정기 -> 반시계방향 순환
    for i in range(air_cleaner_up - 1):
        A[air_cleaner_up - 1 - i][0] = A[air_cleaner_up - 2 - i][0]

    for j in range(C - 1):
        A[0][j] = A[0][j + 1]

    for i in range(air_cleaner_up):
        A[i][C - 1] = A[i + 1][C - 1]

    for j in range(C -2):
        A[air_cleaner_up][C - 1 - j] = A[air_cleaner_up][C - 2 - j]
    A[air_cleaner_up][1] = 0 # 공기청정기에서 나온 바람
        
    # 아래쪽 공기청정기 -> 시계방향 순환
    for i in range(air_cleaner_down + 1, R - 1):
        A[i][0] = A[i + 1][0]
        
    for j in range(C - 1):
        A[R - 1][j] = A[R - 1][j + 1]

    for i in range(R - air_cleaner_down - 1):
        A[R - 1 - i][C - 1] = A[R - 2 - i][C - 1]        

    for j in range(C - 2):
        A[air_cleaner_down][C - 1 - j] = A[air_cleaner_down][C - 2 - j]
    A[air_cleaner_down][1] = 0 # 공기청정기에서 나온 바람

##    print("After circulation")
##    for i in range(R):
##        print(A[i])



# 남아있는 미세먼지의 양 구하는 함수
def get_dust_sum(A):
    sum = 0

    for i in range(R):
        for j in range(C):
            if A[i][j] > 0:
                sum += A[i][j]

    return sum
            

    

import sys
input = sys.stdin.readline

if __name__ == "__main__":
    R, C, T = map(int, input().split())

    A = [ [] for _ in range(R) ]
    for i in range(R):
        A[i] = list(map(int, input().split()))

    for _ in range(T):
        diffusion(A)
        circulation(A)

    print(get_dust_sum(A))








    

