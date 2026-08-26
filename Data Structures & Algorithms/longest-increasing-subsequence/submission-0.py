class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # recurrence relation:
        # dp[i] = length of longest subsequence ending at index i
        # note that it is not the longest subsequence for nums[:i] but the length of the longest subsequence 'ending' at index i.

        # dp[i] = 1 initially for all i since all nums are subsequences of length 1 ending at i
        # now, for any i, if there exists a j < i such that nums[j] < nums[i], then dp[i] = max(dp[i], dp[j] + 1).
        # in the end, return max(dp) since the subsequence could end anywhere

        dp = [1]*len(nums)

        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        return max(dp)
        