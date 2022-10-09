# 괄호 회전하기
"""
왼쪽으로 x칸만큼 회전, s가 올바른 괄호 문자열이 되게 하는 x의 개수
-> for _ in range(s) 로 한번씩 넘기면서 확인하면 될듯

stack 활용하면 될듯
"""

left = ["(", "[", "{"]
right = [")", "]", "}"]


def check(s):
    stack = []

    for i in range(len(s)):
        cur = s[i]
        if cur in left:
            stack.append(cur)
        else:
            if stack:
                prev = stack.pop()
                if left.index(prev) != right.index(cur):
                    return False
            else:
                return False
    if stack:
        return False
    else:
        return True


def solution(s):
    answer = 0

    for i in range(len(s)):
        temp = s[i:] + s[:i]

        if check(temp):  # temp가 올바른 괄호 문자열인지 확인
            answer += 1

    return answer