# 예상 대진표
"""
이진탐색과 같이 점점 올라가도록함

아래로 내려가면서 해도 같지않을까? -> 어짜피 최악의 경우 같은 시간복잡도니까

1~2 / 1~4 / 1~8/ 1~16 / 1~32 / 1~64
"""

import math


def solution(n, a, b):
    left = 0
    right = n

    count = math.log2(n)

    while left < right:  # a와 b를 찾으러 갈때 지나가는 노드
        mid = (left + right) // 2

        if a <= mid and b <= mid:
            right = mid
        elif mid < a and mid < b:
            left = mid + 1
        else:
            break

        count -= 1

    answer = count
    return answer