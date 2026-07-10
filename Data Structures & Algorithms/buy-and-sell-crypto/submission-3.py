class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # left = 0
        # right = 0
        # increase right to go to next val if it is greater, record max profit
        # if the right val is same or lesser than starting day, move left and right to that point
        # start again
        # if it is not less than the starting point but is < the previous value, keep going

        #i.e, you only reset the window id you find a smaller selling price

        left = 0
        right = 0

        max_price = 0
        while right < len(prices)-1:
            if prices[right+1] < prices[left]:
                left = right+1
                right = right+1
            else:
                right += 1
                max_price = max(max_price, prices[right] - prices[left])
        
        return max_price