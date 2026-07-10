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
                i += 1
                continue
            
            j = i+1
            k = len(nums)-1

            while j < k:
                three_sum = nums[i] + nums[j] + nums[k]
                if three_sum == 0:
                    res.append([nums[i], nums[j], nums[k]])
                    j = self.incr_ptr(nums, j)
                    k = self.decr_ptr(nums, k)
                elif three_sum < 0:
                    j = self.incr_ptr(nums, j)
                else:
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



            

        