# 피로도
"""
최소 필요 피로도 - 던전 탐험을 시작하기 위해 필요한 최소 피로도
소모 피로도 - 던전 탐험을 마쳤을 때 소모

최대한 많이 탐험하려 함
현재 피로도 k
유저가 탐험할 수 있는 최대 던전 수 반환

던전 개수 8개 이하 -> 전체 모든 경우를 파악해도 8! 경우
-> 그냥 다 시도해봐도 좋을 듯
"""

from itertools import permutations


def solution(k, dungeons):
    answer = -1

    n = len(dungeons)  # 던전 개수 : n개
    perm_list = list(permutations(range(n), n))
    # print(perm_list)
    max_count = 0

    for perm in perm_list:
        # 해당 순서대로 하면 몇개까지 탐험할 수 있는지 확인
        cur_fatigue = k
        cur_count = 0

        for num in perm:
            if cur_fatigue >= dungeons[num][0]:
                cur_fatigue -= dungeons[num][1]
                cur_count += 1

        max_count = max(max_count, cur_count)

    answer = max_count

    return answer