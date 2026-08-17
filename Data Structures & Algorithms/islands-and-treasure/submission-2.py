class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # multi source bfs from the treasure chests
        queue = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    queue.append((i, j))
        
        d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        def is_valid(x, y):
            return 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == 2**31 - 1

        # bfs
        while queue:
            children = []
            for x, y in queue:
                for dx, dy in d:
                    if is_valid(x+dx, y+dy):
                        grid[x+dx][y+dy] = grid[x][y] + 1
                        children.append((x+dx, y+dy))
            queue = children



                


