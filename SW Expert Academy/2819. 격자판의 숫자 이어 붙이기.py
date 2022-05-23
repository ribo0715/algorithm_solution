# 2819. 격자판의 숫자 이어 붙이기

# import sys
# input = sys.stdin.readline

from collections import deque

# 상 하 좌 우 이동
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def count_nums(grid):
    total_set = set() # 현재 grid에서 가능한 7자리 수 결과들을 담을 set

    for x in range(4):
        for y in range(4):
            q = deque()
            q.append([x, y, str(grid[x][y])])

            for _ in range(6): # 6번 이동
                for _ in range(len(q)):
                    cur_x, cur_y, cur_str = q.popleft()

                    for i in range(4): # 상 하 좌 우 로 이동
                        next_x = cur_x + dx[i]
                        next_y = cur_y + dy[i]

                        if 0 <= next_x < 4 and 0 <= next_y < 4:
                            next_num = grid[next_x][next_y]
                            next_str = cur_str + str(next_num)

                            q.append([next_x, next_y, next_str])

            while q:
                x, y, num_str = q.popleft()
                total_set.add(num_str)

    return len(total_set)

if __name__ == "__main__":
    T = int(input())

    for test_case in range(1, T + 1): # 테스트케이스마다 수행
        grid = []
        for _ in range(4):
            line = list(map(int, input().split()))
            grid.append(line)

        num_count = count_nums(grid)


        print("#{} {}".format(test_case, num_count))
