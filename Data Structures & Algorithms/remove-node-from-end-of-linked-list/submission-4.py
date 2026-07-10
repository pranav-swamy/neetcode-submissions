# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # recursion - keep track of number during call unwind
        # iterative way - calculate len - n and then unchain the link

        dummy = ListNode()
        dummy.next = head

        self.recurse(dummy, n)

        return dummy.next
    
    def recurse(self, head, n):
        if head.next is None:
            return 1
        
        count = self.recurse(head.next, n)
        
        # inc count for current node
        count += 1
        
        if count == n+1:
            head.next = head.next.next

        return count

