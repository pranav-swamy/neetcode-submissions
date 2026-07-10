class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_sig = [0]*26
        for ch in s1:
            s1_sig[ord(ch) - ord('a')] += 1
        
        s2_sig = [0]*26
        for ch in range(0, len(s1)):
            s2_sig[ord(s2[ch]) - ord('a')] += 1

        l = 0
        r = len(s1) - 1
        while r < len(s2):
            if self.sig_equals(s1_sig, s2_sig):
                return True
            else:
                s2_sig[ord(s2[l]) - ord('a')] -= 1
                l += 1
                
                r += 1
                if r < len(s2):
                    s2_sig[ord(s2[r]) - ord('a')] += 1
        
        #print([x for x in range(len(s1_sig)) if s1_sig[x] > 0 ])
        #print([x for x in range(len(s1_sig)) if s2_sig[x] > 0 ])
        
        return False

        
    
    def sig_equals(self, s1, s2):
        for i in range(26):
            if s1[i] != s2[i]:
                return False
        return True
        
