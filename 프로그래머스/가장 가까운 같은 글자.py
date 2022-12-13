"""
딕셔너리에 저장해가면서 해당 글자의 가장 최근 위치를 기억하도록 함
"""


def solution(s):
    answer = []
    loc_dict = {}

    for index, c in enumerate(s):
        if c in loc_dict:
            answer.append(index - loc_dict[c])
        else:
            answer.append(-1)

        loc_dict[c] = index

    return answer