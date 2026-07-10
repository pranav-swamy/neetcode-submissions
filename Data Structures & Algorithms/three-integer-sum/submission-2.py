class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort the array
        # then do a two pointer approach to collect the triplets
        # skip over the same numbers so that it prevents adding duplicate triplets.

        # sort the array
        nums = sorted(nums)

        # two ptr approach
        res = []
        
        i = 0
        while i < len(nums):
            if i-1 >= 0 and nums[i] == nums[i-1]:
                # skip if current i is the same as previous i
                i += 1
                continue
            
            j = i+1
            k = len(nums)-1
            # nums[i] + nums[j] + nums[k] = 0
            # nums[i] = - nums[j] - nums[k]
            # - nums[i] = nums[j] + nums[k]

            while j < k:
                left = nums[j] + nums[k]
                right = nums[i]
                if left == right*-1:
                    res.append([nums[i], nums[j], nums[k]])
                    j = self.incr_ptr(nums, j)
                    k = self.decr_ptr(nums, k)
                elif left < right*-1:
                    # increase j
                    j = self.incr_ptr(nums, j)
                elif left > right*-1:
                    # decrease k
                    k = self.decr_ptr(nums, k)

            # increment i
            i += 1

        return res
    
    def incr_ptr(self, nums, cur):
        new_ptr = cur 
        while new_ptr < len(nums) and nums[new_ptr] == nums[cur]:
            new_ptr += 1
        return new_ptr
    
    def decr_ptr(self, nums, cur):
        new_ptr = cur 
        while new_ptr >= 0 and nums[new_ptr] == nums[cur]:
            new_ptr -= 1
        return new_ptr



            

        