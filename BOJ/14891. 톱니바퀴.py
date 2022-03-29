# 14891. 톱니바퀴

"""
8개 톱니 -> 톱니바퀴 4개

톱니 -> N, S극 둘중 하나

톱니바퀴 총 K번 회전 - 시계, 반시계

회전할떄, 맞닿은 부분이 서로 다른 극이면 같이 회전 O (방향은 반대)
같은 극이면 회전 X

입력:
톱니바퀴의 초기상태
회전시킨 방법 

출력:
최종 톱니바퀴의 상태

첫 네줄동안 각 번호의 톱니바퀴의 상태 입력
12시 방향부터 시계방향 순서대로, N극 : 0, S극 : 1

다섯번째줄 : 회전횟수 k
k줄동안 회전시킨 방법 -> 톱니바퀴 번호, 방향(1 : 시계, -1 : 반시계)

회전 후, 점수의 합 출력
각 톱니바퀴의 12시 방향이 S극인 경우 점수 부여
1번 -> 1점
2번 -> 2점
3번 -> 4점
4번 -> 8점

"""

# 전체 톱니바퀴에서 target번째를 시계/반시계 방향으로 회전 -> 결과 gear를 반환
def rotation(target, clockwise, gear):
    # 양쪽이 존재하는지 확인 후, 존재하면, 회전하게 되는 경우 회전
    left = target - 1
    right = target + 1

    if left >= 1: # 왼쪽 톱니바퀴가 존재
        if gear[target][6] != gear[left][2]: # left의 오른쪽과 target의 왼쪽이 같은 극 -> 회전
            rotation_by(target, left, clockwise * (-1), gear)
        
    if right <= 4: # 오른쪽 톱니바퀴가 존재
        if gear[target][2] != gear[right][6]: # target의 오른쪽과 right의 왼쪽이 같은 극 -> 회전
            rotation_by(target, right, clockwise * (-1), gear)

    if clockwise == 1: # 시계방향 회전
        gear[target].appendleft(gear[target].pop())
    else: # 반시계방향 회전
        gear[target].append(gear[target].popleft())
        

# cause번째 톱니바퀴로 인해 effect번째 톱니바퀴가 시계/반시계 방향으로 회전
# cause번째 톱니바퀴 쪽으로는 영향을 주지 않음
def rotation_by(cause, effect, clockwise, gear):
    # 오른쪽에서 왼쪽으로 가는 방향 -> 왼쪽만 확인
    if effect < cause:
        left = effect - 1
        if left >= 1:
            if gear[effect][6] != gear[left][2]: # left의 오른쪽과 target의 왼쪽이 같은 극 -> 회전
                rotation_by(effect, left, clockwise * (-1), gear)    
            
    # 왼쪽에서 오른쪽으로 가는 방향 -> 오른쪽만 확인
    else:
        right = effect + 1
        if right <= 4:
            if gear[effect][2] != gear[right][6]: # target의 오른쪽과 right의 왼쪽이 같은 극 -> 회전
                rotation_by(effect, right, clockwise * (-1), gear)            

    if clockwise == 1: # 시계방향 회전
        gear[effect].appendleft(gear[effect].pop())
    else: # 반시계방향 회전
        gear[effect].append(gear[effect].popleft())




def calc_score(gear):
    score = 0
    for i in range(1, 5):
        score += gear[i][0] * (2 ** (i - 1))

    print(score)


from collections import deque    
import sys
input = sys.stdin.readline

if __name__ == "__main__":
    gear = [None for _ in range(5)]
    
    for i in range(1, 5): # 각 톱니에 대한 상태 입력
        line = input()
        
        q = deque()
        
        for j in range(8): # 8칸에 대한 입력
            q.append(int(line[j]))
        
        gear[i] = q # i번째 톱니바퀴 -> gear[i]

    k = int(input()) # 회전 횟수 : 1 ~ 100

    for _ in range(k): # k번의 회전 방법 입력
        target, clockwise = map(int, input().split())
        rotation(target, clockwise, gear)

    calc_score(gear)

        
























