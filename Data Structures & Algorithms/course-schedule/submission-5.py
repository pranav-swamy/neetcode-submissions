class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        adj = dict()
        for n in range(numCourses):
            adj[n] = []

        for p, q in prerequisites:
            adj[q].append(p)
        
        def dfs(node, path):
            path.add(node)

            for neighbor in adj[node]:
                if neighbor in path:
                    return False
                if not dfs(neighbor, path):
                    return False
            
            path.remove(node)

            adj[node] = []
            return True
        
        for i in range(numCourses):
            if not dfs(i, set()):
                return False
        
        return True
        