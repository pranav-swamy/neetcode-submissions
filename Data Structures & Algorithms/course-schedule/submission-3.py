class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # given a dag, make sure that there is no cycle

        adj = dict()
        for n in range(numCourses):
            adj[n] = []

        for p, q in prerequisites:
            adj[q].append(p)
        

        def dfs(node, path):
            for child in adj[node]:
                if child in path:
                    return False
                path.add(child)
                if not dfs(child, path):
                    return False
                path.remove(child)
            
            adj[node] = [] 
            return True
        
        for i in range(numCourses):
            if not dfs(i, set()):
                return False
        
        return True