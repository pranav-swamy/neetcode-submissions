class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = {}
        for num in nums:
            if num not in freq_map:
                freq_map[num] = 1
            freq_map[num] += 1
        
        # sorting approach
        arr = [(x, freq_map[x]) for x in freq_map]
        arr.sort(key=lambda x: -x[1])

        res = []
        for i in range(k):
            res.append(arr[i][0])
        return res