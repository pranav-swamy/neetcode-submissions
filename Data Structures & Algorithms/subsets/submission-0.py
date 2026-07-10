class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # backtracking algorithm
        # at every node, 1) choose
        # 2) explore all next choices recursively
        # 3) unchoose

        current = []
        soln = []


        def backtrack(i):
            # collect answer
            soln.append(current[:])

            for ptr in range(i, len(nums)):
                # choose
                current.append(nums[ptr])

                # recursively go to next steps
                backtrack(ptr+1)

                # unchoose
                current.pop()
        
        backtrack(0)
        return soln

