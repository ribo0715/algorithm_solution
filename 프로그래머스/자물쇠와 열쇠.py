def get_rotated_key(key):  # 시계방향 90도 회전된 key 반환
    M = len(key)
    rotated_key = [[0 for _ in range(M)] for _ in range(M)]

    for i in range(M):
        for j in range(M):
            rotated_key[j][M - 1 - i] = key[i][j]

    return rotated_key


def solution(key, lock):
    answer = False
    M = len(key)
    N = len(lock)

    # 자물쇠의 홈이 있는 구역을 찾음
    left = -1
    right = -1
    up = -1
    down = -1
    for i in range(N):
        if 0 in lock[i]:
            if up == -1:
                up = i
            down = i

        is_zero = False
        for j in range(N):
            if lock[j][i] == 0:
                is_zero = True
                break

        if is_zero:
            if left == -1:
                left = i
            right = i

    # 자물쇠에 홈이 있는 구역 -> left, right, up, down 사이
    width = right - left + 1
    length = down - up + 1

    if width > M or length > M:  # 열쇠 크기보다 큰 구역에 홈이 있는 경우
        return False

    # 열쇠를 회전해가며 확인
    for _ in range(4):
        for di in range(M - length + 1):
            for dj in range(M - width + 1):
                is_able = True

                for i in range(M):
                    for j in range(M):
                        if 0 <= up - di + i < N and 0 <= left - dj + j < N:  # 자물쇠 위에 있는 지점
                            if lock[up - di + i][left - dj + j] == 1 and key[i][j] == 1:
                                is_able = False
                            if lock[up - di + i][left - dj + j] == 0 and key[i][j] == 0:
                                is_able = False
                        if not is_able:
                            break
                    if not is_able:
                        break

                if is_able:
                    return True

        key = get_rotated_key(key)

    return is_able