class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # backtracking algorithm
        # at every node, 1) choose
        # 2) explore all next choices recursively
        # 3) unchoose

        soln = []
        current = []

        def backtrack(start):
            soln.append(current[:])

            for i in range(start, len(nums)):
                current.append(nums[i])
                backtrack(i+1)
                current.pop()
        
        backtrack(0)
        return soln

