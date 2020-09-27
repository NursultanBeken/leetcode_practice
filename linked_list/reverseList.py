# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
While you are traversing the list, change the current node's
 next pointer to point to its previous element. Since a node does 
 not have reference to its previous node, you must store its previous element beforehand. 
 You also need another pointer to store the next node before changing the reference.
 Do not forget to return the new head reference at the end!
"""
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head
        
        while curr != None:
            next_tmp = curr.next
            curr.next = prev
            prev = curr
            curr = next_tmp
            
        return prev