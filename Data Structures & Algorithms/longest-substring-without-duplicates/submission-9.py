class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        pos = {}
        # pos contains the last known latest position of char pos[char]
        maxsize = 0
        l = 0

        for r in range(len(s)):
            if s[r] in pos:
                l = max(pos[s[r]] + 1, l)
            # update pos all the time since it has to contain the latest position of char x.
            pos[s[r]] = r
            maxsize = max(maxsize, r-l+1)
        
        return maxsize


        
