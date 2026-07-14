class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # sort first
        # [1, 1, 2]
        # skip same elements at the same level of recursion

        soln = []
        subset = []
        nums.sort()

        def backtrack(start):
            soln.append(subset[:])

            for i in range(start, len(nums)):
                if i > start and nums[i-1] == nums[i]:
                    continue
                subset.append(nums[i])
                backtrack(i+1)
                subset.pop()
        
        backtrack(0)
        
        return soln
        
        