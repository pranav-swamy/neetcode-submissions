class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # array of [1,n]
        # for each val in arr, negate its corresponding position
        # when we encounter another same value and 
        # the position is already negated, it is the duplicate

        for i in range(0, len(nums)):
            val = nums[i]

            if nums[abs(val)-1] < 0:
                # this num already has been seen before
                return abs(val)

            nums[abs(val)-1] *= -1

