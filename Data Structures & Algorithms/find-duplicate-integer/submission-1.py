class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        for i in range(0, len(nums)):

            idx_position = abs(nums[i])-1
            if nums[idx_position] < 0:
                # that is the duplicate
                return abs(nums[i])
            else:
                nums[idx_position] *= -1


