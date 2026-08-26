class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # calculate max ending at an index i
        # min ending at an index i
        # candidates = max(nums[i], max ending at nums[i], min ending at nums[i])
        
        max_product = nums[0]
        max_so_far = nums[0]
        min_so_far = nums[0]

        for i in range(1, len(nums)):
            candidates = (nums[i], max_so_far*nums[i], min_so_far*nums[i])
            # to calc new max_so_far and new min_so_far, compare against current nums[i], and the new products.
            max_so_far = max(candidates)
            min_so_far = min(candidates)

            max_product = max(max_so_far, max_product)
        
        return max_product