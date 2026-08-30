class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # dp[i][j] = length of longest common subsequence considering text1 of length i and text2 of length j
        dp = [[0]*(len(text2)+1) for _ in range(len(text1)+1)]

        # dp[0][j] = 0
        # dp[i][0] = 0
        # there cannot be a subsequence when one string is empty

        for i in range(len(dp)):
            for j in range(len(dp[0])):
                if i == 0 or j == 0:
                    dp[i][j] = 0
                elif text1[i-1] == text2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        return dp[-1][-1]

