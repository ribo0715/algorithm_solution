# 가사 검색(기본)

from collections import deque

def solution(words, queries):
    answer = []

    # 길이에 따라 딕셔너리에 분류
    word_dict = {}
    query_dict = {}

    for word in words:
        length = len(word)

        if length in word_dict:
            word_dict[length].append(word)
        else:
            word_dict[length] = deque()
            word_dict[length].append(word)

    # 길이 확인
    # 접두사인지 접미사인지
    for query in queries:
        length = len(query)
        start_index = query.index("?")  # 값이 0이면 접두사, 아니면 접미사
        end_index = length - 1 - query[::-1].index("?")

        count = 0
        if start_index == 0 and end_index == length - 1:  # "????" 인 경우
            if length in word_dict:
                count = len(word_dict[length])
                answer.append(count)
            continue

        if length in word_dict:
            for _ in range(len(word_dict[length])):
                # for word in word_dict[length]:
                word = word_dict[length].popleft()
                if start_index == 0:  # "?" 로 시작
                    if query[end_index + 1:] == word[end_index + 1:]:
                        count += 1
                else:  # "?" 로 끝
                    if query[:start_index] == word[:start_index]:
                        count += 1
                word_dict[length].append(word)
        answer.append(count)

    return answer