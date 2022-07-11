# 7465. 창용 마을 무리의 개수


# x의 root를 반환
def get_root(root, x):
    cur = x
    while root[cur] != cur:
        cur = root[cur]

    return cur


if __name__ == "__main__":
    T = int(input())

    for test_case in range(1, T + 1):
        N, M = map(int, input().split())
        root = [i for i in range(N + 1)] # 각 번호의 root는 자기 자신으로 시작

        for _ in range(M):
            a, b = map(int, input().split()) # a, b 가 서로 아는 관계
            root_of_a = get_root(root, a)
            root_of_b = get_root(root, b)

            if root_of_a > root_of_b: # root의 번호가 작은쪽으로 root를 변경해줌
                root[root_of_a] = root_of_b
            else:
                root[root_of_b] = root_of_a

        total_set = set()
        # N개의 root를 확인하며 갯수 파악
        for i in range(1, N + 1):
            root_of_i = get_root(root, i)
            total_set.add(root_of_i)

        answer = len(total_set)
        print("#{} {}".format(test_case, answer))