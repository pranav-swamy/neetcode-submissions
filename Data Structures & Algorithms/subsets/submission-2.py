class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # backtracking
        # dfs approach, start collecting results at
        # every node since all nodes are valid answers
        
        soln = []
        cur = []

        def backtrack(start):
            if start == len(nums)+1:
                return
            
            soln.append(cur[:])

            for i in range(start, len(nums)):
                # at first level of recursion tree, only one elt is there in cur
                # in this for loop
                cur.append(nums[i])
                backtrack(i+1)
                cur.pop()
        
        backtrack(0)
        return soln
