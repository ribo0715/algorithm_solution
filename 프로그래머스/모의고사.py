def solution(answers):
    answer = []

    pick_1 = [1, 2, 3, 4, 5]  # 5개
    pick_2 = [2, 1, 2, 3, 2, 4, 2, 5]  # 8개
    pick_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]  # 10개

    score_1 = 0
    score_2 = 0
    score_3 = 0

    for i in range(len(answers)):
        if answers[i] == pick_1[i % 5]:
            score_1 += 1

        if answers[i] == pick_2[i % 8]:
            score_2 += 1

        if answers[i] == pick_3[i % 10]:
            score_3 += 1

    scores = [score_1, score_2, score_3]
    max_score = max(scores)

    for i in range(3):
        if scores[i] == max_score:
            answer.append(i + 1)

    return answer