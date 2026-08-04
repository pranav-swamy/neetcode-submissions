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

        if not node:
            return None
            
        visited = dict()
        visited[node] = Node(node.val, [])

        queue = deque([node])

        while queue:
            cur = queue.popleft()
            for neighbor in cur.neighbors:
                if neighbor not in visited:
                    visited[neighbor] = Node(neighbor.val, [])
                    queue.append(neighbor)
                visited[cur].neighbors.append(visited[neighbor])
        
        return visited[node]

        