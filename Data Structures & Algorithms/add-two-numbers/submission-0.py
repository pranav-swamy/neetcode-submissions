# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        cur = res
        carry = 0

        while l1 and l2:
            _sum = l1.val + l2.val + carry
            if _sum >= 10:
                carry = 1
            else:
                carry = 0
            
            node = ListNode(_sum % 10)
            cur.next = node
            cur = cur.next
            l1 = l1.next
            l2 = l2.next
        
        while l1:
            _sum = l1.val + carry
            if _sum >= 10:
                carry = 1
            else:
                carry = 0
            
            node = ListNode(_sum % 10)
            cur.next = node
            cur = cur.next
            l1 = l1.next
        
        while l2:
            _sum = l2.val + carry
            if _sum >= 10:
                carry = 1
            else:
                carry = 0
            
            node = ListNode(_sum % 10)
            cur.next = node
            cur = cur.next
            l2 = l2.next
        
        if carry == 1:
            node = ListNode(1)
            cur.next = node

        return res.next


        
        




