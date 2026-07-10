import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # max heap
        heap = []
        for stone in stones:
            heapq.heappush(heap, -stone)
        
        while heap:
            if len(heap) == 1:
                return -heap[0]

            first_stone = heapq.heappop(heap)
            sec_stone = heapq.heappop(heap)
            diff = abs(first_stone) - abs(sec_stone)
            if diff > 0:
                heapq.heappush(heap, -diff)
        
        return 0

