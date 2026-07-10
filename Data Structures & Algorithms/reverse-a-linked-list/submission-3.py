# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # iterative way
        # need 3 pointers = prev, cur, next

        prev = None
        cur = head
        new_head = None

        if not head:
            return None

        while cur.next:
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node
        
        cur.next = prev
        return cur
            