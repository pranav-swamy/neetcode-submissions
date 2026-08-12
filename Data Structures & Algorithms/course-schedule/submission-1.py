class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = dict()
        for i in range(numCourses):
            graph[i] = []
        for prereq in prerequisites:
            graph[prereq[1]].append(prereq[0])
        
        # find if there is a cycle in this DAG
        # to find a cycle, we do a dfs on every node
        # and on every path, make sure that there is
        # no cycle. so, keep track of the path on every
        # dfs and check for a cycle by seeing if a node
        # already exists in the current path
        def dfs(node, path):
            
            for next_node in graph[node]:
                if next_node in path:
                    # cycle found
                    return False
                
                path.add(next_node)
                res = dfs(next_node, path)
                if not res:
                    return False # short-circuit
                path.remove(next_node)
            
            # node is safe if it reached here
            # so, I can remove all edges from this node - 
            # memoizing it so that it is not processed again
            graph[node] = []
            return True
        
        for i in range(numCourses):
            if not dfs(i, set()):
                return False
        
        return True

            

