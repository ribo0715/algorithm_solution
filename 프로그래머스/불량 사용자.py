# 불량 사용자

from collections import deque
import copy


def check_banned(target, ban):
    # 길이 확인
    length_ban = len(ban)
    length_target = len(target)

    if length_ban != length_target:
        return False

    for i in range(length_ban):
        if ban[i] == "*":
            continue

        if target[i] != ban[i]:
            return False

    return True


def solution(user_id, banned_id):
    # banned_id를 하나씩 확인하며 현재 user_id에서 가능한 ban_id를 추가해감

    left_user_id = copy.deepcopy(user_id)
    left_banned_id = copy.deepcopy(banned_id)

    q = deque()  # 현재 남은 user_id, banned_id 를 담음
    q.append([left_user_id, left_banned_id])
    visited = []
    visited.append([left_user_id, left_banned_id])

    for i in range(len(banned_id)):
        for _ in range(len(q)):
            left_user_id, left_banned_id = q.popleft()
            temp_banned_id = copy.deepcopy(left_banned_id)

            cur_banned_id = temp_banned_id.pop(0)

            for j in range(len(left_user_id)):
                if check_banned(left_user_id[j], cur_banned_id):
                    temp_user_id = copy.deepcopy(left_user_id)
                    temp_user_id.pop(j)

                    if [temp_user_id, temp_banned_id] not in visited:
                        q.append([temp_user_id, temp_banned_id])
                        visited.append([temp_user_id, temp_banned_id])

    answer = len(q)

    return answer
