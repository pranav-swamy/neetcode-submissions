class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # bottom up approach
        # dp[i] = is s[0:i] splittable into words?
        # dp[0] = True
        # dp[i] is splittable if there exists a 1 < j < i where dp[j] is splittable and s[j:i] is a word in word dict => hence the whole of s[0:i] i splittable

        words = set(wordDict)
        dp = [False]*(len(s)+1)
        dp[0] = True

        for i in range(1, len(s)+1):
            for j in range(0, i):
                prefix = s[j:i]
                if dp[j] == True and prefix in words:
                    # valid split found!
                    dp[i] = True
                    break # break since any one valid split is fine
        return dp[-1]
