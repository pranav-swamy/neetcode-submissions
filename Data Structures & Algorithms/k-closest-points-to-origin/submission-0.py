import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # max heap of size k
        # put distance and coordinates in a tuple
        # keep pushing and popping and maintain heap of size k
        # return final heap

        heap = []
        for point in points:
            heapq.heappush(heap, (-math.sqrt(point[0]**2 + point[1]**2), point))
            if len(heap) > k:
                heapq.heappop(heap)

        return [point[1] for point in heap]


