class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        maxArea = 0
        d = [(-1, 0), (0, -1), (1, 0), (0, 1)]


        def is_valid(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])

        def dfs(row, col):
            # mark as visited
            grid[row][col] = 0

            islands = 0
            for dx, dy in d:
                newr = row + dx
                newc = col + dy
                if is_valid(newr, newc) and grid[newr][newc] == 1:
                    islands += dfs(newr, newc)
            
            return 1 + islands
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    maxArea = max(maxArea, dfs(row, col))
        
        return maxArea