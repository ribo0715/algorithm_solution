# 14179. 복제한 수열의 인버전 수

# import sys
# input = sys.stdin.readline

if __name__ == "__main__":
    T = int(input())

    # 여러개의 테스트 케이스가 주어지므로, 각각을 처리
    for test_case in range(1, T + 1):
        N, K = map(int, input().split())
        arr = list(map(int, input().split()))

        temp = [[0, 0] for _ in range(N)] # 해당 index의 기준으로 왼쪽, 오른쪽에 더 작은 값이 몇개 있는지를 담음
        answer = 0
        for i in range(N):
            right, left = 0, 0
            for j in range(0, i): # 왼쪽
                if arr[i] > arr[j]:
                    left += 1

            for j in range(i, N): # 오른쪽
                if arr[i] > arr[j]:
                    right += 1

            temp[i] = [left, right]

            answer += left * (K - 1) * K // 2 + right * (K + 1) * K // 2
            # left * ( (K - 1) + (K - 2) + ... + 0 ) + right * ( K + (K - 1) + ... + 1 )
            # = (K - 1) * K / 2 + (K + 1) * K / 2

        answer = answer % (10 ** 9 + 7)
        print("#" + str(test_case), answer)
