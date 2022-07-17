# 4. Median of Two Sorted Arrays

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged_length = len(nums1) + len(nums2)
        median_index = (merged_length - 1) // 2
        
        index = 0
        median_num = 0
        
        while index <= median_index:
            if not nums2:
                median_num = nums1.pop(0)
                
            elif not nums1:
                median_num = nums2.pop(0)
                
            elif nums1[0] >= nums2[0]:
                median_num = nums2.pop(0)
            else:
                median_num = nums1.pop(0)
            
            index += 1
        
        if merged_length % 2 == 0: # length == even num -> one more
            temp_num = 0
            if not nums2:
                temp_num = nums1.pop(0)
                
            elif not nums1:
                temp_num = nums2.pop(0)
                
            elif nums1[0] >= nums2[0]:
                temp_num = nums2.pop(0)
            else:
                temp_num = nums1.pop(0)
            
            median_num = (median_num + temp_num) / 2
            
        
        return median_num
            
            
            
