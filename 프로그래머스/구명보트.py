# 구명보트
"""
정렬한 뒤, 가장 큰 사람부터

최대 2명 -> 최대인 애랑 최소인 애를 태우면 됨
최대인 애랑 꾸역꾸역 굳이 태울 필요가 없음
-> 최대인 애랑도 같이 탈 수 있는애면 누구든 같이 탈 수 있는 애이므로
"""


def solution(people, limit):
    answer = 0

    people.sort(reverse=True)  # 무거운 순서로 정렬

    max_idx = 0
    min_idx = len(people) - 1

    while max_idx <= min_idx:
        if people[max_idx] + people[min_idx] <= limit:
            min_idx -= 1

        max_idx += 1
        answer += 1

    return answer