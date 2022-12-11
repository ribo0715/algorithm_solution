"""
k개를 고름
귤 크기가 서로 다른게 가장 적도록

가장 많은 순서대로 차례대로 담으면 될듯?
"""

from collections import defaultdict
import operator


def solution(k, tangerine):
    answer = 0
    tangerine_dic = defaultdict(int)

    # 해당 귤 크기 갯수 +1 카운트해줌
    for x in tangerine:
        tangerine_dic[x] += 1

    # 각 귤 크기 갯수가 많은 순서대로 정렬
    sorted_dic = sorted(tangerine_dic.items(), key=operator.itemgetter(1), reverse=True)
    # print(sorted_dic)

    total_count = 0
    while total_count < k:
        cur_size, cur_count = sorted_dic.pop(0)
        total_count += cur_count
        answer += 1

    return answer