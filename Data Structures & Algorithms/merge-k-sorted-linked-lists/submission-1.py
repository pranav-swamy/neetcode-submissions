# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # merge 2 at a time?

        if not lists:
            return None
        
        while len(lists) != 1:
            list1 = lists.pop(0)
            list2 = lists.pop(0)
            lists.append(self.merge_ll_iter(list1, list2))
        
        return lists[0]


    def merge_ll_iter(self, list1, list2):
        res = ListNode()
        cur = res

        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next
        if list1:
            cur.next = list1
        if list2:
            cur.next = list2
        
        res = res.next
        return res

    
    def merge_ll(self, list1, list2):
        if not list1:
            return list2
        if not list2:
            return list1
        
        if list1.val < list2.val:
            list1.next = self.merge_ll(list1.next, list2)
            return list1
        else:
            list2.next = self.merge_ll(list1, list2.next)
            return list2
            