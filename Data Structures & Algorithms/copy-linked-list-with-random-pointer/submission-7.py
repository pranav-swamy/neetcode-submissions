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
        nodemap = dict()

        if not head:
            return None

        cur = head

        while cur:
            if cur not in nodemap:
                nodemap[cur] = Node(cur.val)
            cur = cur.next
        
        cur = head
        while cur:
            if cur.next:
                nodemap[cur].next = nodemap[cur.next]
            if cur.random:
                nodemap[cur].random = nodemap[cur.random]
            cur = cur.next
        
        return nodemap[head]

