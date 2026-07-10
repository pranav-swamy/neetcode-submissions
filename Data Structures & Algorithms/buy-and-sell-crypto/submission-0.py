class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_val = prices[0]
        max_profit = 0

        # keep track of min_val in an iteration
        # always subtract current val with min_val and caluclate the max profit
        for i in range(1, len(prices)):
            max_profit = max(prices[i] - min_val, max_profit)
            min_val = min(min_val, prices[i])
        
        return max_profit



        