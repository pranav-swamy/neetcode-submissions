import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # use heap or bucket sort

        # heap method
        freq_map = defaultdict(int)
        for num in nums:
            freq_map[num] += 1
        
        heap = []
        for num in freq_map:
            # insert
            heapq.heappush(heap, (freq_map[num], num))

            # if len > k, pop push
            if len(heap) > k:
                heapq.heappop(heap)
            
        
        return [x[1] for x in heap]



