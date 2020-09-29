# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        
        curr = head
        item_set = set()
        
        while curr != None:
            if curr not in item_set:
                item_set.add(curr)
                curr = curr.next
            else:
                return True
        return False   