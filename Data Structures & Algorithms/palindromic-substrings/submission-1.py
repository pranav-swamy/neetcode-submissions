class Solution:
    def countSubstrings(self, s: str) -> int:
        # pointer approach (not dp)

        count = 0

        # 1 ptr - odd length
        for i in range(len(s)):
            l = r = i

            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    count += 1
                    l -= 1
                    r += 1
                else:
                    break
        
        # 2 ptr - even length
        for i in range(len(s)-1):
            l = i
            r = i+1
            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    count += 1
                    l -= 1
                    r += 1
                else:
                    break
        
        return count