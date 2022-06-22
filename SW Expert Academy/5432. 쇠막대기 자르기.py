# 5432. 쇠막대기 자르기
"""
index를 키워가면서 확인 -> 현재 index에 포함된 막대 갯수를 저장해나가면서 확인(cur_stick)

"("가 나오고 "("가 나오면 막대 하나 추가 -> cur_sitck += 1

")"가 나온 시점에
바로 앞에 "("가 있으면 레이저 -> count += cur_stick
")"가 있으면 막대기 끝 -> count += 1, cur_stick -= 1
"""


if __name__ == "__main__":
    T = int(input())

    for test_case in range(1, T + 1):
        line = input()
        count = 0
        cur_stick = 0 # 현재 index에 있는 막대의 갯수

        i = 0 # 확인할 index
        while i < len(line) - 1: # line 끝에 도달할때까지
            cur, next = line[i], line[i + 1]
            if cur == "(":
                if next == ")": # 레이저
                    count += cur_stick
                    i += 2
                    # print("레이저로", cur_stick, "개 자름")
                else: # "("
                    cur_stick += 1
                    i += 1

            else: # cur == ")"
                # if next == ")":
                #     count += 1
                #     cur_stick -= 1
                #     i += 1
                # else:
                cur_stick -= 1
                count += 1
                # print("떨거지 막대기")
                i += 1

        count += cur_stick # 마지막에 혹시 막대가 남아있는 경우 떨거지 막대기를 더해줌

        print("#{} {}".format(test_case, count))

"""
2
()(((()())(())()))(())
(((()(()()))(())()))(()())
"""