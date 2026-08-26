class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # t(n) = 1 + min(t(n-val) for each coin of value val)

        dp = [0]*(amount+1)

        # dp(n) = min coins needed to amount to n

        dp[0] = 0

        for i in range(1, amount+1):
            minval = float('inf')
            for val in coins:
                if i-val >= 0 and dp[i-val] != -1:
                    minval = min(minval, 1 + dp[i-val])
            
            if minval == float('inf'):
                dp[i] = -1 # not possible
            else:
                dp[i] = minval
        # print(dp)
        return dp[-1]
            
                    


