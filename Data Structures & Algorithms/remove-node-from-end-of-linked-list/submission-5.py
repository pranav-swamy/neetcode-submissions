# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # recursion - keep track of number during call unwind
        # iterative way - calculate len - n and then unchain the link
        # 2-ptr approach - n nodes away from each other, reach the end, and you get the node to remove

        dummy = ListNode()
        dummy.next = head

        count = n
        p1 = dummy
        p2 = dummy
        while count > 0:
            p2 = p2.next
            count -= 1
        # now, p1 nad p2 are n distance apart

        while p2.next is not None:
            p1 = p1.next
            p2 = p2.next
        
        # now p1's next node needs to be removed
        p1.next = p1.next.next
        
        return dummy.next



