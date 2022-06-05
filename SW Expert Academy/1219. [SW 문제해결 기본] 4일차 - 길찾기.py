# 1219. [SW 문제해결 기본] 4일차 - 길찾기

from collections import defaultdict
from collections import deque


if __name__ == "__main__":
    while True:
        try: # input이 얼마나 들어올지에 대한 설명이 없기 때문에 try-except로 처리하였음
            test_case, nums = map(int, input().split())
            line = list(map(int, input().split()))

            dic = defaultdict(list) # 전체 경로들을 저장해둘 딕셔너리 -> dic[0] = [1,2] : 0에서 1, 2로 이동 가능
            for i in range(nums): # 전체 경로들을 저장
                start = line[2 * i]
                end = line[2 * i + 1]

                dic[start].append(end) # start -> end 로 이동가능

            # 0에서 시작해서 99에 도달 가능한지 확인
            q = deque()
            q.append(0)

            visited = set() # 방문 표시
            visited.add(0) # 0번에서 시작

            answer = 0

            while q:
                start = q.popleft()
                for next in dic[start]:
                    if next == 99:
                        answer = 1 # 도달 가능하면 answer을 1로 함
                        break
                    elif next not in visited: # 방문하지 않은 곳이면 방문표시
                        q.append(next)
                        visited.add(next)

                if answer == 1:
                    break

            print("#{} {}".format(test_case, answer))

        except EOFError:
            break
