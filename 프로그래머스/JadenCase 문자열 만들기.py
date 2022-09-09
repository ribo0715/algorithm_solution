# JadenCase 문자열 만들기
"""
JadenCase -> 모든 단어의 첫 문자가 대문자이고, 그 외의 알파벳은 소문자인 문자열
첫 문자가 알파벳이 아닐 때에는 이어지는 알파벳은 소문자로

s는 길이 1 이상 200 이하인 문자열입니다.
s는 알파벳과 숫자, 공백문자(" ")로 이루어져 있습니다.
 숫자는 단어의 첫 문자로만 나옵니다.
 숫자로만 이루어진 단어는 없습니다.
 공백문자가 연속해서 나올 수 있습니다.

"""


def get_JadenCase(word):
    # 숫자로 시작하면 나머지 전부 소문자
    if word[0].isdigit():
        word = word.lower()
    # 알파벳으로 시작하면, 대문자로 시작, 나머지 전부 소문자
    else:
        word = word.capitalize()

    return word


def solution(s):
    answer = ''

    cur_word = ""  # 현재 확인중인 단어
    for i in range(len(s)):
        if s[i] == " ":  # 공백
            if cur_word:  # 이 조건을 달아주지 않으면, 런타임 에러 남 ->
                answer += get_JadenCase(cur_word)
            cur_word = ""
            answer += " "
        else:
            cur_word += s[i]

        i += 1

    if cur_word:  # 마지막 단어
        answer += get_JadenCase(cur_word)

    return answer
