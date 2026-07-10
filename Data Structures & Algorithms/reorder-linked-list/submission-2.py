# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        count = 0
        cur = head
        while cur:
            count += 1
            cur = cur.next
        
        half = 0
        if count % 2 == 0:
            half = (count // 2) - 1
        else:
            half = count // 2
        
        # print(half)

        list1 = head
        list2 = head
        count = 0
        while count < half:
            count += 1
            list2 = list2.next
        
        list2_real = list2.next
        list2.next = None
        
        # print(list1.val)
        # print(list2.val)
        
        # reverse list2
        # merge list1 and list2
        rev_list2 = self.reverse(list2_real)
        #print(rev_list2.val)
        self.merge(list1, rev_list2)
        
    
    def reverse(self, head):
        if head is None or head.next is None:
            return head
        
        new_head = self.reverse(head.next)

        head.next.next = head
        head.next = None
        return new_head
    
    def merge(self, list1, list2):
        if not list1:
            return list2
        if not list2:
            return list1
        
        next1 = list1.next
        next2 = list2.next

        list1.next = list2
        
        list2.next = self.merge(next1, next2)

        return list1


        