class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = {}
        for num in nums:
            if num not in freq_map:
                freq_map[num] = 1
            freq_map[num] += 1

        # heap approach
        heap = []
        for num in freq_map:
            heapq.heappush(heap, (freq_map[num], num)) # min heap by default
            if len(heap) > k:
                # pop the top to remove the smallest elt
                heapq.heappop(heap)

        res = []
        for i in range(k):
            res.append(heap[i][1])
        return res