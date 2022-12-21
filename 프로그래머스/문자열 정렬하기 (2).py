def solution(my_string):
    answer = ''

    my_string = my_string.lower()
    my_string_sorted_list = sorted(list(my_string))

    answer = "".join(my_string_sorted_list)

    return answer