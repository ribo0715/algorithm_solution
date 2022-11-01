from itertools import combinations

def solution(number):
    answer = 0
    for group in list(combinations(number, 3)):
        if sum(group) == 0:
            answer += 1
    return answer
