class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        #keep track of max so far, min so far
        max_so_far = nums[0]
        min_so_far = nums[0]
        max_p = nums[0]

        for i in range(1, len(nums)):
            candidates = (max_so_far*nums[i], min_so_far*nums[i], nums[i])
            max_so_far = max(candidates)
            min_so_far = min(candidates)
            max_p = max(max_p, max_so_far)
        
        return max_p