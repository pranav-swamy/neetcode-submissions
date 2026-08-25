class Solution:
    def longestPalindrome(self, s: str) -> str:
        ispali = [[False]*len(s) for _ in range(len(s))]
        maxs = s[0] if s else ""
        maxlen = 1 if s else 0

        for i in range(len(s)):
            ispali[i][i] = True
        
        for i in range(len(s)-2, -1, -1):
            for j in range(i, len(s)):
                if j - i + 1 <= 2 and s[i] == s[j]:
                    ispali[i][j] = True
                else:
                    ispali[i][j] = ispali[i+1][j-1] and s[i] == s[j]
                
                if j - i + 1 > maxlen and ispali[i][j]:
                    maxlen = j - i + 1
                    maxs = s[i:j+1]
        
        return maxs

        



