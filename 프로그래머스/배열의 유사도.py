def solution(s1, s2):
    answer = 0

    for x in s1:
        for y in s2:
            if x == y:
                answer += 1

    return answer