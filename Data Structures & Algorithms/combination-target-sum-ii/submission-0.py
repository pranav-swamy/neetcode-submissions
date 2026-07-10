from collections import Counter
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        current = []
        soln = []

        # sort so that you can skip duplicates
        candidates.sort()

        can_map = Counter(candidates)

        def backtrack(start, cur_sum):
            
            if cur_sum == target:
                soln.append(current[:])
                return
            elif cur_sum > target or start == len(candidates):
                return
            
            for i in range(start, len(candidates)):
                if i > start and candidates[i-1] == candidates[i]:
                    continue
                
                # choose
                current.append(candidates[i])
                #explore
                backtrack(i+1, cur_sum + candidates[i])
                #unchoose
                current.pop()
                
            
        backtrack(0, 0)
        return soln
