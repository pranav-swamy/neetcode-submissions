class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # dfs from a node
        # make sure that in a path, there is no cycle
        # to check for cycle - a node should be there in the path that is not the parent.
        # and one dfs run should reach all nodes

        adj_list = dict()
        for i in range(n):
            adj_list[i] = []
        
        for e1, e2 in edges:
            adj_list[e1].append(e2)
            adj_list[e2].append(e1)
        visited = set()
        def dfs(node, path, parent):
            visited.add(node)
            path.add(node)

            for neighbor in adj_list[node]:
                if neighbor == parent:
                    continue
                if neighbor in path:
                    return False
                
                path.add(neighbor)
                if not dfs(neighbor, path, node):
                    return False
                path.remove(neighbor)
            
            return True
        
        if not dfs(0, set(), None):
            return False

        if len(visited) == n:
            return True
        else:
            return False
