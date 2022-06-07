# 4366. 정식이의 은행업무
"""
각 수의 자릿수 -> 3 ~ 40자리 -> 모두 확인하면 최대 1600가지 경우 -> 해도 괜찮을듯

2진수의 각 자리를 한칸씩 변경하면서, 그 값에 해당하는 3진수가 하나빼고 일치하는지 확인
-> 2진수면 0은 1로, 1은 0으로 바꾸면 되므로
"""


def get_answer(num_2_str, num_3_str):
    num_2_len = len(num_2_str)

    for i in range(num_2_len): # i번째를 제외
        if num_2_str[i] == "0":
            changed_num_2_str = num_2_str[:i] + "1" + num_2_str[i + 1:]
        else:
            changed_num_2_str = num_2_str[:i] + "0" + num_2_str[i + 1:]
        changed_num = int(changed_num_2_str, 2) # 2진수 값을 10진수로 변환 -> int(x, 2)로 가능

        changed_num_3_str = ""
        cur_num = changed_num
        index = 0
        count = 0 # 3진수로 바꿨을때 값이 다른 자리의 갯수 카운트 -> 1개가 넘어가면 바로 끝
        while cur_num and count <= 1:
            temp = cur_num % 3
            if str(temp) != num_3_str[-1 - index]:
                count += 1

            changed_num_3_str = str(temp) + changed_num_3_str
            cur_num = cur_num // 3
            index += 1

        if count == 1 and len(changed_num_3_str) == len(num_3_str):
            return changed_num


if __name__ == "__main__":
    T = int(input())

    for test_case in range(1, T + 1):
        num_2_str = input()
        num_3_str = input()


        # 2진수의 각 자리를 한칸씩 변경하면서, 그 값에 해당하는 3진수가 하나빼고 일치하는지 확인
        answer = get_answer(num_2_str, num_3_str)
        print("#{} {}".format(test_case, answer))

