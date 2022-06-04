# 전화번호 목록

def solution(phone_book):
    answer = True

    phone_book.sort()

    temp_len = 0

    for i in range(len(phone_book)):
        temp_len = len(phone_book[i])

        for j in range(i + 1, len(phone_book)):
            if len(phone_book[j]) <= temp_len:  # 길이가 더 짧아지면 그 번호로 시작되는 번호가 아님
                break

            if phone_book[j].startswith(phone_book[i]):
                answer = False
                return answer

    return answer