# 로또의 최고 순위와 최저 순위
"""
로또 -> 1~45 중 6개 선택
set으로?
중복되는걸 제외하고 남은 개수와 0의 개수를 확인

당첨 가능한 최고 순위, 최저 순위 반환
"""

# correct_nums 개수만큼 일치할 때, 그에 대한 순위를 반환
def return_ranking(correct_nums):
    if correct_nums <= 1:
        return 6
    else:
        return 7 - correct_nums
    

def solution(lottos, win_nums):    
    min_num = 0
    
    missed = lottos.count(0)
    for num_picked in lottos:
        if num_picked in win_nums:
            min_num += 1
    
    max_num = min_num + missed
    
    answer = [return_ranking(max_num), return_ranking(min_num)]
    
    return answer
