# 3289. 서로소 집합

def get_root(root, x):
    num = x
    while root[num] != num:
        num = root[num]

    return num

if __name__ == "__main__":
    T = int(input())

    for test_case in range(1, T + 1):
        answer = ""

        n, m = map(int, input().split())
        root = [i for i in range(n + 1)] # n개의 원소에 대해 각 원소가 속한 집합의 중심이 누구인지

        for _ in range(m): # m번 연산 수행
            op, a, b = map(int, input().split())

            if op == 0: # 합집합 -> a가 속한 집합, b가 속한 집합을 합침
                root_of_a = get_root(root, a)
                root_of_b = get_root(root, b)

                if root_of_a < root_of_b:
                    root[root_of_b] = root_of_a
                else:
                    root[root_of_a] = root_of_b

            else: # a, b가 같은 집합에 포함되어 있는지 확인 -> answer에 결과를 더함
                root_of_a = get_root(root, a)
                root_of_b = get_root(root, b)

                if root_of_a == root_of_b: # 같은 집합에 속하는 경우
                    answer += "1"
                else:
                    answer += "0"


        print("#{} {}".format(test_case, answer))
