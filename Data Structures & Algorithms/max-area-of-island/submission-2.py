class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # dfs from a cell that is a 1 and has not been visited yet
        # return the total area so far

        maxArea = 0
        d = [(-1, 0), (0, -1), (1, 0), (0, 1)]

        def is_valid(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0]) and grid[row][col] == 1

        def dfs(row, col):

            area = 1
            grid[row][col] = 0

            for dx, dy in d:
                if is_valid(row+dx, col+dy):
                    area += dfs(row+dx, col+dy)
            
            return area
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    maxArea = max(maxArea, dfs(i, j))
        
        return maxArea
