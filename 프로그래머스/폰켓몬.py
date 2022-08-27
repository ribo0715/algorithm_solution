# 폰켓몬
"""
N 마리 중에서 N/2 마리를 가짐
-> 최대한 다양한 종류의 폰켓몬을 가지도록
-> 그때의 폰켓몬 종류 번호의 개수 반환

중복되는 번호는 의미가 없음 -> 중복 제거 -> set로 바꿈
N/2보다 갯수가 적으면, 모든 종류의 폰켓몬을 선택해야함
N/2보다 갯수가 많으면, 아무리 가져도 N/2개이므로 N/2
"""


def solution(nums):
    N = len(nums)
    count = N / 2

    answer = min(len(set(nums)), N / 2)

    return answer