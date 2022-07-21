# 1337. The K Weakest Rows in a Matrix

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        soldiers_num_list = [] # soldiers_num for each row
        
        for row in mat:
            soldiers_num = row.count(1)
            soldiers_num_list.append(soldiers_num)
        
        answer = []
        
        for i in range(k):
            weakest_value = min(soldiers_num_list)
            weakest_index = soldiers_num_list.index(weakest_value)
            answer.append(weakest_index)
            soldiers_num_list[weakest_index] = 101 # make biggest_value
        
        return answer
