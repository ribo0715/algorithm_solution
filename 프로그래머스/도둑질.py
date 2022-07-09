def solution(money):
    answer = 0

    dp = [0 for _ in range(len(money))]  # i번 집까지 봤을때, 가장 많이 터는 돈
    # 0번 집을 터는 경우
    dp[0] = money[0]

    for i in range(1, len(money) - 1):  # 마지막 집은 털 수 없음
        dp[i] = max(dp[i - 1], dp[i - 2] + money[i])

    max_for_first = max(dp)

    dp = [0 for _ in range(len(money))]
    # 0번 집을 털지 않는 경우
    dp[0] = 0
    dp[1] = money[1]
    for i in range(2, len(money)):  # 마지막까지 확인
        dp[i] = max(dp[i - 1], dp[i - 2] + money[i])

    max_for_last = max(dp)

    answer = max(max_for_first, max_for_last)

    return answer