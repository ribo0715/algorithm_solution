def solution(n, k):
    answer = 0

    answer += 12000 * n

    service = n // 10

    if k > service:
        answer += 2000 * (k - service)

    return answer