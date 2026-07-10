class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = {}
        for num in nums:
            if num not in freq_map:
                freq_map[num] = 0
            freq_map[num] += 1

        # bucket sort
        buckets = [[] for _ in range(len(nums)+1)]

        for num in freq_map:
            # print(freq_map[num])
            buckets[freq_map[num]].append(num)
        
        res = []
        for i in range(len(buckets)-1, -1, -1):
            if buckets[i]:
                for n in buckets[i]:
                    res.append(n)
                    if len(res) == k:
                        return res
        return res
