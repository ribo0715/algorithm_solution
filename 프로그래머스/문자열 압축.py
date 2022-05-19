# 문자열 압축
"""
길이가 n인 문자열을 1개단위, 2개단위, ... , n//2개단위로 나눌 수 있는지 확인
"""


# 문자열 s를 n개 단위로 압축할 때 결과를 반환
def merge_in_n_unit(s, n):
    min_length = len(s)

    # 0 1 2 3 4 5 6 7
    for j in range(1):  # j번째부터 시작해서 n개 단위로 확인 -> 문제 이상한 조건으로 인해 n을 1로 바꿔서 실행함
        temp_result = ""
        temp_result += s[:j]

        prev = ""
        count = 1
        for i in range((len(s) - j) // n):
            cur = s[n * i + j: n * (i + 1) + j]

            if prev == cur:
                count += 1
            else:
                if count >= 2:
                    temp_result += str(count) + prev
                else:
                    temp_result += prev

                prev = cur
                count = 1

        if count >= 2:
            temp_result += str(count) + prev
        else:
            temp_result += prev

        temp_result += s[j + (len(s) - j) // n * n:]  # 뒤 부분을 이어줌

        # print(n, "개 단위로 압축한 결과", temp_result)
        if min_length > len(temp_result):
            min_length = len(temp_result)

    return min_length


"""
ababbbbbbbb
2ab3bbb
aba4bb -> 맨 앞에서부터 나오는걸로 바로 자르는게 더 짧다는 보장이 없음
문제가 뭐 이러냐... 맨 앞에서부터 무조건 시작이어야 하나보다... 
"""


def solution(s):
    n = len(s)
    min_length = len(s)

    for i in range(1, n // 2 + 1):  # 1개 ~ n//2개 단위로 나눠봄
        temp_length = merge_in_n_unit(s, i)  # n개 단위로 압축할 때 최소 길이
        # print(i, "개로 압축했을 때의 최소 길이 :", temp_length)
        if min_length > temp_length:
            min_length = temp_length

    return min_length