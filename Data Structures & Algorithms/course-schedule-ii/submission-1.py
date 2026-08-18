class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = dict()
        indeg = [0]*numCourses

        for i in range(numCourses):
            adj[i] = []
        
        for p, q in prerequisites:
            adj[q].append(p)
            indeg[p] += 1
        
        # kahns algo - start from nodes with 0 indegree

        queue = []
        for i in range(numCourses):
            if indeg[i] == 0:
                queue.append(i)
        
        order = []
        while queue:
            children = []
            for node in queue:
                order.append(node)
                for neighbor in adj[node]:
                    indeg[neighbor] -= 1
                    if indeg[neighbor] == 0:
                        children.append(neighbor)
            queue = children
        
        return order if len(order) == numCourses else []

        




