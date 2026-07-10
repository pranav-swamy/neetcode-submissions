class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []

        # sort arr
        # fix i,
        # use two pointer approach to get j and k

        nums.sort()

        for i in range(0, len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]: # skip same values of i
                continue
            
            j = i+1
            k = len(nums)-1

            while j < k:
                cur_sum = nums[i] + nums[j] + nums[k]
                if cur_sum == 0:
                    res.append([nums[i], nums[j], nums[k]])
                    while j < k and nums[j+1] == nums[j]:
                        j += 1
                    j += 1 # move to the next non-dup val
                    while j < k and nums[k-1] == nums[k]:
                        k -= 1
                    k -= 1 # move to the next non-dup val
                elif cur_sum < 0: # total val should be increased, so increase j
                    j += 1
                elif cur_sum > 0: # total val should be decreased, so decrease j
                    k -= 1
        
        return res
