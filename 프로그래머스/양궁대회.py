# 양궁대회
"""
어피치보다 점수가 높게
-> 어피치가 맞춘 갯수보다 많게 맞춤 or 어피치가 얻지 못한 점수에 한발을 맞춤
-> 다 하고나서 화살이 남으면, 0점짜리에 다 쏨

어피치가 점수를 낸 부분에 대해서 체크
-> 해당 부분보다 하나 더 많이 or 포기

최대 점수차를 낸 것들에 대해서는 가장 낮은 점수에 많이 맞춘 것을 반환

현재까지 가장 큰 점수 차이를 내는 방법
"""

from collections import deque
import copy

# 점수 차를 계산
def get_score_gap(apeach, lion):
    score_gap = 0

    for i in range(11):
        # 둘다 0점이면 넘어감
        if apeach[i] == lion[i] == 0:
            continue

        if apeach[i] >= lion[i]: # 어피치 점수
            score_gap -= 10 - i
        else:
            score_gap += 10 - i

    return score_gap


def solution(n, info):
    q = deque()
    q.append([0 for _ in range(11)])
    
    for i in range(11):
        for _ in range(len(q)):
            cur = q.popleft()

            next1 = copy.deepcopy(cur) # 해당 점수에 어피치보다 한발 더 쏨
            next1[i] = info[i] + 1
            if sum(next1) <= n: # 최대 쏠 수 있는 횟수를 넘어가면 제외
                q.append(next1)

            next2 = copy.deepcopy(cur) # 해당 점수에 쏘지 않음
            q.append(next2)

    for _ in range(len(q)):
        cur = q.popleft()
        next = copy.deepcopy(cur)
        next[10] = n - sum(next) # 마지막 0점에 남은 화살을 다 소모
        q.append(next)

    max_gap = 1
    max_lion_list = []
    # q에는 모든 조합이 존재 -> 가장 큰 점수차를 내는 경우를 선택해야함

    while q:
        temp_lion = q.pop()
        temp_gap = get_score_gap(info, temp_lion)

        if max_gap < temp_gap:
            max_gap = temp_gap
            max_lion_list = [temp_lion]
        elif max_gap == temp_gap:
            max_lion_list.append(temp_lion)

    # 가장 큰 점수 차를 내는 경우를 구함
    if max_lion_list:
        if len(max_lion_list) == 1: # 하나는 그냥 바로 출력
            answer = max_lion_list[0]
        else:
            for i in range(len(max_lion_list)):
                max_lion_list[i].reverse() # 거꾸로 뒤집어 확인

            max_lion_list.sort(reverse = True) # 가장 낮은 점수에 많이 쏜 순서대로 정렬

            answer = list(reversed(max_lion_list[0]))

    else:
        answer = [-1]
    return answer