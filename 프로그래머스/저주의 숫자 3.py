"""
1부터 100번
3의 배수, 3이 들어간 수들 제외하고 넣음
"""

def solution(n):
    answer = 0
    
    answer_list = [0]
    num = 1 # 1부터 시작
    for i in range(n):
        flag = True
        while flag:
            if "3" in str(num):
                num += 1
            elif num % 3 == 0:
                num += 1
            else:
                answer_list.append(num)
                flag = False
                num += 1
            
    # print(answer_list)
    answer = answer_list[n]
    return answer
