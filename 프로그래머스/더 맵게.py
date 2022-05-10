# 더 맵게

import heapq

def solution(scoville, K):
    answer = 0

    heapq.heapify(scoville)

    while scoville[0] < K:  # 제일 작은 수가 K 이상이 되면 끝
        if len(scoville) == 1:  # 모든 음식의 스코빌 지수를 K 이상으로 하지 못한 경우 -1 을 리턴
            return -1

        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)

        new = first + second * 2
        heapq.heappush(scoville, new)

        answer += 1

    return answer