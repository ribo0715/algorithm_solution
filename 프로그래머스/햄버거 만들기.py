from collections import deque

def solution(ingredient):
    answer = 0
    
    stack = deque()
    
    # 1 2 3 1 이 나타나야함 -> 1이 들어오면 앞에 1 2 3 이 있는지 확인?    
    for x in ingredient:
        if len(stack) >= 3:
            if x == 1:
                if stack[-1] == 3 and stack[-2] == 2 and stack[-3] == 1:
                    stack.pop()
                    stack.pop()
                    stack.pop()
                    answer += 1
                    continue
                
        stack.append(x)
        
    
    return answer
