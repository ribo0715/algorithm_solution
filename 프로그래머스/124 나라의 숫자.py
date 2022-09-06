# 124 나라의 숫자
"""
[1, 2, 4] -> [1, 2, 3] 으로 바꾸고 3진법이라고 생각하면 될듯?

자연수 n이 매개변수로 주어질 때, n을 124 나라에서 사용하는 숫자로 바꾼 값을 return
"""


def solution(n):
    answer = ''

    cur_num = n
    while cur_num:
        leftover = cur_num % 3
        if leftover == 0:
            answer = "4" + answer
            cur_num = cur_num // 3 - 1
        else:
            answer = str(leftover) + answer
            cur_num = cur_num // 3

    return answer