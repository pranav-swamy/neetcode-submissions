class Solution:
    def longestPalindrome(self, s: str) -> str:
        # a string s[i:j] is a palindrome if 
        # s[i+1:j-1] is a palindrome and s[i] == s[j]
        # s[i:i] are all palindromes
        # all length 2 are palindromes if they are the same letter

        if not s:
            return ""

        maxlen = 1
        maxs = s[0]
        ispali = [[False]*len(s) for _ in range(len(s))]

        for i in range(len(s)):
            ispali[i][i] = True
            if i+1 < len(s) and s[i] == s[i+1]:
                ispali[i][i+1] = True
                maxlen = 2
                maxs = s[i:i+2]
        
        for i in range(len(s)-1, -1, -1):
            for j in range(i+2, len(s)):
                if s[i] == s[j] and ispali[i+1][j-1]:
                    ispali[i][j] = True
                    if j - i + 1 > maxlen:
                        maxlen = j - i + 1
                        maxs = s[i:j+1]
        
        return maxs

                