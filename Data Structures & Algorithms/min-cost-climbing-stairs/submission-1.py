class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # dp[i] = the min cost to get up to step i

        # dp[i] = minimum of dp[i-2] + cost[i-2] or
        # dp[i-1] + cost[i-1]

        dp = [0]*(len(cost)+1)

        dp[0] = 0
        dp[1] = 0

        for i in range(2, len(dp)):
            dp[i] = min(dp[i-1] + cost[i-1], dp[i-2]+cost[i-2])
        
        return dp[-1]