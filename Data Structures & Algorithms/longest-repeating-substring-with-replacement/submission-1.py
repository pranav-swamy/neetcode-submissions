class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # a valid window is one where 
        # the len(window) - # of chars that are not the most freq one <= k
        # therefore, keep track of 
        # maxfreq in a window, and character counts in every window
        # if a window becomes invalid, then shrink from left and adjust counts
        # keep track of max length whenever a window is valid

        fmap = defaultdict(int)
        max_freq = 0

        l=0
        r=0
        max_size = 0

        while r < len(s):
            fmap[s[r]] += 1
            max_freq = max(max_freq, fmap[s[r]])

            len_window = r - l + 1
            while len_window - max_freq > k:
                # shrink window
                # move l, change char counts in fmap
                fmap[s[l]] -= 1
                l += 1
                len_window = r - l + 1

                # change max_freq
                max_freq = max(fmap.values())

            
            max_size = max(max_size, len_window)

            r += 1
        
        return max_size




