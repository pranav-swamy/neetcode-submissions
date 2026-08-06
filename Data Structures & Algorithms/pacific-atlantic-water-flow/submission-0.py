class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # add all border cells that are touching the pacific to a pacific set
        # add all border cells that are touching the atlantic to an atlantic set
        # start doing a dfs for each cell from these cells and move inward when the next val >= val.
        # collect all cells in a pacific_total and atlantic_total set
        # intersect these two sets to find the answer

        d = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        pacific = set()
        for x in range(len(heights)):
            pacific.add((x, 0))
        for y in range(len(heights[0])):
            pacific.add((0, y))

        atlantic = set()
        for x in range(len(heights)):
            atlantic.add((x, len(heights[0]) - 1))
        for y in range(len(heights[0])):
            atlantic.add((len(heights) - 1, y))

        def is_valid(x, y):
            within_bounds = 0 <= x < len(heights) and 0 <= y < len(heights[0])
            if not within_bounds:
                return False
            return True
            
        def dfs(x, y, _set):
            # add to set
            _set.add((x, y))

            for dx, dy in d:
                newx = x + dx
                newy = y + dy
                if is_valid(newx, newy) and heights[x][y] <= heights[newx][newy] and (newx, newy) not in _set:
                    dfs(newx, newy, _set)

        
        atlantic_set = set()
        # dfs from atlantic
        for x, y in atlantic:
            dfs(x, y, atlantic_set)
        
        pacific_set = set()
        for x, y in pacific:
            dfs(x, y, pacific_set)
        
        print(pacific_set)
        print(atlantic_set)
        result = pacific_set.intersection(atlantic_set)
        return [[x, y] for x,y in result]
