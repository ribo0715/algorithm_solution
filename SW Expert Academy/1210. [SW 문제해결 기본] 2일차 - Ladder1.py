# 1210. [SW 문제해결 기본] 2일차 - Ladder1
"""
100 x 100 크기의 2차원 배열로 주어진 사다리에 대해서, 지정된 도착점에 대응되는 출발점 X를 반환하는 코드
‘0’으로 채워진 평면상에 사다리는 연속된 ‘1’로 표현된다. 도착 지점은 '2'로 표현된다
"""

if __name__ == "__main__":
    for _ in range(10):
        test_case = int(input())
        ladder = []
        for _ in range(100):
            line = [0] + list(map(int, input().split())) + [0] # 양옆으로 0을 더 붙여 끝에서도 양쪽을 확인할 수 있도록 함 -> 이후 결과값에서 index를 -1 해줘야함
            ladder.append(line)

        # 맨 아래 X부터 위로 올라감
        x, y = 99, ladder[99].index(2)

        # 올라가면서 왼쪽 or 오른쪽 으로 이동할 수 있으면 계속 이동
        while x > 0: # 맨 위에 도달하기까지 이동
            if ladder[x][y - 1] == 1:
                while ladder[x][y - 1] == 1: # 왼쪽으로 이동할 수 있으면 끝까지 이동
                    y -= 1

                x -= 1
                continue

            if ladder[x][y + 1] == 1:
                while ladder[x][y + 1] == 1: # 오른쪽으로 이동할 수 있으면 끝까지 이동
                    y += 1

                x -= 1
                continue

            x -= 1

        answer = y - 1
        print("#{} {}".format(test_case, answer))