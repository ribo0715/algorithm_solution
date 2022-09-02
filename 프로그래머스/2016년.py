# 2016년
"""
1월 1일 금요일 -> a월 b일은 무슨 요일?

몇일 차이인지 계산 -> 7로 나눔
"""


def solution(a, b):
    week = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]

    month_days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    total_day = sum(month_days[:a]) + b - 1
    answer = week[(total_day + 5) % 7]

    return answer