# [1차] 뉴스 클러스터링
"""
자카드 유사도
-> 두 집합의 교집합 크기 / 합집합 크기

둘 다 공집합이면 1로 정의

문자열 사이의 유사도 -> 두 글자씩 끊어서 집합을 만듦

같은 문자열이 나오면 뒤에 숫자를 붙여서 카운트를 해줄까?
"""


def get_set(temp_str):
    result = []

    for i in range(len(temp_str) - 1):
        if temp_str[i].isalpha() and temp_str[i + 1].isalpha():
            temp_piece = temp_str[i].lower() + temp_str[i + 1].lower()

            while temp_piece in result:
                temp_piece += "_"
            result.append(temp_piece)

    return result


# def get_set(temp_str):
#     result = []

#     i = 0
#     temp_piece = ""
#     while i < len(temp_str):
#         if temp_str[i].isalpha():
#             temp_piece = temp_str[i].lower()
#             i += 1
#             break
#         else:
#             i += 1

#     while i < len((temp_str)):
#         if temp_str[i].isalpha():
#             cur_piece = temp_str[i].lower()
#             cur_str = temp_piece + cur_piece

#             while cur_str in result:
#                 cur_str += "_"
#             result.append(cur_str)
#             temp_piece = cur_piece
#         i += 1
#     return result


def solution(str1, str2):
    answer = 0

    list_1 = get_set(str1)
    list_2 = get_set(str2)
    # print(list_1)
    # print(list_2)

    union_count = len(set(list_1 + list_2))
    intersection_count = len(list_1 + list_2) - union_count

    if union_count == 0:
        answer = 1
    else:
        answer = intersection_count / union_count

    return int(answer * 65536)