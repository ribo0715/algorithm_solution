# 1223. [SW 문제해결 기본] 6일차 - 계산기2
"""
문자열로 이루어진 계산식이 주어질 때, 이 계산식을 후위 표기식으로 바꾸어 계산하는 프로그램
“3+4+5*6+7”
-> "34+56*+7+"
"""

def to_postfix_notation(line):
    result = ""

    op_stack = []

    for x in line:
        if "0" <= x <= "9":
            result += x

        elif x == "+":
            while op_stack:
                temp = op_stack.pop()
                result += temp
            op_stack.append(x)

        elif x == "*":
            if op_stack:
                if op_stack[-1] == "*":
                    temp = op_stack.pop()
                    result += temp
            op_stack.append(x)

        # print("현재 :", result, "op_stack", op_stack)

    while op_stack:
        temp = op_stack.pop() # 끝까지 보고 남은 op 붙여주기
        result += temp

    return result


def calc_postfix_notation(postfix_line):
    result = 0
    postfix_line = list(postfix_line)
    while len(postfix_line) > 1:
        # print(postfix_line)
        for i in range(len(postfix_line)):
            if postfix_line[i] == "+":
                temp = int(postfix_line[i - 2]) + int(postfix_line[i - 1])
                postfix_line = postfix_line[:i - 2] + [temp] + postfix_line[i + 1:]
                break
            elif postfix_line[i] == "*":
                temp = int(postfix_line[i - 2]) * int(postfix_line[i - 1])
                postfix_line = postfix_line[:i - 2] + [temp] + postfix_line[i + 1:]
                break

    result = int(postfix_line[0])
    return result


if __name__ == "__main__":
    for test_case in range(1, 11):
        n = int(input())
        line = input()

        postfix_line = to_postfix_notation(line)
        # print(postfix_line)
        answer = calc_postfix_notation(postfix_line)

        print("#{} {}".format(test_case, answer))