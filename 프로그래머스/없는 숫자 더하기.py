# 없는 숫자 더하기

def solution(numbers):
    # answer = -1
    temp = set(range(10))
    # print(temp)
    
    for number in numbers:
        temp.discard(number)
    
    answer = sum(temp)
    return answer
