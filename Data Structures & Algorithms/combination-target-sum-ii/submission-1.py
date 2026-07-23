from collections import Counter
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # same as combination sum
        # however, at the same recursion level
        # skip identical numbers!
        # when the sum reaches the target, collect the answer

        soln = []
        # sort candidates so it is easy to skip identical
        # numbers at the same recursion level
        candidates.sort()
        nums = candidates

        cur = []

        def backtrack(start, cur_sum):
            if cur_sum == target:
                soln.append(cur[:])
                return
            elif cur_sum > target:
                return
            
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue
                cur.append(nums[i])
                backtrack(i+1, cur_sum + nums[i])
                cur.pop()
        
        backtrack(0, 0)
        return soln

