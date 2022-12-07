def solution(order):
    answer = 0

    nums = list(str(order))
    for num in nums:
        if num in ['3', '6', '9']:
            answer += 1

    return answer