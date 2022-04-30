# 14890. 경사로

"""
한쪽 끝에서 다른쪽 끝까지 지나갈 수 있는 길이 몇 개 있는지
모든 칸의 높이가 모두 같아야 한다

경사로를 놓아서 지나갈 수 있는 길
경사로는 높이가 항상 1이며, 길이는 L

지나갈 수 있는 길의 개수를 구하는 프로그램
"""

# 한칸씩 옆으로 가면서 높이 확인
# 높이가 1이 낮거나 높아지는 경우, 연속된 길이 확인
#   높아진 경우, 이전까지의 길이를
#   낮아진 경우, 앞으로의 길이를 확인
#   -> L 길이 이상 연속되면 ok

from collections import deque
import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n, L = map(int, input().split())
    board = [[] for _ in range(n)] # 지도
    
    for i in range(n):
        board[i] = list(map(int, input().split()))

    q_lines = deque()

    for j in range(n): 
        q_lines.append(board[j]) # 가로줄
            
        temp_line = []
        
        for i in range(n):
            temp_line.append(board[i][j])

        q_lines.append(temp_line) # 세로줄

    count_total = 0
    
    while q_lines:
        line = q_lines.pop() # 가능한 line 하나씩 꺼내서 확인
        
        # 연속된 같은 높이의 길 수
        prev_h, curr_h = line[0], line[0]
        same_h_count = 1

        flag = 0 # 동일한 높이인 경우 0, 높이가 1만큼 낮아진 경우 -1, 높이가 1만큼 높아진 경우 1

        can_road = True # 해당 line이 지나갈 수 있는 길인지
        
        for i in range(1, n):
            curr_h = line[i]

            ###################
            if flag == 0: # 동일한 높이가 연속되는 경우
                if prev_h == curr_h: # 이전과 동일한 높이인 경우
                    same_h_count += 1

                elif prev_h - 1 == curr_h: # 한칸 내려가는 경우
                    # 앞으로 연속된 높이의 수를 확인해야함
                    flag = - 1
                    same_h_count = 1

                    if L == 1: # 경사로 길이가 1인경우는 바로 가능
                        can_road = True
                    else:
                        can_road = False # 이후에 경사로가 놓이기 전까지는 불가능

                elif prev_h + 1 == curr_h: # 한칸 올라가는 경우
                    # 지금까지 연속된 높이의 수를 확인
                    if same_h_count >= L: # 경사로를 놓을 수 있는 경우, 가능
                        flag = 0
                        same_h_count = 1
                    else:
                        can_road = False
                        break

                else: # 두칸 이상 차이나는 경우, 끝
                    can_road = False
                    break
                
            ###################
            elif flag == -1: # 이전에 한칸 아래로 내려온 상태인 경우                
                # 앞으로 같은 높이가 L 이상 연속되어야 함
                if prev_h == curr_h: # 다음칸과 동일한 높이인 경우
                    same_h_count += 1

                    if same_h_count >= L:
                        can_road = True

                elif prev_h - 1 == curr_h: # 한칸 내려가는 경우
                    # 이전까지 같은 높이로 L 이상 연속되었는지 확인
                    if same_h_count >= L: # 경사로를 놓을 수 있는 경우, 가능
                        flag = - 1
                        same_h_count = 1

                        if L == 1: # 경사로 길이가 1인경우는 바로 가능
                            can_road = True
                        else:
                            can_road = False # 이후에 경사로가 놓이기 전까지는 불가능
                            
                    else:
                        can_road = False
                        break

                elif prev_h + 1 == curr_h: # 한칸 올라가는 경우
                    # 지금까지 연속된 높이의 수를 확인
                    # 내려왔다 올라가므로 경사로가 두개 필요
                    if same_h_count >= 2 * L: # 경사로를 놓을 수 있는 경우, 가능
                        flag = 0
                        same_h_count = 1
                    else: # 
                        can_road = False
                        break

                else: # 두칸 이상 차이나는 경우, 끝
                    can_road = False
                    break
                
            ###################
##            elif flag == 1: # 한칸 위로 올라온 경우
##                # flag를 업데이트할 때에 이전까지 같은 높이가 L 이상 연속되었는지 확인
##                if prev_h == curr_h: # 다음칸과 동일한 높이인 경우
##                    flag = 0
##                    same_h_count += 1
##
##                elif prev_h - 1 == curr_h: # 한칸 내려가는 경우
##                    # 앞으로 연속된 높이의 수를 확인
##                    flag = - 1
##
##                elif prev_h + 1 == curr_h: # 한칸 올라가는 경우
##                    # 지금까지 연속된 높이의 수를 확인
##
##                    flag = 1
##
##                else: # 두칸 이상 차이나는 경우, 끝
##                    can_road = False
##                    break                

                
            prev_h = curr_h # prev_h 업데이트한 뒤, 다음 칸으로 넘어감

##        print(line)
        if can_road:
##            print("can :", line)
            count_total += 1

    print(count_total)











        
