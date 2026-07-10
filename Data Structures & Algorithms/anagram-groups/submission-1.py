class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map_anag = {}
        for word in strs:
            sig = self.create_sig(word)
            if sig not in map_anag:
                map_anag[sig] = []
            map_anag[sig].append(word)
        
        return list(map_anag.values())



    
    def create_sig(self, word):
        sig = [0]*26
        for ch in word:
            sig[ord(ch) - ord('a')] += 1

        return tuple(sig)
    
    # def comp_anag(self, list1, list2):
    #     for i in range(len(list1)):
    #         if list1[i] != list2[i]:
    #             return False
        
    #     return True