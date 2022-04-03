# 17140. 이차원 배열과 연산

"""
크기가 3×3인 배열 A, 인덱스는 1부터 시작

R 연산: 배열 A의 모든 행에 대해서 정렬을 수행
-> 행의 개수 ≥ 열의 개수인 경우에 적용

C 연산: 배열 A의 모든 열에 대해서 정렬을 수행
-> 행의 개수 < 열의 개수인 경우에 적용

각각의 수가 몇 번 나왔는지
수의 등장 횟수가 커지는 순으로, 그러한 것이 여러가지면 수가 커지는 순으로 정렬

배열 A에 정렬된 결과를 다시 넣어야 한다
수와 등장 횟수를 모두 넣으며, 순서는 수가 먼저

가장 큰 곳을 기준으로 모든 곳의 크기가 변한다
행 또는 열의 크기가 커진 곳에는 0이 채워진다
수를 정렬할 때 0은 무시

행 또는 열의 크기가 100을 넘어가는 경우에는 처음 100개를 제외한 나머지는 버린다

배열 A에 들어있는 수와 r, c, k가 주어졌을 때, A[r][c]에 들어있는 값이 k가 되기 위한 최소 시간 구하기

"""

# 어떤 연산을 할지 파악 후, 연산 호출
def pick_op(A):
    if len(A) >= len(A[0]): # 행의 개수 ≥ 열의 개수
##        print("R 연산 수행")
        return op_B(A)
    else: # 행의 개수 < 열의 개수
##        print("C 연산 수행")
        return op_C(A)

# 

import operator

# B 연산
def op_B(A):
    result = [ [] for _ in range(len(A)) ]
    longest_len = 0
    
    # 모든 행에 대해 정렬
    for i in range(len(A)):
        temp_dict = {} # 각 행에 대한 딕셔너리
        for j in range(len(A[i])):
            if A[i][j] == 0: # 0은 무시
                continue
            if A[i][j] in temp_dict: # 딕셔너리에 존재하는지 확인
                temp_dict[A[i][j]] += 1
            else:
                temp_dict[A[i][j]] = 1 # 없으면 값 추가

        temp_arr = sorted(temp_dict.items()) # 수가 커지는 순서로 우선 정렬
        temp_arr = sorted(temp_arr, key = operator.itemgetter(1)) # 등장 횟수로 정렬

        for x in range(len(temp_arr)):
            # 100보다 긴 경우 버림
            if len(result[i]) >= 100:
##                print("100이 넘었어!!")
                break
            
            result[i].append(temp_arr[x][0]) # 수
            if len(result[i]) >= 100:
##                print("100이 넘었어!!")
                break
            result[i].append(temp_arr[x][1]) # 등장 횟수

        longest_len = max(longest_len, len(result[i]))
    
    # 가장 긴 행보다 모자른 부분 0으로 채움
    for i in range(len(A)):
        for j in range(longest_len - len(result[i])):
            result[i].append(0)
            
    return result

# 행/열을 바꿈
def transpose(A):
    r, c = len(A), len(A[0])

    result = [ [0 for _ in range(r)] for _ in range(c) ]
    
    for i in range(r):
        for j in range(c):
            result[j][i] = A[i][j]

    return result      

# C 연산
def op_C(A):
    result = [ [ ] for _ in range(len(A[0])) ]
    # 모든 열에 대해 정렬 -> 행, 열을 바꾼 후 B 연산 -> 다시 행, 열을 바꿈
    return transpose(op_B(transpose(A)))



import sys
input = sys.stdin.readline

if __name__ == "__main__":
    r, c, k = map(int, input().split())
    r, c = r - 1, c - 1 # 1씩 줄여 배열에 바로 접근할 수 있도록 함

    A = [ [] for _ in range(3) ]
    for i in range(3):
        A[i] = list(map(int, input().split()))

    t = 0
    while t <= 100: # 100초까지 확인
##        print("Before")
##        for i in range(3):
##            print(A[i])
            
        # A[r][c] == k 확인 -> 배열 크기 확인
        if len(A) > r and len(A[r]) > c:
            if A[r][c] == k:
                print(t)
                break
                
        # A에 대해 연산 수행
        A = pick_op(A)
        
##        print("After")
##        for i in range(3):
##            print(A[i])
##        print()
        
        # t 값 1 증가
        t += 1

    if t > 100:
        print("-1")




