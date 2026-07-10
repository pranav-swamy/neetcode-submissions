class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # sliding window way
        # keep track of l and r
        # if s[r] is already seen, move l right until the char is out of the window
        # keep trak of max size at every step

        l = 0
        r = 0
        charset = set()
        maxsize = 0

        while r < len(s):
            if s[r] in charset:
                while l < r and s[l] != s[r]:
                    charset.remove(s[l])
                    l += 1
                if s[l] == s[r]:
                    charset.remove(s[l])
                    l += 1
            
            charset.add(s[r])
            maxsize = max(r-l+1, maxsize)
            # inc r
            r += 1
        
        return maxsize
