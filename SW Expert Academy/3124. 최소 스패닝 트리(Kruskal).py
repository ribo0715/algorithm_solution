# 3124. 최소 스패닝 트리 - Kruskal 알고리즘
"""
모든 정점들을 연결하는 부분 그래프 중에서 그 가중치의 합이 최소인 트리

1) Prim 알고리즘 -> 정점들을 기준으로 어떤 정점에서 가장 가중치가 낮은 쪽으로 이동해가며 연결 -> heap 이용
2) Kruskal 알고리즘 -> 간선들을 가중치 기준으로 정렬 -> 작은 것부터 연결해가면서 서브그래프의 root를 바꿔감

1
7 9
0 1 29
1 2 16
2 3 12
3 4 22
4 5 27
5 0 10
6 1 15
6 3 18
6 4 25
"""

#
def get_root(V_root, n):
    if n != V_root[n]:
        V_root[n] = get_root(V_root, V_root[n])

    return V_root[n]

if __name__ == "__main__":
    T = int(input())

    for test_case in range(1, T + 1):
        V, E = map(int, input().split()) # 정점의 개수 V(1≤V≤100,000)와 간선의 개수 E(1≤E≤200,000)

        V_root = [i for i in range(V + 1)] # i번 정점이 속한 서브 그래프의 root를 담을 배열
        E_list = [] # 모든 간선들을 담을 배열

        for _ in range(E):
            A, B, C = map(int, input().split()) # A번 정점과 B번 정점이 가중치 C인 간선으로 연결되어 있다
            E_list.append([A, B, C])

        E_list.sort(key=lambda x:x[2]) # 가중치 기준으로 정렬

        answer = 0

        # print(E_list)
        for A, B, C in E_list:

            A_root = get_root(V_root, A) # A에서
            B_root = get_root(V_root, B)

            if A_root != B_root:
                # print(A, B, C, "->", V_root)
                if A_root > B_root:
                    V_root[A_root] = B_root
                else:
                    V_root[B_root] = A_root

                answer += C

        print("#{} {}".format(test_case, answer))