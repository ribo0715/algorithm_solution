def solution(s):
    answer = True

    if len(s) == 4 or len(s) == 6:
        for c in s:
            if not c.isdigit():
                return False
    else:
        return False

    return answer