# 3. Longest Substring Without Repeating Characters

from collections import deque

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        
        q = deque() # store current sub string
        
        # how to check space? -> change string to list
        s_list = list(s)
        curr_length = 0
        
        for c in s_list:
            if c in q: # if repeating character
                curr_length = len(q)
                if curr_length > max_length: # compare length
                    max_length = curr_length
                    # print(q)
                    
                target_index = q.index(c)
                for i in range(target_index + 1):
                    q.popleft()
                    
            q.append(c) # add character
        
        curr_length = len(q)
        if curr_length > max_length: # finished but now is max
            max_length = curr_length
            
        return max_length
        
    
