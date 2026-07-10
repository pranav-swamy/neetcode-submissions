class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # find mid
        # if mid == target, return mid
        # if mid is on left hill:
        #   compare nums[mid], target and nums[r]
        #   if nums[mid] < target:
        #       l = mid + 1
        #   else if target < nums[r]:
        #       l = mid + 1
        #   else:
        #       r = mid - 1
        # if mid is on right hill:
        #   if target > nums[r]:
        #       r = mid - 1
        #   elif nums[mid] < target:
        #       l = mid+1
        #   else:
        #        r = mid - 1
    
        l = 0
        r = len(nums)-1

        while l <= r:
            mid = l + (r-l)//2
            if nums[mid] == target:
                return mid
            
            if nums[mid] > nums[r]:
                if nums[mid] < target:
                    l = mid + 1
                elif nums[r] < target:
                    r = mid - 1
                else:
                    l = mid + 1
            
            else:
                if nums[mid] > target:
                    r = mid - 1
                elif nums[r] < target:
                    r = mid - 1
                else:
                    l = mid + 1
        
        return -1

