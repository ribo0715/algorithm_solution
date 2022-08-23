# 숫자 문자열과 영단어
"""
일부 자릿수를 영단어로 바꾼 것을 보고, 원래 숫자를 찾는 게임
-> 숫자의 일부 자릿수가 영단어로 바뀌어졌거나, 혹은 바뀌지 않고 그대로인 문자열
-> 의미하는 원래 숫자를 반환

s가 숫자로 시작하면 그대로 answer에 넣어줌(s에선 제거)
문자로 시작하면, 어떤 숫자에 대한 영단어인지 파악 후 answer로 넘겨줌(해당 길이만큼 제거)
"""


def solution(s):
    answer = ""

    num_words = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

    while s:
        # print(s)
        if s[0].isdigit():
            answer += s[0]
            s = s[1:]
        else:
            for num_word in num_words:
                if s.startswith(num_word):
                    idx = num_words.index(num_word)
                    answer += str(idx)
                    s = s[len(num_word):]
                    break

    answer = int(answer)
    return answer