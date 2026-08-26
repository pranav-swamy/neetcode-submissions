class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        memo = dict()

        def dfs(remaining):
            if not remaining:
                return True
            
            if remaining in memo:
                return memo[remaining]
            
            for i in range(1, len(remaining)+1):
                split = remaining[:i]
                if split in words and dfs(remaining[i:]):
                    # found a valid word and the rest of the string is splittable
                    memo[remaining] = True
                    return True
            
            # didn't find any valid word
            memo[remaining] = False
            return False
        
        return dfs(s)

