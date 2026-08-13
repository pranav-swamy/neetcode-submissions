class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # use union find algorithm
        # bare-bones version - no optimizations
        # to understand the approach

        # process each edge one at a time
        # when adding the edge, see if both the nodes
        # are already in the same connected component
        # by looking at their parent (a nominated node for the group)
        # if they are not, then this is a valid edge
        # if they are - then this is an edge that causes a cycle

        num_nodes = len(edges) # as there is exactly 1 extra edge - given in the problem statement
        parent = [i for i in range(num_nodes+1)] # 1-indexed

        def find_parent(node):
            while parent[node] != node:
                node = parent[node]
            return node
        
        # start adding edges one by one
        for u,v in edges:
            # find parent for u
            u_parent = find_parent(u)
            # find parent for v
            v_parent = find_parent(v)

            if u_parent == v_parent:
                # these nodes are already in the same connected component
                # this is the edge that will cause a cycle
                return [u,v]
            
            # else, connect these 2 components
            parent[u_parent] = v_parent
        
        return []
