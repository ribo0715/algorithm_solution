def solution(s):
    answer = ''
    
    log = []
    answer_list = []
    
    for c in s:
        if c not in answer_list:
            answer_list.append(c)
    
        else:
            log.append(c)
        
    for target in log:
        if target in answer_list: 
            answer_list.remove(target)
            
    answer_list.sort()
    answer = "".join(answer_list)
    
    return answer
