class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # recursive top down approach
        # at each coin i, either use the coin and subtract the amount
        # or don't use the coin.
        memo = {}

        def dfs(index, amount):
            if amount == 0:
                return 1
            if amount < 0 or index >= len(coins):
                return 0
            if (index, amount) in memo:
                return memo[(index, amount)]
            
            numways = 0
            use = dfs(index, amount - coins[index]) 
            dont_use = dfs(index+1, amount)
            numways = use + dont_use
            memo[(index, amount)] = numways
            return numways
        
        return dfs(0, amount)

        