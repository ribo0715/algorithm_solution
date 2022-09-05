# 두 큐 합 같게 만들기
"""
두 개의 큐 -> 한쪽에서 빼고(pop) 다른쪽에 넣기(insert) -> deque 이용
-> 각 큐의 원소 합이 같아질때까지

단순한 bfs로 하면 2 ^ n 이 되므로 이건 아닌듯...
-> 어떤 방법으로도 같아지지 않는 경우에 대해 판단하기가 어려울 듯
-> 전체 합이 홀수인 경우 그냥 바로 끝내도 될듯?

전체 원소의 합을 구하고 그의 절반이 되는 상황을 미리 생각해두는게 편할까?
-> 큐의 길이가 30만까지 있는걸 보면... 이것도 아닌 것 같음

총 합을 더하는데 계속 sum을 쓰는건 별로 좋지 않을듯, sum을 따로 저장해두고 pop되는 값을 더하고 빼는게 좋을 듯
-> sum1, sum2로 queue1, queue2의 원소 합을 저장

절대 불가능한 경우를 어떻게 판단할 수 있을까?

"""

from collections import deque


def solution(queue1, queue2):
    answer = 0
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    queue1 = deque(queue1)
    queue2 = deque(queue2)

    if (sum1 + sum2) % 2 != 0:  # 전체 합이 홀수인 경우, 바로 끝
        return -1

    for _ in range(3 * len(queue1)):
        if sum1 > sum2:
            sum1 -= queue1[0]
            sum2 += queue1[0]
            queue2.append(queue1.popleft())
        elif sum1 < sum2:
            sum1 += queue2[0]
            sum2 -= queue2[0]
            queue1.append(queue2.popleft())
        else:
            return answer
        answer += 1
        
    return -1