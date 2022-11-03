import operator

def solution(strings, n):
    answer = []
    strings.sort()
    answer = sorted(strings, key=operator.itemgetter(n))

    return answer
