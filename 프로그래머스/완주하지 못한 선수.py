def solution(participant, completion):
    answer = ''

    #     participant.sort()
    #     completion.sort()

    #     answer = participant[-1]

    #     for i in range(len(completion)):
    #         if participant[i] != completion[i]:
    #             answer = participant[i]
    #             break

    hashDict = {}
    hashSum = 0

    for p in participant:
        h = hash(p)
        hashDict[h] = p
        hashSum += h

    for c in completion:
        h = hash(c)
        hashSum -= h

    answer = hashDict[hashSum]

    return answer