class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # kahn's algorithm (bfs)
        # keep collecting nodes that have 0 indegree

        indeg = dict()
        adj_list = dict()
        for i in range(numCourses):
            indeg[i] = set()
            adj_list[i] = list()
        for p in prerequisites:
            indeg[p[0]].add(p[1])
            adj_list[p[1]].append(p[0])
        
        res = []
        queue = []
        for node in indeg:
            if len(indeg[node]) == 0:
                queue.append(node)
                res.append(node)
        
        # start bfs
        while queue:
            children = []
            for node in queue:
                # remove edges - process prereqs
                for neighbor in adj_list[node]:
                    indeg[neighbor].remove(node)
                    if len(indeg[neighbor]) == 0:
                        children.append(neighbor)
                        res.append(neighbor)
            queue = children
        
        return res if len(res) == numCourses else []
        


