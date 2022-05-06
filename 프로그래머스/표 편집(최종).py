# 표 편집 (이중 링크드 리스트)

def solution(n, k, cmd):
    answer = ''
    linked_list = {i: [i - 1, i + 1] for i in range(n)} # prev, next로 어느 행을 가리키는지
    result = ["O" for _ in range(n)]

    curr = k
    deleted_stack = [] # C 로 삭제한 행에 대한 정보

    for comand in cmd:
        if comand[0] == "U":
            X = int(comand.split()[1])
            for _ in range(X):
                curr = linked_list[curr][0]

        elif comand[0] == "D":
            X = int(comand.split()[1])
            for _ in range(X):
                curr = linked_list[curr][1]

        elif comand[0] == "C":
            prev, next = linked_list[curr]

            result[curr] = "X"
            deleted_stack.append([prev, curr, next])

            if next == n: # 맨 뒤
                curr = linked_list[curr][0]
            else:
                curr = linked_list[curr][1]

            if prev == -1: # 맨 앞
                linked_list[next][0] = prev
            elif next == n: # 맨 뒤
                linked_list[prev][1] = next
            else:
                linked_list[prev][1] = next
                linked_list[next][0] = prev

        else:  # comand[0] == "Z"
            prev, temp, next = deleted_stack.pop()
            result[temp] = "O"

            if prev == -1: # 맨 앞
                linked_list[next][0] = temp
            elif next == n: # 맨 뒤
                linked_list[prev][1] = temp
            else:
                linked_list[prev][1] = temp
                linked_list[next][0] = temp

    answer = "".join(result)

    return answer