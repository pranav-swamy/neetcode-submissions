"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # keep a mapping of old node -> new node
        # when you encounter a new number, create a new node
        # dfs approach

        visited = dict()

        if not node:
            return None

        def dfs(n):
            if n in visited:
                return visited[n]
                
            visited[n] = Node(n.val, [])
            
            for neighbor in n.neighbors:
                visited[n].neighbors.append(dfs(neighbor))
            
            return visited[n]
        
        return dfs(node)