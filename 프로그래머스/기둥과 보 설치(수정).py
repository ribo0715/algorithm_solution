# 기둥과 보 설치 -> 현재 설치된 기둥과 보 에 대해서만 생각을 함

"""
구조물을 추가하는 경우
구조물을 추가한 후 모든 구조물에 대하여 문제에서의 조건을 만족하는지 확인
만족하지 않는다면 추가한 구조물을 다시 제거

구조물을 제거하는 경우
구조물을 제거한 후 모든 구조물에 대하여 문제에서의 조건을 만족하는지 확인
만족하지 않는다면 제거한 구조물을 다시 추가

list가 아닌 set을 사용함으로서 원소의 탐색 및 삭제 속도를 높임
"""

def is_valid(answer):
    for x, y, a in answer:
        if a == 0: # 기둥
            if (x, y - 1, 0) in answer: # 아래 기둥
                continue
            elif (x - 1, y, 1) in answer: # 왼쪽 아래 보
                continue
            elif (x, y, 1) in answer: # 오른쪽 아래 보
                continue
            elif y == 0: # 바닥
                continue
            else:
                return False

        if a == 1: # 보
            if (x, y - 1, 0) in answer: # 왼쪽 아래 기둥
                continue
            elif (x + 1, y - 1, 0) in answer: # 오른쪽 아래 기둥
                continue
            elif (x - 1, y, 1) in answer and (x + 1, y, 1) in answer: # 양옆에 보
                continue
            else:
                return False
    return True


def solution(n, build_frame):
    answer = set() # list로 하는 것보다 더 빠르게 처리할 수 있음

    for cur_build_frame in build_frame:
        x, y, a, b = cur_build_frame

        if b == 0: # 제거
            answer.remove((x, y, a)) # 일단 제거해보고
            if not is_valid(answer): # 제거하고도 가능한 상태인지 확인
                answer.add((x, y, a))

        else: # 설치
            answer.add((x, y, a)) # 일단 설치해보고
            if not is_valid(answer): # 설치할 수 없는 상태
                answer.remove((x, y, a))

    answer = [list(x) for x in answer]
    answer.sort(key=lambda x:[x[0], x[1], x[2]])
    return answer