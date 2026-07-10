class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[right]: # still in left mountain
                left = mid + 1
            else:
                right = mid
        
        return nums[left] # left and right meet at the valley