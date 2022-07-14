# 1. Two Sum

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            num = nums[i]
            necessary_num = target - num
            
            if necessary_num in nums[(i + 1):]: # check right side
                offset = nums[(i + 1):].index(necessary_num) + 1
                return [i, i + offset]
