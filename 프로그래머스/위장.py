def solution(clothes):
    answer = 1

    dic = {}

    for cloth in clothes:
        # name = cloth[0]
        kind = cloth[1]

        if kind in list(dic.keys()):
            dic[kind] += 1
        else:
            dic[kind] = 1

    for value in list(dic.values()):
        answer *= (value + 1)

    answer -= 1

    return answer