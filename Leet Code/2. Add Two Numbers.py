# 2. Add Two Numbers

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # linkdlist -> int
        first = 0
        second = 0
        
        first_node = l1
        count = 0
        while first_node:
            temp_val = first_node.val
            first += temp_val * (10 ** count)
            first_node = first_node.next
            count += 1
            
        second_node = l2
        count = 0
        while second_node:
            temp_val = second_node.val
            second += temp_val * (10 ** count)
            second_node = second_node.next
            count += 1
            
        answer_num = first + second
        
        # answer_num -> answer_listNode
        temp = answer_num % 10
        answer_listNode = ListNode(temp)
        
        
