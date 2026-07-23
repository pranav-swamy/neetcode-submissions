class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # keep a visited array and 
        # iterate through every single number
        # at every recusion level/depth, marking the ones
        # visited as true and then unmarking them to backtrack
        # this will permute through the numbers

        soln = []
        visited = [False]*len(nums)
        cur = []

        def backtrack():
            if len(cur) == len(nums):
                soln.append(cur[:])
                return
                
            for i in range(len(nums)):
                if not visited[i]:
                    visited[i] = True
                    cur.append(nums[i])
                    backtrack()
                    cur.pop()
                    visited[i] = False
        
        backtrack()
        return soln





            
