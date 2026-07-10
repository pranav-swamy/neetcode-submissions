class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # prefix and suffix array
        prefix_arr = []
        suffix_arr = []

        # prefix - product of all elts to the left of nums[i]
        # suffix - prod of all elts to the right of nums[i]

        product = 1
        for i in range(len(nums)):
            prefix_arr.append(product)
            product *= nums[i]
        
        product = 1
        for i in range(len(nums)-1, -1 ,-1):
            suffix_arr.insert(0, product)
            product *= nums[i]
        
        ans = [prefix_arr[i] * suffix_arr[i] for i in range(len(nums))]
        return ans;

        