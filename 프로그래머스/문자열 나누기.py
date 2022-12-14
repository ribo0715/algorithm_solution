
def solution(s):
    answer = 0

    n = len(s)
    last = 0
    for i in range(n):
        temp_count = s[last:i + 1].count(s[last])

        if temp_count == (i + 1 - last) / 2:
            answer += 1
            last = i + 1

    if last != n:
        answer += 1

    return answer