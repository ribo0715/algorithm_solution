# 순위 검색 - dict 활용

"""
info -> 개발언어 직군 경력 소울푸드 점수
최대한 빠르게 하려면 0번째 index만 체크해도 될듯?
4가지 값에 대해 각각 나눌까? -> 3 * 2 * 2 * 2 = 24 가지 경우
8a + 4b + 2c + d 로 index를 구분하면 어떨까?

점수에 대해 반대로 정렬을 수행 -> 이후 조건 점수보다 낮아지는 순간까지 카운트해주면?

query의 조건에 따라 가능한 a,b,c,d의 조합들을 생성
"""

from collections import defaultdict
from collections import deque


def make_info_dic(info):
    info_dic = defaultdict(list)

    for x in info:
        a, b, c, d, e = x.split()

        if a[0] == "c":
            a = 0
        elif a[0] == "j":
            a = 1
        elif a[0] == "p":
            a = 2

        if b[0] == "b":
            b = 0
        elif b[0] == "f":
            b = 1

        if c[0] == "j":
            c = 0
        elif c[0] == "s":
            c = 1

        if d[0] == "c":
            d = 0
        elif d[0] == "p":
            d = 1

        index = 8 * a + 4 * b + 2 * c + d
        info_dic[index].append(int(e))

    return info_dic


def count_num(q, info_dic):
    q_list = q.split()
    a = q_list[0]
    b = q_list[2]
    c = q_list[4]
    d = q_list[6]
    score = int(q_list[7])

    queue = deque()

    if a[0] == "c":
        queue.append([0])
    elif a[0] == "j":
        queue.append([1])
    elif a[0] == "p":
        queue.append([2])
    else:
        queue.append([0])
        queue.append([1])
        queue.append([2])

    for _ in range(len(queue)):
        temp = queue.popleft()

        if b[0] == "b":
            queue.append(temp + [0])
        elif b[0] == "f":
            queue.append(temp + [1])
        else:
            queue.append(temp + [0])
            queue.append(temp + [1])

    for _ in range(len(queue)):
        temp = queue.popleft()

        if c[0] == "j":
            queue.append(temp + [0])
        elif c[0] == "s":
            queue.append(temp + [1])
        else:
            queue.append(temp + [0])
            queue.append(temp + [1])

    for _ in range(len(queue)):
        temp = queue.popleft()
        if d[0] == "c":
            queue.append(temp + [0])
        elif d[0] == "p":
            queue.append(temp + [1])
        else:
            queue.append(temp + [0])
            queue.append(temp + [1])

    count = 0

    while queue:
        a, b, c, d = queue.popleft()
        index = 8 * a + 4 * b + 2 * c + d

        for x in info_dic[index]:
            if x >= score:
                count += 1

    return count


def solution(info, query):
    answer = []

    info_dic = make_info_dic(info)

    for q in query:
        count = count_num(q, info_dic)
        answer.append(count)

    return answer
