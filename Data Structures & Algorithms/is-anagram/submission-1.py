class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        arr_s = [0]*26
        arr_t = [0]*26

        for ch in s:
            arr_s[ord(ch) - ord('a')] += 1
        
        for ch in t:
            arr_t[ord(ch) - ord('a')] += 1
        
        for i in range(len(arr_s)):
            if arr_s[i] != arr_t[i]:
                return False
        return True