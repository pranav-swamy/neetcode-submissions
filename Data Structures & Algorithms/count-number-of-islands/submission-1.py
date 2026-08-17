class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        d = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        def is_valid(row, col):
            within_bounds = 0 <= row < len(grid) and 0 <= col < len(grid[0])
            
            return within_bounds and grid[row][col] == "1"

        def dfs(row, col):
            grid[row][col] = "0"

            for dx, dy in d:
                if is_valid(row+dx, col+dy):
                    dfs(row+dx, col+dy)

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    count += 1
                    dfs(i, j)
        
        return count
            
            


