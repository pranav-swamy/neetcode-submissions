class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # optimized version by sending cur_sum

        soln = []
        cur = []

        def backtrack(start, cur_sum):
            if cur_sum == target:
                soln.append(cur[:])
                return
            elif cur_sum > target:
                return
            
            for i in range(start, len(nums)):
                cur.append(nums[i])
                backtrack(i, cur_sum + nums[i])
                cur.pop()
            
        backtrack(0, 0)
        return soln