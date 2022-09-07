# 최댓값과 최솟값
"""
문자열s -> 공백으로 구분, 숫자들
최소값, 최대값 찾아 문자열 형태로 반환

split을 한 뒤, max?
"""


def solution(s):
    answer = ''

    num_list = list(map(int, s.split()))  # int형으로 list를 만들어줌
    # str형식으로 바로 list를 만들면 "-1", "-4"에서 "-1"이 min으로 선정됨 -> 왜 그런거지?

    # print(num_list)

    minumum = min(num_list)
    maximum = max(num_list)

    answer = str(minumum) + " " + str(maximum)

    return answer