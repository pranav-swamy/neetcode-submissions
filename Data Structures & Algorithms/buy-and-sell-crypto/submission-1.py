class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 2 ptr approach
        # l, r -> move r and subtract with l to find max profit
        # if l > r, move l to r

        l, r = 0, 1
        max_p = 0

        while r < len(prices):
            profit = prices[r] - prices[l]
            max_p = max(max_p, profit)
            if prices[l] > prices[r]:
                l = r
            r += 1
        
        return max_p




        