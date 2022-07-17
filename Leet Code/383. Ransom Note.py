# 383. Ransom Note

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # change to list -> remove target letter from each list
        magazine_list = list(magazine)
        ransomNote_list = list(ransomNote)
        
        for letter in ransomNote_list: # for each letter in ransomNote
            if letter not in magazine_list:
                return False
            
            else:
                magazine_list.remove(letter)
            
        return True
                
