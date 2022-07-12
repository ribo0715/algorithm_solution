# 13. Roman to Integer

class Solution:
    
    def romanToInt(self, s: str) -> int:
        # value of each symbol
        value_dict = {"I" : 1, "V" : 5, "X" : 10, "L" : 50, "C" : 100, "D" : 500, "M" : 1000}
    
        output_int = 0
                      
        if len(s) == 1: # single symbol
            output_int = value_dict[s]
        
        else: # multiple symbol
            i = 0
            while i < len(s):
                curr_c = s[i]
                
                if i == len(s) - 1:
                    output_int += value_dict[curr_c]
                    break
                    
                next_c = s[i + 1] # check two continuous symbol
                
                if value_dict[curr_c] < value_dict[next_c]: # ex) CM
                    output_int += value_dict[next_c] - value_dict[curr_c]
                    i += 2
                    
                else: # ex) MC -> check up to M, and next, check after C~
                    output_int += value_dict[curr_c]
                    i += 1
        
        return output_int
