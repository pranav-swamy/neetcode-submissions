import heapq
class MedianFinder:

    def __init__(self):
        # keep a min heap and a max heap
        # add first elt to maxheap
        # then, for every new elt:
        # if > top of maxheap, add to minheap
        # else add to maxheap

        # if sie diff > 1,
        # rebalance heaps
        

        self.maxheap = list()
        self.minheap = list()
        

    def addNum(self, num: int) -> None:
        if not self.minheap:
            heapq.heappush(self.maxheap, -num)
        elif num > self.minheap[0]:
            heapq.heappush(self.minheap, num)
        else:
            heapq.heappush(self.maxheap, -num)
        
        if len(self.maxheap) > len(self.minheap):
            while len(self.maxheap) - len(self.minheap) > 1:
                val = heapq.heappop(self.maxheap)
                heapq.heappush(self.minheap, -val)
        
        if len(self.minheap) > len(self.maxheap):
            while len(self.minheap) - len(self.maxheap) > 1:
                val = heapq.heappop(self.minheap)
                heapq.heappush(self.maxheap, -val)
                
        
    def findMedian(self) -> float:
        if len(self.minheap) == len(self.maxheap):
            return (self.minheap[0] + -self.maxheap[0]) / 2
        elif len(self.minheap) > len(self.maxheap):
            return self.minheap[0]
        else:
            return -self.maxheap[0]
        
        
        