class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # same as subsets 1, 
        # but at the same recursion level
        # skip the similar subsets

        soln = []
        nums.sort()
        cur = []

        def backtrack(start):
            soln.append(cur[:])

            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue
                cur.append(nums[i])
                backtrack(i+1)
                cur.pop()
        
        backtrack(0)
        return soln