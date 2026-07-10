class Solution:
    def findMin(self, nums: List[int]) -> int:
        # l = 0, r = len(nums)-1
        # find mid 
        # anchor right elt because thta will tell whether to move left or right
        # if mid > r, move l to mid+1
        # if mid < r, move r = mid
        # key intuition to reduce search space - two hills and a valley
        # if on left hill, keep going right
        # if on right hill, kepp going left
        # stop in the valley

        l = 0
        r = len(nums) - 1

        while l < r:
            mid = l + (r-l)//2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        
        return nums[l]