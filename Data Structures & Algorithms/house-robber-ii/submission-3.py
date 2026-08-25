class Solution:
    def rob(self, nums: List[int]) -> int:
        # since 0 and n-1 are connected,
        # we cannot rob both of them together.
        # therefore, 
        # max money made from robbing 0 - n-2: (n-1) excluded
        # max money made from robbing 1 - n-1: (0 excluded)

        def max_money(arr):
            dp = [0]*len(arr)
            dp[0] = arr[0]
            dp[1] = max(arr[0], arr[1])

            for i in range(2, len(arr)):
                dp[i] = max(dp[i-2] + arr[i], dp[i-1])
            
            return dp[-1]
        
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])

        # 0 - n-2
        res1 = max_money(nums[:len(nums)-1])

        # 1 - n-1
        res2 = max_money(nums[1:])

        return max(res1, res2)



