# N개의 최소공배수
"""
최대 15개의 수, 100이하
-> 그냥 다 해봐도 되려나?

각 수를 소인수분해 후 조합?
-> 소인수분해 한 결과는 딕셔너리로 저장
"""

from collections import defaultdict


def get_factorization(num):
    num_list = [1 for _ in range(num + 1)]  # num_list[i] -> i로 나누어지는지 확인해봐야할지를 담음
    dic = defaultdict(int)

    i = 2
    while i <= num:
        if num_list[i]:
            # i로 계속 나누어봄
            temp = num

            while temp % i == 0:  # num이 i로 몇번 나눠지는지 확인
                temp = temp // i
                dic[i] += 1

            # i의 배수들을 이후엔 확인하지 않도록 해줌
            for j in range(1, num // i + 1):
                num_list[i * j] = 0
        i += 1

    return dic


def solution(arr):
    answer = 1

    total_dic = defaultdict(int)

    for num in arr:
        temp_dic = get_factorization(num)  # num을 소인수분해

        for element in temp_dic:  # 소인수
            total_dic[element] = max(temp_dic[element], total_dic[element])

    for element in total_dic:
        answer *= element ** total_dic[element]

    return answer