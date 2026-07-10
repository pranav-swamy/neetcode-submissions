# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # recursion - keep track of number during call unwind
        # iterative way - calculate len - n and then unchain the link

        count = 0
        cur = head
        while cur is not None:
            count += 1
            cur = cur.next
        
        remove_idx = count - n

        if remove_idx == 0:
            return head.next

        cur = head
        i = 0
        while cur:
            if i == remove_idx-1:
                cur.next = cur.next.next # unlink the next node
                break
            cur = cur.next
            i += 1
        
        return head

