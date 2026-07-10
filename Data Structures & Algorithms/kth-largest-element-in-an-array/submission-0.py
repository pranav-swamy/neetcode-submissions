import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # min heap of size k elts

        heap = []

        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)
        
        return heap[0]