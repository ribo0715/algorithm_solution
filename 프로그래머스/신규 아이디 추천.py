# 신규 아이디 추천

def solution(new_id):
    answer = ''
    id_list = []

    new_id = new_id.lower()  # 대문자 -> 소문자

    for char in new_id:  # 다른 모든 문자들 제거
        if char.isalpha() or char.isdigit() or char in ['-', '_', '.']:
            id_list.append(char)

    dot_flag = False
    for i in reversed(range(len(id_list))):
        if id_list[i] == '.':
            if dot_flag:  # 이전에도 .가 나온 경우
                id_list.pop(i)  # 제거
            dot_flag = True
        else:
            dot_flag = False

    if id_list:
        if id_list[0] == '.':
            id_list.pop(0)

    if id_list:
        if id_list[-1] == '.':
            id_list.pop()

    if not id_list:
        id_list.append("a")

    if len(id_list) >= 16:
        id_list = id_list[:15]
        if id_list[-1] == ".":
            id_list.pop()

    if len(id_list) <= 2:
        temp = id_list[-1]
        for _ in range(3 - len(id_list)):
            id_list.append(temp)

    answer = "".join(id_list)

    return answer