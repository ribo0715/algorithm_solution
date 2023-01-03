# 최빈값 구하기
"""
딕셔너리로 각 값을 key로 갖고, 나온 횟수를 value로 갖도록함
이후 value를 기준으로 정렬하여 가장 작은 값을 반환
"""

import operator
from collections import defaultdict


def solution(array):
    answer = 0

    temp_dict = defaultdict(int)

    for num in array:
        temp_dict[num] += 1

    sorted_list = sorted(temp_dict.items(), key=operator.itemgetter(1), reverse=True)

    if len(sorted_list) >= 2:
        if sorted_list[0][1] == sorted_list[1][1]:
            answer = -1
        else:
            answer = sorted_list[0][0]
    else:
        answer = sorted_list[0][0]

    return answer
