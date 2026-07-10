import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # min heap
        # push k elts to the minheap
        # after that for each remaining elt,
        # pop the min elt and push the next one
        # what remains is the kth largest in the top of the heap

        self.heap = []
        self.max_size = k
        
        for num in nums:
            heapq.heappush(self.heap, num)
            if len(self.heap) > k:
                heapq.heappop(self.heap)
        

    def add(self, val: int) -> int:
        
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.max_size:
            heapq.heappop(self.heap)
        
        return self.heap[0]
        
