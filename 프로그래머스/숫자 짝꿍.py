# 숫자 짝꿍
"""
임의의 자리에서 공통으로 나타나는 정수 k
짝꿍이 없으면 -1

자릿수를 늘려가면서 키우고 같은 값이 나오면 배열에 담아 저장해두고 정렬한 뒤 합침
-> 이게 아니라, 다른 자릿수에 있어도 가능한 것이므로 이 방법은 땡

자릿수마다 값을 확인해서 몇번째 자리에 같은게 있는지 확인할 필요가 없을 듯
-> n ^ 2 으로 복잡도도 너무 높음
-> 시간초과도 뜸

0~9 까지의 수를 카운트해서 이어붙이면 될 듯
-> 시간초과
"""


def solution(X, Y):
    answer = ''

    for i in reversed(range(10)):
        answer += (str(i) * min(X.count(str(i)), Y.count(str(i))))

    if answer == '':
        return '-1'
    elif len(answer) == answer.count('0'):  # elif int(answer) == 0: 으로 하는 경우 시간초과가 나옴
        return '0'
    else:
        return answer


"""
from collections import defaultdict

def solution(X, Y):
    answer = ''

    str_X, str_Y = str(X), str(Y)
    list_X, list_Y = list(str_X), list(str_Y)
    dict_X, dict_Y = defaultdict(int), defaultdict(int) # X, Y에 각 숫자가 몇개 담겨있는지 파악

    len_X, len_Y = len(str_X), len(str_Y)
    for _ in range(len_X):
        dict_X[list_X.pop(0)] += 1

    for _ in range(len_Y):
        dict_Y[list_Y.pop(0)] += 1

    for k in reversed(range(10)):
        answer += str(k) * min(dict_X[str(k)], dict_Y[str(k)])

    if answer == "":
        answer = "-1"
    elif int(answer) == 0:
        answer = "0"

    return answer    
"""

"""
def solution(X, Y):
    answer = ''

    str_X, str_Y = str(X), str(Y)

    for k in reversed(range(10)):
        count_k = min(str_X.count(str(k)), str_Y.count(str(k)))
        answer += str(k) * count_k

    if answer == "":
        answer = "-1"
    elif int(answer) == 0:
        answer = "0"

    return answer
"""

"""
def solution(X, Y):
    answer = ''

    list_X, list_Y = list(str(X)), list(str(Y))

    temp_list = []

    for i in range(len(list_X)):
        limit = len(list_Y)
        j = 0
        for _ in range(limit): # while 문 대체
            if j >= len(list_Y):
                break

            if list_X[i] == list_Y[j]:
                temp_list.append(list_Y.pop(j))
            else:
                j += 1

    if temp_list:
        temp_list.sort(reverse=True)
        answer = "".join(temp_list)
        if int(answer) == 0:
            answer = "0"
    else:
        answer = "-1"


    return answer
"""