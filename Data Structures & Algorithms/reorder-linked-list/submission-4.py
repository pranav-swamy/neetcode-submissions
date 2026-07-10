# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # split the ll into two
        # reverse the second half
        # merge alternatively

        # split the ll into two
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # sever list
        list2 =slow.next
        slow.next = None
        list1 = head

        # rev the 2nd half
        rev_list2 = self.rev(list2)

        # merge l1 and rev_list2
        self.mergell(list1, rev_list2)
    

    def rev(self, head):
        if not head or not head.next:
            return head
        
        new_head = self.rev(head.next)

        head.next.next = head
        head.next = None

        return new_head
    
    def mergell(self, list1, list2):
        # iterative
        head = ListNode()

        cur = head

        while list1 and list2:
            cur.next = list1
            list1 = list1.next
            cur = cur.next
            cur.next = list2
            list2 = list2.next
            cur = cur.next
        
        if list1:
            cur.next = list1
        
        if list2:
            cur.next = list2
        
        return head.next


