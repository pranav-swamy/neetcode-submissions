class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # keep track of indexes of each char
        # if a repear=ting char is next, then
        # move left to next of the exisitng index where the value is
        # update the index with the new one
        # track length

        imap = {}

        l = 0
        r = 0
        maxlen = 0

        while r < len(s):
            # if found
            if s[r] in imap:
                new_l = imap[s[r]] + 1

                while l < new_l:
                    del imap[s[l]]
                    l += 1
                
            
            imap[s[r]] = r
            # track len
            maxlen = max(maxlen, r - l + 1)
            r += 1
        
        return maxlen