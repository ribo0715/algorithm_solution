def solution(cipher, code):
    answer = ''

    k = 1
    idx = code * k - 1

    while idx < len(cipher):
        answer += cipher[idx]
        k += 1
        idx = code * k - 1

    return answer