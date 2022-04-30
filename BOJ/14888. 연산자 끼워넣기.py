# 14888. 연산자 끼워넣기

import sys

input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))
plus, minus, mult, div = map(int, input().split())

max_temp = -1e9 # -10억
min_temp = 1e9 # 10억


def dfs(count, total, plus, minus, mult, div):
    global max_temp, min_temp

    
    if count == n:
        max_temp = max(total, max_temp)
        min_temp = min(total, min_temp)
        return

    if plus:
        dfs(count + 1, total + num[count], plus - 1, minus, mult, div)

    if minus:
        dfs(count + 1, total - num[count], plus, minus - 1, mult, div)

    if mult:
        dfs(count + 1, total * num[count], plus, minus, mult - 1, div)

    if div:
        dfs(count + 1, int(total / num[count]), plus, minus, mult, div - 1)


dfs(1, num[0], plus, minus, mult, div)
print(max_temp)
print(min_temp)
