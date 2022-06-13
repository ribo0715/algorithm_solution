def solution(priorities, location):
    answer = 0

    prints = [0 for _ in range(len(priorities))]
    prints[location] = 1

    while True:
        while priorities[0] != max(priorities):
            priorities.append(priorities[0])
            del priorities[0]

            prints.append(prints[0])
            del prints[0]

        answer += 1

        if prints[0] == 1:
            break
        del priorities[0]
        del prints[0]

    return answer