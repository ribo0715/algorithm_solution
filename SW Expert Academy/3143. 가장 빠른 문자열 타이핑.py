# 3143. 가장 빠른 문자열 타이핑
"""
A와 B가 주어질 때 A 전체를 타이핑 하기 위해 키를 눌러야 하는 횟수의 최솟값
"""


# A의 i번째 index에서부터 B를 사용할 수 있는지
def check_i(A, B, i):
    if A[i:].startswith(B):
        return True
    else:
        return False


if __name__ == "__main__":
    T = int(input())

    for test_case in range(1, T + 1):
        A, B = input().split()
        answer = len(A)
        # index를 0부터 확인해가면서, B를 해당 index부터 사용할 수 있는지 확인
        i = 0
        while i <= len(A) - len(B) + 1:
            if check_i(A, B, i):
                answer -= len(B) - 1
                i += len(B)
            else:
                i += 1

        print("#{} {}".format(test_case, answer))
