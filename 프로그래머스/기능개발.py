def solution(progresses, speeds):
    answer = []

    date = 1

    while len(progresses) > 0:
        finishNum = 0

        while progresses[0] + date * speeds[0] >= 100:
            del progresses[0]
            del speeds[0]

            finishNum += 1

            if len(progresses) == 0:
                break

        if finishNum > 0:
            answer.append(finishNum)

        date += 1  # 하루가 끝

    return answer