# 메뉴 리뉴얼
"""
최소 2명 이상의 손님으로부터 주문된 단품메뉴 조합
해당 개수짜리 세트메뉴 중 가장 많이 나온 것들을 찾음
"""

from itertools import combinations
from collections import Counter


def solution(orders, course):
    answer = []

    for num in course:  # 단품메뉴 num개짜리 세트메뉴
        temp = []  # 가능한 num개짜리 세트메뉴들을 담을 배열

        for order in orders:
            order = sorted(order)  # 정렬
            temp.extend(list(combinations(order, num)))  # num개짜리 세트 조합을 추가

        counter = Counter(temp)  # 각 세트 조합이 몇번 중복되는지를 나타냄
        # print(counter)

        if counter:  # num개짜리 세트의 조합이 있는 경우
            max_val = max(counter.values())
            if max_val >= 2:  # 2번 이상 주문한게 있는 경우
                for key in counter:
                    if counter[key] == max_val:
                        cur_answer = "".join(key)
                        answer.append(cur_answer)

    answer.sort()  # 정렬

    return answer