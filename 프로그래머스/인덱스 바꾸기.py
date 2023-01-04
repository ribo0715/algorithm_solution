def solution(my_string, num1, num2):
    answer = ''

    answer = list(my_string)
    answer[num2] = my_string[num1]
    answer[num1] = my_string[num2]

    answer = "".join(answer)

    return answer