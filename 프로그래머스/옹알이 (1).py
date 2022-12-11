"""
앞에서부터 4개중 하나로 시작하는지 확인해가면서 지워나감
-> 문자열이 없어질때까지
"""


def solution(babbling):
    answer = 0

    for s in babbling:
        while s:
            flag = False
            for can_speak in ["aya", "ye", "woo", "ma"]:
                if s.startswith(can_speak):
                    s = s[len(can_speak):]
                    flag = True
                    break
            if s and flag == False:
                break
        if not s:
            answer += 1

    return answer