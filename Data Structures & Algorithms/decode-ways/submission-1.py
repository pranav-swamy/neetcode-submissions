class Solution:
    def numDecodings(self, s: str) -> int:
        
        # s[i] = s[i+1] or s[i+2]?
        
        memo = dict()
        #count = 0

        def dfs(index):
            #nonlocal count
            if index == len(s):
                return 1
            if s[index] == '0':
                return 0
            
            if index in memo:
                return memo[index]
            
            count = 0
            if 1 <= int(s[index]) <= 9:
                count += dfs(index+1)
            
            if index+1 < len(s) and 10 <= int(s[index:index+2]) <= 26:
                count += dfs(index+2)
            
            memo[index] = count
            return count

        
        return dfs(0)