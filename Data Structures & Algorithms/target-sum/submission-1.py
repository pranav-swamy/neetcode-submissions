class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        memo = {}
        def dfs(index, runningsum):
            if index == len(nums):
                if runningsum == target:
                    return 1
                else:
                    return 0
            if (index, runningsum) in memo:
                return memo[(index, runningsum)]
            
            add = dfs(index+1, runningsum + nums[index])
            sub = dfs(index+1, runningsum - nums[index])
            numways = add + sub
            memo[(index, runningsum)] = numways
            return numways

        return dfs(0, 0)