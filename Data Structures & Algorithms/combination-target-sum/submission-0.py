class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        soln = []
        current = []

        def backtrack(start):
            cur_sum = sum(current)
            if cur_sum == target:
                soln.append(current[:])
            elif cur_sum > target:
                return

            # recursively walk the tree (dfs) (next choices)
            for i in range(start, len(nums)):
                # choose
                current.append(nums[i])
                # backtrack
                backtrack(i)
                # unchoose
                current.pop()
        
        backtrack(0)
        return soln
            