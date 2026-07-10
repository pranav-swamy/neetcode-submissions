# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode(-1)
        cur = res
        carry = 0

        while l1 and l2:
            _sum = (carry + l1.val + l2.val) % 10
            carry = (carry + l1.val + l2.val) // 10
            cur.next = ListNode(_sum)
            cur = cur.next
            l1 = l1.next
            l2 = l2.next
        
        while l1:
            _sum = (carry + l1.val) % 10
            carry = (carry + l1.val) // 10
            cur.next = ListNode(_sum)
            cur = cur.next
            l1 = l1.next
        
        while l2:
            _sum = (carry + l2.val) % 10
            carry = (carry + l2.val) // 10
            cur.next = ListNode(_sum)
            cur = cur.next
            l2 = l2.next

        if carry:
            cur.next = ListNode(1)
        
        return res.next
