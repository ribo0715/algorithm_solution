# 크레인 인형뽑기 게임
"""
"N x N" 크기의 정사각 격자

같은 모양의 인형 두 개가 바구니에 연속해서 쌓이게 되면 두 인형은 터뜨려지면서 바구니에서 사라짐
-> 가장 위에 있는 것만 알면 됨 -> 스택(stack)
바구니는 모든 인형이 들어갈 수 있을 만큼 충분히 크다고 가정

게임 화면의 격자의 상태가 담긴 2차원 배열 board
인형을 집기 위해 크레인을 작동시킨 위치가 담긴 배열 moves

크레인을 모두 작동시킨 후 터트려져 사라진 인형의 개수를 return
"""


def solution(board, moves):
    answer = 0
    N = len(board)
    stack = []  # 바구니의 역할을 할 스택

    for k in range(len(moves)):  # N이 아니라 len(moves)로 수정!
        move = moves[k] - 1  # k번째 move의 값 -> 0부터 시작하게끔 1을 빼줌
        # move번째 줄 확인
        for i in range(N):
            if board[i][move]:  # 인형이 존재
                num = board[i][move]
                board[i][move] = 0

                if stack:
                    if stack[-1] == num:
                        stack.pop(-1)
                        answer += 2
                    else:
                        stack.append(num)
                else:
                    stack.append(num)

                break

    return answer