def solution(money):
    answer = []

    americano = money // 5500
    left_money = money % 5500

    answer = [americano, left_money]

    return answer