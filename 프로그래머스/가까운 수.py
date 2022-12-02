def solution(array, n):
    answer = 0
    min_diff = 100
    
    for num in array:
        temp_diff = abs(num - n)
        if min_diff > temp_diff:
            answer = num
            min_diff = temp_diff
        elif min_diff == temp_diff:
            answer = min(answer, num)
            
    return answer
