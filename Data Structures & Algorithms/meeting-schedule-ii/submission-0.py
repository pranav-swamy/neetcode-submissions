"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        minheap = []

        intervals.sort(key = lambda x: x.start)

        for intl in intervals:
            if not minheap:
                heapq.heappush(minheap, (intl.end, intl.start))
                continue
            
            earliest_end = minheap[0][0]
            current_start = intl.start

            if current_start < earliest_end:
                # they overlap, we need a new room
                heapq.heappush(minheap, (intl.end, intl.start))
            else:
                # meeting starts after the prev meeting ends
                # can use the same
                heapq.heappop(minheap)
                heapq.heappush(minheap, (intl.end, intl.start))
        
        return len(minheap)