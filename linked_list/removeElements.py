class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        
        sentinel = ListNode(0)
        sentinel.next = head
        
        prev = sentinel
        curr = head
        while curr != None:
            if curr.val == val:     
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
            
        return sentinel.next 