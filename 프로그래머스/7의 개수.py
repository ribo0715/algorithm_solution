def solution(array):
    array = map(str, array)

    temp = "".join(array)

    answer = temp.count("7")

    return answer