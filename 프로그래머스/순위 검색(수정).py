# 순위 검색 - 수정
"""
info를 읽으며 해당 info를 나타낼 수 있는 query들을 미리 생각해두어 정리

query를 읽으며 가능한 info를 생각하는 것이 아니라,
먼저 info를 보고 가능한 query들을 미리 생각해둔 뒤 검사를 시작함

갯수를 확인할 때는 binary search를 이용
"""
import copy
from itertools import combinations
from collections import defaultdict

def solution(info, query):
    answer = []
    dic = defaultdict(list)

    for i in info:
        temp = i.split()
        condition = temp[:-1] # 조건
        score = int(temp[-1]) # 점수

        for n in range(5):
            cases = list(combinations([0, 1, 2, 3], n)) # 4개의 조건 중 -로 표현할 경우들

            for case in cases:
                temp_condition = copy.deepcopy(condition)

                for index in case:
                    temp_condition[index] = "-"

                key = " ".join(temp_condition)
                dic[key].append(score)

    for condition in dic:
        dic[condition].sort()
        # print(dic[condition])

    # for value in dic.values():
    #     value.sort()

    for q in query:
        q = q.replace("and", "") # and 를 없앰
        q = q.split()

        target_key = " ".join(q[:-1])
        target_score = int(q[-1])
        # print(target_key)

        count = 0

        if target_key in dic:
            target_list = dic[target_key]

            if target_list:
                start, end = 0, len(target_list)

                while start < end:
                    mid = (start + end) // 2
                    if target_list[mid] >= target_score: # 왼쪽에 target_score보다 높은 점수가 존재할 수 있음
                        end = mid
                    else:
                        start = mid + 1

                count = len(target_list) - start # target_score 이상인 점수 갯수
        answer.append(count)

    return answer
