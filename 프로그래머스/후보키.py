# 후보키
"""
유일성 -> 기존의 갯수와 set으로 했을때의 갯수가 같으면 만족

최소성 -> 유일성을 만족하지 않는 것들로 조합

유일성, 최소성을 만족하지 않는것들을 list로 관리
둘을 조합했을때, 유일성을 만족하는지 확인
-> 만족하면 count + / 만족하지 않으면 list에 추가

그냥 combination으로 가능한 경우들을 확인해볼까?
"""

from itertools import combinations


def is_unique(relation, key_list):  # 유일성 판단
    tuple_set = set()
    for cur_tuple in relation:
        cur = ""
        for key in key_list:
            cur += cur_tuple[key]
        tuple_set.add(cur)

    if len(tuple_set) == len(relation):  # 유일성을 만족하지 않으면, False
        return True
    else:
        return False


def solution(relation):
    answer_list = []
    tuple_num = len(relation)  # tuple 수
    attribute_num = len(relation[0])  # attribute 수

    total_list = []
    for i in range(1, attribute_num + 1):
        total_list += list(combinations(range(attribute_num), i))

    for key_list in total_list:
        key_list = list(key_list)
        if is_unique(relation, key_list):
            is_minimal = True  # 최소성 판단
            for target in answer_list:
                if set(target).issubset(set(key_list)):
                    is_minimal = False  # subset이 answer_list에 있으면, 최소성 탈락
                    break

            if is_minimal:
                answer_list.append(key_list)

    answer = len(answer_list)
    return answer