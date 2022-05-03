# 4408. 자기 방으로 돌아가기

if __name__ == "__main__":
    T = int(input())

    for test_case in range(1, T + 1):
        N = int(input())

        total_sum = [0 for _ in range(200)] # 각 지점에 학생이 몇 번 이동하는지를 다 더함 -> 최대값이 최단 시간
        # 긴 막대기들을 다 쌓아올리는 느낌 -> 겹칠 수 있는건 최고 효율로 알아서 겹쳐짐

        for i in range(N):
            start, end = map(int, input().split())

            # (1,2)가 같은 구간, (3,4)가 같은 구간이므로 묶어서 생각함
            start = (start - 1) // 2
            end = (end - 1) // 2

            start, end = sorted([start, end])

            for x in range(start, end + 1): # 해당 학생의 이동 구간 표시
                total_sum[x] += 1

        min_time = max(total_sum)

        print("#" + str(test_case), min_time)
        # print("#{} {}".format(test_case, min_time)) # 또 다른 출력 방법 -> 알아두면 좋을 듯