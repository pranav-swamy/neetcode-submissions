class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        perm = []
        visited = [False] * len(nums)

        def backtrack():
            if len(perm) == len(nums):
                result.append(perm[:])
                return

            for i in range(len(nums)):
                if not visited[i]:
                    # choose
                    visited[i] = True
                    perm.append(nums[i])

                    # explore
                    backtrack()

                    # un-choose
                    visited[i] = False
                    perm.pop()
        
        backtrack()
        return result



            
