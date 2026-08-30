class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # recursive approach
        # on each day, we can either do nothing
        # or buy
        # or sell

        memo = {}

        def dfs(i, buying):
            if i >= len(prices):
                return 0
            
            if (i, buying) in memo:
                return memo[(i, buying)]
            
            cooldown = dfs(i+1, buying)
            if buying:
                amount = dfs(i+1, False) - prices[i]
                memo[(i, buying)] = max(cooldown, amount)
                return max(cooldown, amount)
            else:
                amount = dfs(i+2, True) + prices[i]
                memo[(i, buying)] = max(cooldown, amount)
                return max(cooldown, amount)
            
        
        return dfs(0, True)
