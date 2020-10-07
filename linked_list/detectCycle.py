# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        curr = head
        
        visited = set()
        
        while curr:
            if curr not in visited:
                visited.add(curr)
                curr = curr.next
            else:
                return curr
        return None    
        