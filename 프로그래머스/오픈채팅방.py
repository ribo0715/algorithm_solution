# 오픈채팅방
"""
채팅방에서 닉네임을 변경하는 방법
-> 채팅방을 나간 후, 새로운 닉네임으로 다시 들어간다.
-> 채팅방에서 닉네임을 변경한다.

딕셔너리 -> user_id : nickname

한번 쭉 읽고 각 user_id의 최종 nickname을 저장
"""


def solution(record):
    answer = []
    user_dic = {}

    for cur_record in record:
        cur = cur_record.split()

        if len(cur) == 3:
            user_id, nickname = cur[1:]
            user_dic[user_id] = nickname

    for cur_record in record:
        cur = cur_record.split()

        op, user_id = cur[:2]
        nickname = user_dic[user_id]

        line = nickname + "님이 "
        if op == "Enter":
            line += "들어왔습니다."
            answer.append(line)
        elif op == "Leave":
            line += "나갔습니다."
            answer.append(line)

    return answer