# 20055. 컨베이어 벨트 위의 로봇

from collections import deque
import sys
input = sys.stdin.readline

# 가장 먼저 벨트에 올라간 로봇부터, 벨트가 회전하는 방향으로 한 칸 이동할 수 있다면 이동
def robot_move():
    for i in range(N - 1):
        index = N - 2 - i
        target_robot = robot[index]

        if target_robot == 1:
            if A[index + 1] >= 1 and robot[index + 1] == 0:
                robot[index] = 0
                if index != N - 2:
                    robot[index + 1] = 1
                A[index + 1] -= 1


def belt_move():
    # 벨트 이동
    A.appendleft(A.pop())

    # 로봇 이동
    robot.pop()
    robot.appendleft(0)

    if robot[-1] == 1:
        robot[-1] = 0


def put_robot():
    if A[0] > 0:
        A[0] -= 1 # 올리는 위치 내구도 -1
        robot[0] = 1

# def print_belt():
#     for i in range(N):
#         print(A[i], end=" ")
#     print()
#     for i in range(N):
#         print(A[2*N - 1 - i], end=" ")
#     print()

if __name__ == "__main__":
    N, K = map(int, input().split())
    A = deque(list(map(int, input().split()))) # i번 칸의 내구도
    robot = deque([0 for _ in range(N)]) # 벨트 위 로봇들 상황을 담음

    time = 1
    while True:
        # print(time, "번째 단계")
        # print("로봇 위치 상태 :", robot)
        # print_belt()

        belt_move()
        # print("belt_move() 로봇 위치 상태 :", robot)
        # print_belt()

        robot_move()
        # print("robot_move() 로봇 위치 상태 :", robot)
        # print_belt()

        put_robot()
        # print("put_robot() 로봇 위치 상태 :", robot)
        # print_belt()

        if A.count(0) >= K:
            break

        time += 1

    print(time)

