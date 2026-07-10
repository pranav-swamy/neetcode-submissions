"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        cur = head

        #new_head = Node()
        nodemap = {}

        while cur:
            # create deep copy
            node = Node(cur.val)
            
            # add node to map
            nodemap[cur] = node
            
            # move to next node
            cur = cur.next
        
        cur = head
        while cur:
            # link all next ptrs
            nodemap[cur].next = nodemap[cur.next] if cur.next else None

            # link all random ptrs
            nodemap[cur].random = nodemap[cur.random] if cur.random else None

            cur = cur.next
        
        return nodemap[head] if head else None

