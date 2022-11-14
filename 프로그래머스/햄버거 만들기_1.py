def solution(ingredient):
    answer = 0
    
    stack = []
    
    # 1 2 3 1 이 나타나야함 -> 1이 들어오면 앞에 1 2 3 이 있는지 확인?    
    for x in ingredient:
        if len(stack) >= 3:
            if stack[-3:] == [1, 2, 3] and x == 1:
                stack = stack[:-3]
                answer += 1
                continue
                
        stack.append(x)
        
    
    return answer
