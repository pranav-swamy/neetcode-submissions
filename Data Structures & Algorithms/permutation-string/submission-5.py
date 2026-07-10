class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # fixed window of size len(s1)
        # calculate signature using [0]*26 and populate counts
        # slide the window over s2 and find if a permutation exists

        if len(s1) > len(s2):
            return False
        
        s1_sig = [0]*26
        for ch in s1:
            s1_sig[ord(ch) - ord('a')] += 1
        
        s2_sig = [0]*26
        for i in range(len(s1)):
            s2_sig[ord(s2[i]) - ord('a')] += 1
        
        l = 0
        r = len(s1)-1

        while r < len(s2):
            if self.isPerm(s1_sig, s2_sig):
                return True
            
            s2_sig[ord(s2[l]) - ord('a')] -= 1
            l += 1
            r += 1
            # if r >= len(s2):
            #     return False
            if r < len(s2):
                s2_sig[ord(s2[r]) - ord('a')] += 1
        
        return False
    
    def isPerm(self, s1_sig, s2_sig):
        for i in range(len(s2_sig)):
            if s1_sig[i] != s2_sig[i]:
                return False
            
        return True