class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = []
        fresh = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append((i, j))
                if grid[i][j] == 1:
                    fresh += 1
        

        def is_valid(x, y):
            return 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] != 0 and grid[x][y] != 2

        time = 0
        d = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        # bfs
        while queue:
            children = []
            for x, y in queue:
                for dx, dy in d:
                    if is_valid(x+dx, y+dy):
                        grid[x+dx][y+dy] = 2
                        fresh -=1 
                        children.append((x+dx, y+dy))
            
            if children:
                time += 1
            queue = children
        
        return time if fresh == 0 else -1
        