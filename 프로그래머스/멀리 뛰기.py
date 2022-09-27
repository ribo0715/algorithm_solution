# 멀리 뛰기
"""
n을 1, 2 의 조합으로 더할 수 있는 가지 수
-> dp 쓰면 될 듯?
"""


def solution(n):
    answer = 0

    dp = {}
    dp[1] = 1
    dp[2] = 2

    # dp[n] = dp[n - 1] + dp[n - 2]
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    answer = dp[n] % 1234567

    return answer