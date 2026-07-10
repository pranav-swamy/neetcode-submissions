class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # left_arr = product of all elts to the left of that pos
        # right_arr = product of all elts to the right of that pos

        left_arr = [1]*len(nums)
        right_arr = [1]*len(nums)

        
        for i in range(1, len(nums)):
            left_arr[i] = left_arr[i-1] * nums[i-1]


        for i in range(len(nums)-2, -1, -1):
            right_arr[i] = right_arr[i+1] * nums[i+1]
        
        res = [left_arr[i] * right_arr[i] for i in range(len(nums))]
        return res
