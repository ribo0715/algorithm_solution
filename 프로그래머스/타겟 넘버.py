def solution(numbers, target):
    answer = 0

    n = len(numbers)  # 0부터 2^n - 1 까지 2진수로 확인

    for i in range(2 ** n):
        # i 에 대한 결과값 계산 -> 2진수로 표현했을 때, 1이면 -로 계산
        temp = i
        made_num = 0

        for j in range(n):
            x = temp % 2  #
            temp = temp // 2

            if x == 1:
                made_num += numbers[j]
            else:
                made_num -= numbers[j]

        if made_num == target:
            answer += 1
    # 순서를 바꾸지 않음, +/- 조합으로만
    # 전부 다 해봐도 될듯 -> 2진수로 표현된 값을 1씩 키워나간다?

    return answer