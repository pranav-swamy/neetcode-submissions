class Solution:
    def climbStairs(self, n: int) -> int:
        # numways to climb step i
        # = numways to clinb step i-1
        # + numways to climb step i-2


        dp = [0]*(n+1)
        dp[0] = 1
        dp[1] = 1

        for i in range(2, len(dp)):
            dp[i] = dp[i-1] + dp[i-2]
        
        return dp[n]