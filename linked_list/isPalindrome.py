# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        arr = []
        
        curr = head
        
        while curr is not None:
            arr.append(curr.val)
            curr = curr.next
        return arr == arr[::-1]    
            