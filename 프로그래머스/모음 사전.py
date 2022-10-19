# 모음 사전
"""
그냥 다 해봐도 될듯...? 어렵게 계산해서 딱 뽑기엔 너무 머리아프다...
"""

from itertools import product


def solution(word):
    words = []

    for i in range(1, 6):
        for c in product(['A', 'E', 'I', 'O', 'U'], repeat=i):
            temp_word = "".join(list(c))
            words.append(temp_word)

    words.sort()

    answer = words.index(word) + 1

    return answer
