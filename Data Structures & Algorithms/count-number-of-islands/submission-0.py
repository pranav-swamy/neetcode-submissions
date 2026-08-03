class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # dfs, mark 1's as visited 
        # iterate through the entire grid

        count = 0
        d = [(-1,0), (0, -1), (1, 0), (0,1)]

        def dfs(row, col):
            # mark as visited
            grid[row][col] = "0"
            
            for dx, dy in d:
                newr = row + dx
                newc = col + dy
                if 0 <= newr < len(grid) and 0 <= newc < len(grid[0]) and grid[newr][newc] == "1":
                    dfs(newr, newc)
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    count += 1
                    dfs(row, col)
        
        return count
            
            


