# 15683. 감시

"""
N×M 크기의 직사각형 사무실

총 K개의 CCTV , CCTV는 5가지 종

1번 CCTV는 한 쪽 방향만

2번과 3번은 두 방향을 감시
2번은 감시하는 방향이 서로 반대방향
3번은 직각 방향

4번은 세 방향

5번은 네 방향

CCTV는 감시할 수 있는 방향에 있는 칸 전체를 감시할 수 있다
CCTV는 벽을 통과할 수 없다

CCTV는 회전시킬 수 있는데, 회전은 항상 90도 방향

지도에서 0은 빈 칸, 6은 벽, 1~5는 CCTV의 번호

사무실의 크기와 상태, 그리고 CCTV의 정보가 주어졌을 때, 사각 지대의 최소 크기 구하기
-> CCTV가 가장 많은 칸들을 확인할 수 있도록

"""



import copy

# arr[i][j]에 cctv가 있을때, 가능한 경우들의 이후 arr를 q에 넣음
# 1번 -> 4가지 경우
def cctv1(q, arr, i, j): # arr[i][j] 에 1번 cctv
    temp = copy.deepcopy(arr)
    look_up(temp, i, j)
    q.append(temp) # 현재 상태에서 arr[i][j] 1번 cctv가 위를 보는 경우에 대한 arr상태를 q에 넣어줌

    temp = copy.deepcopy(arr)
    look_right(temp, i, j)
    q.append(temp)

    temp = copy.deepcopy(arr)
    look_down(temp, i, j)
    q.append(temp)

    temp = copy.deepcopy(arr)
    look_left(temp, i, j)
    q.append(temp)

    
    
# 2번 -> 2가지 경우
def cctv2(q, arr, i, j): # arr[i][j] 에 2번 cctv
    temp = copy.deepcopy(arr)
    look_up(temp, i, j)
    look_down(temp, i, j)
    q.append(temp)

    temp = copy.deepcopy(arr)
    look_right(temp, i, j)
    look_left(temp, i, j)
    q.append(temp)
    
# 3번 -> 4가지 경우
def cctv3(q, arr, i, j): # arr[i][j] 에 3번 cctv
    temp = copy.deepcopy(arr)
    look_up(temp, i, j)
    look_right(temp, i, j)
    q.append(temp)

    temp = copy.deepcopy(arr)
    look_right(temp, i, j)
    look_down(temp, i, j)
    q.append(temp)

    temp = copy.deepcopy(arr)
    look_left(temp, i, j)
    look_down(temp, i, j)
    q.append(temp)

    temp = copy.deepcopy(arr)
    look_left(temp, i, j)
    look_up(temp, i, j)
    q.append(temp)
    
    
# 4번 -> 4가지 경우
def cctv4(q, arr, i, j): # arr[i][j] 에 4번 cctv
    temp = copy.deepcopy(arr)
    look_right(temp, i, j)
    look_down(temp, i, j)
    look_left(temp, i, j)
    q.append(temp)

    temp = copy.deepcopy(arr)
    look_up(temp, i, j)
    look_down(temp, i, j)
    look_left(temp, i, j)
    q.append(temp)

    temp = copy.deepcopy(arr)
    look_up(temp, i, j)
    look_right(temp, i, j)
    look_left(temp, i, j)
    q.append(temp)

    temp = copy.deepcopy(arr)
    look_up(temp, i, j)
    look_right(temp, i, j)
    look_down(temp, i, j)
    q.append(temp)
    
# 5번 -> 1가지 경우 -> 고정
def cctv5(q, arr, i, j): # arr[i][j] 에 5번 cctv
    temp = copy.deepcopy(arr)
    look_up(temp, i, j)
    look_right(temp, i, j)
    look_down(temp, i, j)
    look_left(temp, i, j)
    q.append(temp)




def look_up(arr, i, j): # arr[i][j] 에 있는 cctv가 위쪽을 확인
    while i >= 0:
        if arr[i][j] == 6: # 벽을 만나지 않으면 끝까지 확인
            break

        if arr[i][j] == 0: # 빈칸은 감시 -> #으로 변경
            arr[i][j] = "#"

        i -= 1 # 한칸 위로 올라가 확인
        
def look_down(arr, i, j): # arr[i][j] 에 있는 cctv가 아래쪽을 확인
    n = len(arr)
    
    while i <= n - 1:
        if arr[i][j] == 6: # 벽을 만나지 않으면 끝까지 확인
            break

        if arr[i][j] == 0: # 빈칸은 감시 -> #으로 변경
            arr[i][j] = "#"

        i += 1 # 한칸 위로 올라가 확인

def look_right(arr, i, j): # arr[i][j] 에 있는 cctv가 오른쪽을 확인
    m = len(arr[0])
    
    while j <= m - 1:
        if arr[i][j] == 6: # 벽을 만나지 않으면 끝까지 확인
            break

        if arr[i][j] == 0: # 빈칸은 감시 -> #으로 변경
            arr[i][j] = "#"

        j += 1 # 한칸 위로 올라가 확인

def look_left(arr, i, j): # arr[i][j] 에 있는 cctv가 왼쪽을 확인
    while j >= 0:
        if arr[i][j] == 6: # 벽을 만나지 않으면 끝까지 확인
            break

        if arr[i][j] == 0: # 빈칸은 감시 -> #으로 변경
            arr[i][j] = "#"

        j -= 1 # 한칸 위로 올라가 확인

# 각 경우들의 조합을 다 시도해보도록 하면 될듯


def check(arr): # arr에서의 사각지대 수 파악
    n = len(arr)
    m = len(arr[0])
    count = 0
    
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0:
                count += 1

    return count


import sys
input = sys.stdin.readline
from collections import deque

if __name__ == "__main__":
    n, m = map(int, input().split()) # 사무실의 세로 크기 N과 가로 크기 M

    arr = [[] for _ in range(n)]
    
    for i in range(n):
        arr[i] = list(map(int, input().split()))

    q = deque() # arr 의 상태를 저장해나감
    # cctv들에 대해서 각 종류에 따라 가능한 방법들을 모두 확인
    q.append(arr)

    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1: # cctv 인 경우
                for _ in range(len(q)):
                    arr = q.popleft()
                    cctv1(q, arr, i, j)

            if arr[i][j] == 2: # cctv 인 경우
                 for _ in range(len(q)):
                    arr = q.popleft()
                    cctv2(q, arr, i, j)
                    
            if arr[i][j] == 3: # cctv 인 경우
                for _ in range(len(q)):
                    arr = q.popleft()
                    cctv3(q, arr, i, j)
                    
            if arr[i][j] == 4: # cctv 인 경우
                for _ in range(len(q)):
                    arr = q.popleft()
                    cctv4(q, arr, i, j)
                    
            if arr[i][j] == 5: # cctv 인 경우
                for _ in range(len(q)):
                    arr = q.popleft()
                    cctv5(q, arr, i, j)

    count_min = 64
    while q:
        arr = q.popleft()
        count_temp = check(arr)
        
        if count_min > count_temp:
            count_min = count_temp

    print(count_min)





















    
