class Solution:
    def rob(self, nums: List[int]) -> int:
        # since the houses are arranged in a circle
        # you can either rob house 0, or n-1, but not both
        # max money by robbing house n-1 = 1 .. n-1
        # max money by robbing house 0 = 0 .. n-2
        # max money is max of both

        def max_money(arr):
            if not arr:
                return 0
            if len(arr) == 1:
                return arr[0]
                
            dp = [0]*len(arr)
            dp[0] = arr[0]
            dp[1] = max(arr[0], arr[1])
            for i in range(2, len(dp)):
                dp[i] = max(dp[i-2] + arr[i], dp[i-1])
            return dp[-1]
        
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]


        return max(max_money(nums[0:len(nums)-1]), max_money(nums[1:len(nums)]))
