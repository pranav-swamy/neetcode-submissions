class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # dfs from every node
        # keep track of the path, and parent node
        # if a node is hit that is in the path already 
        # and is not the parent, then a cycle is found
        # return false if a cycle is found

        adj_list = dict()
        count = 0 # count the no. of nodes visited
        for node in range(n):
            adj_list[node] = set()
        for e in edges:
            adj_list[e[0]].add(e[1])
            adj_list[e[1]].add(e[0])
        

        def dfs(node, parent, path):
            nonlocal count
            if node in path:
                # cycle found
                return False
            
            count += 1
            path.add(node)

            for neighbor in adj_list[node]:
                if neighbor != parent:
                    res = dfs(neighbor, node, path)
                    if not res:
                        return False # short-circuit
            
            path.remove(node)

            return True
        
        # only do dfs from one node, since if it is a connected graph, 
        # it will eventually reach ALL nodes and identify a cycle
        if not dfs(0, None, set()):
            return False
        
        return True if count == n else False
