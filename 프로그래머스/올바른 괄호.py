# 올바른 괄호
"""
잘못된 순간 바로 false 반환

스택 활용
"""


def solution(s):
    stack = []
    for cur in s:
        if stack:  # 스택에 무언가 들어있는 경우
            if stack[-1] == "(" and cur == ")":
                stack.pop()
            else:
                stack.append(cur)

        elif cur == ")":  # 스택이 비어있는데, )로 시작하려하면 false
            return False
        else:
            stack.append("(")

        # print(stack)

    if stack:
        return False
    else:
        return True