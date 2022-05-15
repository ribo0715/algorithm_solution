# 파괴되지 않은 건물
"""
매 skill마다 전체 board를 업데이트해주는 방법은 아니지 않을까?
왠지 그냥 하면 시간초과가 날 것 같은데... 어떤 방법 없을까...
-> IMOS 알고리즘, 누적합
"""

def solution(board, skill):
    answer = 0

    n = len(board)  # 세로(행)
    m = len(board[0])  # 가로(열)

    imos = [[0 for _ in range(m + 1)] for _ in range(n + 1)]  # 누적합, IMOS알고리즘

    for type, r1, c1, r2, c2, degree in skill:
        if type == 1:  # 적의 공격
            imos[r1][c1] -= degree  # (r1, c1)부터
            imos[r2 + 1][c2 + 1] -= degree  # (r2, c2)까지 -> (r2 + 1, c2 + 1)이전까지 되도록
            imos[r1][c2 + 1] += degree
            imos[r2 + 1][c1] += degree
        else:  # type == 2 -> 아군 회복
            imos[r1][c1] += degree  # (r1, c1)부터
            imos[r2 + 1][c2 + 1] += degree  # (r2, c2)까지 -> (r2 + 1, c2 + 1)이전까지 되도록
            imos[r1][c2 + 1] -= degree
            imos[r2 + 1][c1] -= degree

    # 오른쪽 방향으로 누적합 계산
    for r in range(n + 1):
        for c in range(1, m + 1):
            imos[r][c] += imos[r][c - 1]

            # 아래 방향으로 누적합 계산
    for c in range(m):
        for r in range(1, n + 1):
            imos[r][c] += imos[r - 1][c]

    # 전체 건물의 상태를 확인
    for r in range(n):
        for c in range(m):
            if board[r][c] + imos[r][c] >= 1:  # 내구도가 1 이상인 경우
                answer += 1  # count해줌

    return answer