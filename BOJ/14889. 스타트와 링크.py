# 14889. 스타트와 링크

"""
총 N명이고 신기하게도 N은 짝수

N/2명으로 이루어진 스타트 팀과 링크 팀

사람에게 번호를 1부터 N까지로 배정

능력치 Sij는 i번 사람과 j번 사람이 같은 팀에 속했을 때, 팀에 더해지는 능력치

팀의 능력치는 팀에 속한 모든 쌍의 능력치 Sij의 합

능력치의 차이를 최소로

첫째 줄에 N(4 ≤ N ≤ 20, N은 짝수)

둘째 줄부터 N개의 줄에 S


"""


# 0 ~ n 의 수들을 두 집합으로 나눔
# 각 경우의 능력치 차이 값을 비교해나감

def calc_diff_s(n, s, team_A, team_B):
    total_A, total_B = 0, 0

    ##    print(n)
    # 두 사람씩 묶어 능력치 계산
    for i in range(n - 1):
        for j in range(i + 1, n):
            x = team_A[i]
            y = team_A[j]

            total_A += s[x][y] + s[y][x]

            z = team_B[i]
            w = team_B[j]

            total_B += s[z][w] + s[w][z]

    return abs(total_A - total_B)


min_diff = 1e9


def split_team(n, count, team_A, team_B, s):  # count 번까지 팀을 나누었을때, A,B팀의 멤버들
    global min_diff

    if count == n:
        if len(team_A) == len(team_B) == n / 2:
            # 능력치 차이 값을 비교
            diff = calc_diff_s(n // 2, s, team_A, team_B)
            min_diff = min(min_diff, diff)

            ##            print("A :", team_A, "B :", team_B)
            return

    # team_A에 추가
    if len(team_A) < n / 2:
        split_team(n, count + 1, team_A + [count], team_B, s)

    # team_B에 추가
    if len(team_B) < n / 2:
        split_team(n, count + 1, team_A, team_B + [count], s)


import sys

input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    s = [[] for _ in range(n)]

    for i in range(n):
        s[i] = list(map(int, input().split()))

    split_team(n, 0, [], [], s)

    print(min_diff)
