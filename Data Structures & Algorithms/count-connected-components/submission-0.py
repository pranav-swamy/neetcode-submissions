class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # dfs from a node:
        # mark all visited nodes as visited and inc count
        # next, do dfs from a node that has not been visited, inc count
        # return total numbner of connected components

        visited = set()
        adj_list = dict()
        for i in range(n):
            adj_list[i] = []
        for e in edges:
            adj_list[e[1]].append(e[0])
            adj_list[e[0]].append(e[1])

        def dfs(node):
            visited.add(node)
            for neighbor in adj_list[node]:
                if neighbor not in visited:
                    dfs(neighbor)
        
        count = 0
        for node in range(n):
            if node not in visited:
                count += 1
                dfs(node)

        return count