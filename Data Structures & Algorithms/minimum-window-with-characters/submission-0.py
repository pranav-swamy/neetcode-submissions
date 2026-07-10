class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # keep increasing window until it becomes valid
        # once valid, keep descreasing window to find min possible size
        # if it becomes invalid, keep increasing window again?

        # how to check validity of a window? - keep track in a map?
        # keep 2 maps - one for t and one for the window, and compare the two to check validity

        tcount = defaultdict(int)
        for ch in t:
            tcount[ch] += 1

        wcount = defaultdict(int)
        l=0
        r=0
        res = ""
        min_length = float("inf")

        while r < len(s):
            wcount[s[r]] += 1
            while self.isWindowValid(wcount, tcount):
                # update if min window so far
                window_length = r - l + 1
                if window_length < min_length:
                    min_length = window_length
                    res = s[l:r+1]
                
                # start shrinking window to find min
                wcount[s[l]] -= 1
                l += 1
            
            r += 1
        
        return res


    def isWindowValid(self, wcount, tcount):
        for ch in tcount:
            if ch not in wcount or wcount[ch] < tcount[ch]:
                return False
        return True

