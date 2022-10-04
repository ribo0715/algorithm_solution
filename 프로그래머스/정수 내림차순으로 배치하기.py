# 정수 내림차순으로 배치하기

def solution(n):
    answer = ""

    # 각 숫자가 몇개 있는지 세고, 차례대로 배치
    num_count = [0] * 10  # num_count[i] -> i가 몇개 있는지

    for i in range(10):
        str_n = str(n)
        cur_count = str_n.count(str(i))
        num_count[i] = cur_count

    for i in reversed(range(10)):
        answer += str(i) * num_count[i]

    answer = int(answer)

    return answer