# 5373. 큐빙

# 반시계 방향 -> 시계 방향 세번 반복 으로 하면 상당히 좋을듯?!!

"""
윗 면 흰색w, 아랫 면 노란색y, 앞 면 빨간색r, 뒷 면 오렌지색o, 왼쪽 면 초록색g, 오른쪽 면 파란색b

큐브의 상태를 어떻게 저장할 수 있을까...
배열? 
전개도?

상대적인 위치로 파악할 방법이 떠오르지 않음...
-> 전개도가 제일 가능해보임

U: 윗 면, D: 아랫 면, F: 앞 면, B: 뒷 면, L: 왼쪽 면, R: 오른쪽 면
+인 경우에는 시계 방향 (그 면을 바라봤을 때가 기준), -인 경우에는 반시계 방향
"""

# 각 큐브의 면을 나타낼 배열
U, D, F, B, L, R = [], [], [], [], [], []

def reset_cube():
    global U, D, F, B, L, R
    
    U = [['w' for _ in range(3)] for _ in range(3)] # 위U
    D = [['y' for _ in range(3)] for _ in range(3)] # 아래 D
    F = [['r' for _ in range(3)] for _ in range(3)] # 앞 F
    B = [['o' for _ in range(3)] for _ in range(3)] # 뒤 B
    L = [['g' for _ in range(3)] for _ in range(3)] # 왼 L
    R = [['b' for _ in range(3)] for _ in range(3)] # 오 R

# 각 면의 사이드 시계방향으로(상, 우, 하, 좌)
#o 위 -> 뒤[2][i], 오[0][2 - i], 앞[0, 2 - i], 왼[0][2 - i]
# 아래 -> 앞[2][i], 오[i][2], 뒤[0][2 - i], 왼[2][i] <- 여기에서 틀림
##o (수정) 아래 -> 앞[2][i], 오[2][i], 뒤[0][2 - i], 왼[2][i]
# 앞 -> 위[2][i], 오[i][0], 아래[0][2 - i], 왼[2 - i][2]
# 뒤 -> 아래[2][i], 오[2 - i][2], 위[0][2 - i], 왼[2 - i][0] <- 여기에서 틀림
##o (수정) 뒤 -> 아래[2][i], 오[2 - i][2], 위[0][2 - i], 왼[i][0] 
#o 왼 -> 위[i][0], 앞[i][0], 아래[i][0], 뒤[i][0]
#o 오른 -> 위[2 - i][2], 뒤[2 - i][2], 아래[2 - i][2], 앞[2 - i][2]


import copy

##어떤 면을 어떤 방향으로 돌릴때 -> 반대쪽 면 빼고 다 영향
def rotate(face_name, direction):
    global U, D, F, B, L, R

    face = None # 돌려지기 전 해당 면의 상태
    if face_name == "U":
        face = U
    elif face_name == "D":
        face = D
    elif face_name == "F":
        face = F
    elif face_name == "B":
        face = B
    elif face_name == "L":
        face = L
    elif face_name == "R":
        face = R

    temp = copy.deepcopy(face) # 돌려지기 전의 해당 면의 상태
    
    if direction == "+": # 시계방향            
        # 해당 면을 돌림
        for i in range(3):
            for j in range(3):
                face[j][2 - i] = temp[i][j]
        
        # 해당 면에 붙어있는 옆면들 12칸을 3칸씩 옮겨줌
        if face_name == "U":
            for i in range(3):
                temp = B[2][i]
                B[2][i] = L[0][2 - i]
                L[0][2 - i] = F[0][2 - i]
                F[0][2 - i] = R[0][2 - i]
                R[0][2 - i] = temp
                
        elif face_name == "D":
            for i in range(3):
                temp = F[2][i]
                F[2][i] = L[2][i]
                L[2][i] = B[0][2 - i]
                B[0][2 - i] = R[2][i]
                R[2][i] = temp
                
        elif face_name == "F":
            for i in range(3):
                temp = U[2][i]
                U[2][i] = L[2 - i][2]
                L[2 - i][2] = D[0][2 - i]
                D[0][2 - i] = R[i][0]
                R[i][0] = temp

        elif face_name == "B":
            for i in range(3):
                temp = D[2][i]
                D[2][i] = L[i][0]
                L[i][0] = U[0][2 - i]
                U[0][2 - i] = R[2 - i][2]
                R[2 - i][2] = temp

        elif face_name == "L":
            for i in range(3):
                temp = U[i][0]
                U[i][0] = B[i][0]
                B[i][0] = D[i][0]
                D[i][0] = F[i][0]
                F[i][0] = temp

        elif face_name == "R":
            for i in range(3):
                temp = U[2 - i][2]
                U[2 - i][2] = F[2 - i][2]
                F[2 - i][2] = D[2 - i][2]
                D[2 - i][2] = B[2 - i][2]
                B[2 - i][2] = temp

    ###########################################
    elif direction == "-": # 반시계방향
        # 해당 면을 돌림
        for i in range(3):
            for j in range(3):
                face[2 - j][i] = temp[i][j]
        
        # 해당 면에 붙어있는 옆면들 12칸을 3칸씩 옮겨줌
        if face_name == "U":
            for i in range(3):
                temp = B[2][i]
                B[2][i] = R[0][2 - i]
                R[0][2 - i] = F[0][2 - i]
                F[0][2 - i] = L[0][2 - i]
                L[0][2 - i] = temp
                
        elif face_name == "D":
            for i in range(3):
                temp = F[2][i]
                F[2][i] = R[2][i]
                R[2][i] = B[0][2 - i]
                B[0][2 - i] = L[2][i]
                L[2][i] = temp
                
        elif face_name == "F":
            for i in range(3):
                temp = U[2][i]
                U[2][i] = R[i][0]
                R[i][0] = D[0][2 - i]
                D[0][2 - i] = L[2 - i][2]
                L[2 - i][2] = temp
        
        elif face_name == "B":
            for i in range(3):
                temp = D[2][i]
                D[2][i] = R[2 - i][2]
                R[2 - i][2] = U[0][2 - i]
                U[0][2 - i] = L[i][0]
                L[i][0] = temp
                
        elif face_name == "L":
            for i in range(3):
                temp = U[i][0]
                U[i][0] = F[i][0]
                F[i][0] = D[i][0]
                D[i][0] = B[i][0]
                B[i][0] = temp
                
        elif face_name == "R":
            for i in range(3):
                temp = U[2 - i][2]
                U[2 - i][2] = B[2 - i][2]
                B[2 - i][2] = D[2 - i][2]
                D[2 - i][2] = F[2 - i][2]
                F[2 - i][2] = temp


def print_U():
    global U

    for i in range(3):
        print(("").join(U[i]))


    
import sys
input = sys.stdin.readline

if __name__ == "__main__":    
    T = int(input())

    for _ in range(T):
        reset_cube()
        n = int(input()) # 큐브를 돌릴 횟수 : 1 ~ 1000

        rotation_list = input().split()

        for rotation in rotation_list:
            face_name = rotation[0]
            direction = rotation[1]
            rotate(face_name, direction)
            
        # 윗면 출력
        print_U()
        
        







    
