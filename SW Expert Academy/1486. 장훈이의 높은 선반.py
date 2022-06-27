# 1486. 장훈이의 높은 선반
"""
높이가 B 이상인 탑 중에서 높이가 가장 낮은 탑
"""
from itertools import combinations

if __name__ == "__main__":
    T = int(input())

    for test_case in range(1, T + 1):
        N, B = map(int, input().split()) # 점원 N명, 선반의 높이 B
        H = list(map(int, input().split())) # 각 점원의 키를 저장

        if sum(H) < B:
            print("#{} {}".format(test_case, -1))
            continue
        elif sum(H) == B:
            print("#{} {}".format(test_case, N))
            continue

        min_gap = 1e9
        for k in range(1, N + 1):
            for combi in list(combinations(H, k)):
                sum_combi = sum(combi)
                if sum_combi >= B:
                    min_gap = min(sum_combi - B, min_gap)

                if min_gap == 0:
                    break
            if min_gap == 0:
                break

        print("#{} {}".format(test_case, min_gap))
