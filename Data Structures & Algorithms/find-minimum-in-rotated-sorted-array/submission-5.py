class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        
        3, 4, 5, 6, 1, 2

        find minimum
        left hill, right hill, find valley

        find mid
        if mid is on left hill, move right
        if mid is on right hill, move left
        when left == right, thats the min

        """

        left = 0
        right = len(nums)-1

        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                # on left hill
                left = mid + 1
            else:
                right = mid
        
        return nums[right]
        