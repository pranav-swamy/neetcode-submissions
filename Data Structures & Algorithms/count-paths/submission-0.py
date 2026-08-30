class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # numways[i][j] = numways[i+1][j] + numways[i][j+1]

        # fill bottom up, right to left

        dp = [[0]*n for i in range(m)]

        dp[m-1][n-1] = 1 # 1 way to get there - already there

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if i+1 == m and j+1 == n:
                    continue
                
                if i+1 == m:
                    dp[i][j] = dp[i][j+1]
                elif j+1 == n:
                    dp[i][j] = dp[i+1][j]
                else:
                    dp[i][j] = dp[i+1][j] + dp[i][j+1]

        return dp[0][0]
