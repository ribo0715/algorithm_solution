def solution(array, commands):
    answer = []
    
    for command in commands:
        i = command[0]
        j = command[1]
        k = command[2]
        
        temp_arr = array[i-1:j]
        sorted_arr = sorted(temp_arr)
        answer.append(sorted_arr[k-1])
        
    return answer
