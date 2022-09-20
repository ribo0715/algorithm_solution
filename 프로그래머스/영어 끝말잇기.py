# 영어 끝말잇기
"""
가장 먼저 탈락하는 사람의 번호
그 사람이 자신의 몇 번째 차례에 탈락하는지

i번째의 마지막, i+1번째의 처음 비교
-> 다르면 탈락

현재까지 나온 단어들과 중복여부 판단
-> 중복이면 탈락
"""


def solution(n, words):
    answer = []
    idx = 1

    next_start = words[0][-1]
    visited = []  # 이미 사용된 단어
    visited.append(words[0])

    while idx < len(words):
        if next_start != words[idx][0]:  # idx번째에서 탈락
            num = idx % n + 1
            count = idx // n + 1
            return [num, count]

        if words[idx] in visited:
            num = idx % n + 1
            count = idx // n + 1
            return [num, count]

        visited.append(words[idx])
        next_start = words[idx][-1]
        idx += 1

    return [0, 0]