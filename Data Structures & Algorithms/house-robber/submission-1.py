class Solution:
    def rob(self, nums: List[int]) -> int:
        # max money upto house n
        # = max(max money upto house n-2 + n, max money upto house n-1)

        if not nums:
            return 0
        if len(nums) == 1:
            return nums[-1]

        maxmoney = [0]*len(nums)

        maxmoney[0] = nums[0]
        maxmoney[1] = max(nums[0], nums[1])
        
        for i in range(2, len(nums)):
            maxmoney[i] = max(maxmoney[i-2] + nums[i], maxmoney[i-1])
        
        return maxmoney[-1]