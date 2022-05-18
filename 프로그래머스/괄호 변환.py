# 괄호 변환

# 문자열 u가 '올바른 괄호 문자열'인지 확인 -> 스택 활용
def is_right(u):
    if not u:
        return True

    stack = []
    if u[0] == ")":
        return False
    else:
        stack.append("(")  # "("

    for i in range(1, len(u)):
        if not stack:  # stack이 비어있는 경우
            if u[i] == ")":
                return False
            else:
                stack.append("(")

        elif stack[-1] == "(":
            if u[i] == "(":
                stack.append("(")
            else:  # ")"
                stack.pop()

    if stack:
        return False
    else:
        return True


# 문자열 w가 "균형잡힌 괄호 문자열"일때, "올바른 괄호 문자열"로 변환
def make_right(w):
    result = ""
    if not w:  # 1.
        return result

    # 2.
    count = 0
    index = 0
    for i in range(len(w)):
        if w[i] == "(":
            count += 1
        else:
            count -= 1

        if count == 0:
            index = i
            break  # 가장 빨리 균형이 잡히는 순간 -> index번째까지 균형잡힌 괄호 문자열

    u = w[:index + 1]
    v = w[index + 1:]

    if is_right(u):  # 3. u가 "올바른 괄호 문자열"인 경우
        result += u
        result += make_right(v)

    else:  # 4. u가 "올바른 괄호 문자열"이 아닌 경우
        temp = "("
        temp += make_right(v)
        temp += ")"

        u = u[1:-1]
        for i in range(len(u)):
            if u[i] == "(":
                temp += ")"
            else:
                temp += "("

        result = temp

    return result


def solution(p):
    answer = ''

    answer = make_right(p)

    return answer