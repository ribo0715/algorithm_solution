# 3234. 준환이의 양팔저울
import math


# 저울 왼쪽의 총 무게합 : left_sum, 오른쪽의 총 무게합 : right_sum, 앞으로 저울에 더 올려야 하는 무게추들 : remain
# 일 때, 가능한 경우의 수를 구하는 함수
def dfs(left_sum, right_sum, remain):
    if not remain: # 저울에 전부 다 올린 경우
        return 1

    if left_sum >= half:
        return (2 ** len(remain)) * math.factorial(len(remain))

    result = 0
    for i in range(len(remain)):
        target = remain[i]
        next_remain = remain[:i] + remain[i + 1:] # i번째를 제외
        result += dfs(left_sum + target, right_sum, next_remain) # 왼쪽에 i번째 무게추를 더함
        if left_sum >= right_sum + target: # 오른쪽에 더할 수 있는 경우
            result += dfs(left_sum, right_sum + target, next_remain)

    return result


if __name__ == "__main__":
    T = int(input())

    for test_case in range(1, T + 1):
        N = int(input())
        line = list(map(int, input().split()))
        half = (sum(line) + 1) // 2

        answer = dfs(0, 0, line)

        print("#{} {}".format(test_case, answer))
