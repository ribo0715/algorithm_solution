def solution(prices):  # 가격이 떨어지지 않은 기간은 몇 초인지를 return
    answer = [len(prices) - i - 1 for i in range(len(prices))]

    stack = [0]

    for i in range(1, len(prices)):
        while stack and prices[i] < prices[stack[-1]]:
            j = stack.pop()
            answer[j] = i - j

        stack.append(i)

    return answer