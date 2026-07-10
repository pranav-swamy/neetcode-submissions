import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # need at least len(piles) hours
        # at most h hours

        # find k -
        # lower bound = 1
        # upper bound = max(piles)!!! because eating any more than that will be useless

        left = 1
        right = max(piles)

        while left < right:
            mid = left + (right - left) // 2
            
            if self.can_finish(piles, mid, h):
                right = mid
            else:
                left = mid + 1
            
        return left

    def can_finish(self, piles, mid, h):
        num_hours = 0
        for pile in piles:
            time = math.ceil(pile/mid)
            if time == 0:
                num_hours += 1
            else:
                num_hours += time
        print(num_hours)
        return num_hours <= h


        

