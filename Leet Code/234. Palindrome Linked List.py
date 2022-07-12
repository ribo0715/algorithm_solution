# 234. Palindrome Linked List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from collections import deque

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        q = deque() # node_val deque
        curr_node = head
        
        while curr_node: # append to q
            curr_val = curr_node.val
            q.append(curr_val)
            
            curr_node = curr_node.next # move to next node
        
        while q:
            if len(q) == 1: # single node_val left
                return True
            
            else:
                first = q.popleft()
                last = q.pop()
                
                if first != last: # palindrome
                    return False
                
        return True
            
