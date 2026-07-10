class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        soln = []
        current = []

        def backtrack(start, cur_sum):
            if cur_sum == target:
                soln.append(current[:])
            elif cur_sum > target:
                return
            
            for i in range(start, len(nums)):
                current.append(nums[i])
                backtrack(i, cur_sum+nums[i])
                current.pop()
        
        backtrack(0, 0)
        return soln