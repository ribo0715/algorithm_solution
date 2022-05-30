# 3752. 가능한 시험 점수

from collections import deque


def calc_possible_case_num(scores, N):
    q = deque()
    possible_score = set() # 현재까지 가능한 점수들을 담음

    index = 0
    # 첫번째 문제를 맞춘 경우, 못맞춘 경우
    q.append(0)
    q.append(scores[index])

    possible_score.add(0)
    possible_score.add(scores[index])

    index += 1

    while q and index < N:
        for _ in range(len(q)):
            curr_score = q.popleft()

            q.append(curr_score) # index번째 문제를 틀린 경우
            temp_score = curr_score + scores[index] # index번째 문제를 맞춘 경우
            if temp_score not in possible_score:
                possible_score.add(temp_score)
                q.append(temp_score)

        index += 1

    return len(possible_score)


if __name__ == "__main__":
    T = int(input())

    for test_case_num in range(1, T + 1):
        N = int(input())
        scores = list(map(int, input().split()))
        scores.sort(reverse=True)
        answer = calc_possible_case_num(scores, N)

        print("#{} {}".format(test_case_num, answer))

