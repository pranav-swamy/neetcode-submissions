class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        visited = [False]*len(nums)

        soln = []

        def backtrack(cur):
            if len(cur) == len(nums):
                soln.append(cur[:])

            for i in range(len(nums)):
                if not visited[i]:
                    visited[i] = True
                    cur.append(nums[i])
                    backtrack(cur)
                    cur.pop()
                    visited[i] = False
        
        backtrack([])
        return soln
