# 876. Middle of the Linked List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from collections import deque

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        q = deque()
        curr_node = head
        
        while curr_node: # make deque from linked list
            curr_val = curr_node.val
            q.append(curr_val)
            curr_node = curr_node.next
        
        second_middle_node_index = 0
        
        # find second middle node index
        while q:
            if len(q) == 1:
                break
            
            else:
                first = q.popleft()
                last = q.pop()
                
                second_middle_node_index += 1
                
        # get node after second middle node index
        curr_node = head
        node_index = 0
        while curr_node:
            if node_index == second_middle_node_index:
                return curr_node
                        
            else:
                curr_node = curr_node.next
                node_index += 1
                
