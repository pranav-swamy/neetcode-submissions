# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # two pointer approach
        # keep pointers n apart
        # move them to the end
        # then you have ptr1 at the node to be removed

        ptr2 = head
        while n:
            ptr2 = ptr2.next
            n -= 1
        
        # keep n+1 distance now so that 
        # when you move both ptrs, ptr1 stops right before 
        # the node to be removed.

        dummy = ListNode()
        dummy.next = head
        ptr1 = dummy
        while ptr2:
            ptr2 = ptr2.next
            ptr1 = ptr1.next
        
        ptr1.next = ptr1.next.next

        return dummy.next


