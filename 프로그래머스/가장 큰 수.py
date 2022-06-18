import operator


def solution(numbers):
    answer = ''

    dic = {}

    #     for num in numbers:
    #         temp = num % 10
    #         l = len(str(num))

    #         str_modified_num = str(num) + str(temp) * (4 - l) # 4자리로 변환한 수 str 형식
    #         dic[num] = int(str_modified_num)

    #     sorted_dic = sorted(dic.items(), key = operator.itemgetter(1), reverse = True)

    # for x in sorted_dic:
    #     answer += str(x[0])

    str_numbers = list(map(str, numbers))

    # str_numbers.sort(key = lambda x : x + x[-1] * (4 - len(x)), reverse = True)
    str_numbers.sort(key=lambda x: x * 3, reverse=True)

    answer = str(int(''.join(str_numbers)))

    return answer