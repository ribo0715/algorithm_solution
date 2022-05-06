# 표 편집 (기본)

from collections import deque

def find_index(sorted_arr, target_value):
    left = 0
    right = len(sorted_arr) - 1
    mid = (right + left) // 2

    if target_value > sorted_arr[right]:
        return right + 1

    while left < right:
        if target_value < sorted_arr[mid]:
            right = mid
        else:
            left = mid + 1
        mid = (right + left) // 2

    return mid


def solution(n, k, cmd):
    answer = ''

    array = [i for i in range(n)]  # 주어진 표의 상태
    curr = k  # 현재 선택하는 행의 index

    deleted_stack = deque()

    for comand in cmd:
        if comand[0] == "U":
            X = int(comand.split()[1])
            curr -= X

        elif comand[0] == "D":
            X = int(comand.split()[1])
            curr += X

        elif comand[0] == "C":
            deleted_element = array.pop(curr)
            if len(array) <= curr:
                curr -= 1

            deleted_stack.append(deleted_element)

        else:  # comand[0] == "Z"
            come_back = deleted_stack.pop()

            if come_back < array[curr]:
                curr += 1

            index = find_index(array, come_back)
            array.insert(index, come_back)

    for i in range(n):
        if i in array:
            answer += "O"
        else:
            answer += "X"

    return answer