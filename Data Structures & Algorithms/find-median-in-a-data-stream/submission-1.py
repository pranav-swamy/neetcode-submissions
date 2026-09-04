import heapq
class MedianFinder:

    def __init__(self):
        self.minheap = list()
        self.maxheap = list()

    def addNum(self, num: int) -> None:
        if not self.maxheap:
            heapq.heappush(self.maxheap, -num)
            return
        
        if num <= abs(self.maxheap[0]):
            heapq.heappush(self.maxheap, -num)
        else:
            heapq.heappush(self.minheap, num)
        
        if len(self.maxheap) - len(self.minheap) > 1:
            heapq.heappush(self.minheap, -heapq.heappop(self.maxheap))
        
        if len(self.minheap) - len(self.maxheap) > 1:
            heapq.heappush(self.maxheap, -heapq.heappop(self.minheap))

    def findMedian(self) -> float:
        numelts = len(self.minheap) + len(self.maxheap)

        if numelts % 2 == 0:
            return (self.minheap[0] + (-self.maxheap[0])) / 2
        
        if len(self.minheap) > len(self.maxheap):
            return self.minheap[0]
        else:
            return -self.maxheap[0]
        
        