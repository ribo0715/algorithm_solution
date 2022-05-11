# 이중우선순위큐

import heapq

max_heap = []
min_heap = []


def solution(operations):
    answer = []

    for op in operations:
        temp = op.split()

        if temp[0] == 'I':
            insert_queue(int(temp[1]))
        elif temp[0] == 'D':
            if len(max_heap) == 0:  # 빈 큐에 데이터를 삭제하라는 경우 무시
                continue

            if temp[1] == '1':
                delete_max()
            elif temp[1] == '-1':
                delete_min()

    if len(max_heap) == 0:
        return [0, 0]
    else:
        max = max_heap[0][1]
        min = min_heap[0]

        answer = [max, min]

    return answer


def insert_queue(num):
    heapq.heappush(max_heap, (-num, num))
    heapq.heappush(min_heap, num)  # 기본 heapq 는 min_heap


def delete_max():
    max_num = heapq.heappop(max_heap)[1]
    min_heap.remove(max_num)


def delete_min():
    min_num = heapq.heappop(min_heap)
    max_heap.remove((-min_num, min_num))