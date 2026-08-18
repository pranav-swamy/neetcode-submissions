class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        total = [0]*(len(cost)+1)

        # total_cost(ith step) = min(total_cost(i-1th step) + cost(i), total_cost(i-2 step) + cost(i-2))

        total[0] = 0
        total[1] = 0
        
        for i in range(2, len(total)):
            total[i] = min(total[i-1] + cost[i-1], total[i-2] + cost[i-2])
        
        return total[-1]

