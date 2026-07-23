class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # same approach
        # but there is a condition for collection of answers
        # and they can be repeated

        soln = []
        cur = []

        def backtrack(start):
            _sum = sum(cur)
            if _sum == target:
                soln.append(cur[:])
                return
            if _sum > target:
                return
            
            for i in range(start, len(nums)):
                cur.append(nums[i])
                backtrack(i)
                cur.pop()
        
        backtrack(0)
        return soln