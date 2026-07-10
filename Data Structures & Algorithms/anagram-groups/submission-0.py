class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq_map = {}

        for string in strs:
            freq_arr = [0]*26
            for ch in string:
                freq_arr[ord(ch) - ord('a')] += 1
            
            key = tuple(freq_arr)
            if key not in freq_map:
                freq_map[key] = []
            freq_map[key].append(string)
        
        return [x for x in freq_map.values()]