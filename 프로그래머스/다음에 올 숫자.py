def solution(common):
    answer = 0

    first, second, third = common[:3]

    if second - first == third - second:
        answer = common[-1] + (second - first)
    else:
        answer = common[-1] * (second / first)

    return answer