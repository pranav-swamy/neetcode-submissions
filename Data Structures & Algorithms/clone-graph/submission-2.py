"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        clonedict = dict()

        def dfs(node):
            if not node:
                return

            if node not in clonedict:
                clonedict[node] = Node(node.val, [])
            else:
                return clonedict[node]
        
            for neighbor in node.neighbors:
                cloned_neighbor = dfs(neighbor)
                clonedict[node].neighbors.append(cloned_neighbor)
        
            return clonedict[node]
    
        return dfs(node)
    

