def solution(array, height):
    answer = 0

    array.append(height)
    array.sort()

    answer = len(array) - array.index(height) - 1

    return answer