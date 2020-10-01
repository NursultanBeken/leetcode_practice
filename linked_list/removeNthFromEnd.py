# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
Two pointers solution
Maintain two pointers and update one with a delay of n steps.
"""
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        
        dummy = ListNode(0);
        dummy.next = head
        
        p1, p2 = dummy, dummy
        
         
        for _ in range(n+1):
            p2 = p2.next
        
        while p2:
            p1 = p1.next
            p2 = p2.next
            
        p1.next = p1.next.next
        
        return dummy.next
        
        
        