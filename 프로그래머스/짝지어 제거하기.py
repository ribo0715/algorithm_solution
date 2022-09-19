# 짝지어 제거하기
"""
같은 알파벳이 2개 붙어있는 짝 -> 제거

문자열을 모두 제거할 수 있으면 1, 아니면 0

-> 스택에 넣는 방법이라고 생각하면 될 듯
"""


def solution(s):
    answer = -1

    stack = [s[0]]

    for i in range(1, len(s)):
        if stack:
            if stack[-1] == s[i]:
                stack.pop()
            else:
                stack.append(s[i])
        else:
            stack.append(s[i])

    if stack:
        answer = 0
    else:
        answer = 1

    return answer
