class Solution:
    def numDecodings(self, s: str) -> int:
        # given a number
        # "1012"
        # JAB
        # JL

        # t(n) = t(n-1) if 1 <= n-1 <= 9 + t(n-2) if 1 <= n-2,n-1 <= 26
        # dp(n) = num ways to decode s[0:n]
        
        dp = [0]*(len(s)+1)

        dp[0] = 1 

        for i in range(1, len(s)+1):
            if 1 <= int(s[i-1]) <= 9:
                dp[i] += dp[i-1]
            if i >= 2 and 10 <= int(s[i-2:i]) <= 26:
                dp[i] += dp[i-2]
        
        return dp[len(s)]
        


