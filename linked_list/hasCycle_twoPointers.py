# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        
        if head is None:
            return False  
        
        slow_pointer  = head
        fast_pointer = head.next
        
        while slow_pointer != fast_pointer:
            if fast_pointer is None or fast_pointer.next is None:
                return False
            else:
                slow_pointer = slow_pointer.next
                fast_pointer = fast_pointer.next.next
                
        return True        