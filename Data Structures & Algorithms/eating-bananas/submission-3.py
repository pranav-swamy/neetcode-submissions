class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # find k - binary search for k
        # condition - run through array and eat k at a time <= h
        # lower bound = 1
        # upper bound = maximum size of all piles

        l = 1
        high = max(piles)

        while l < high:
            mid = l + (high-l)//2
            if self.canFinishEatingAllPilesWithinH(piles, mid, h):
                high = mid
            else:
                l = mid + 1
        
        return l
        

    def canFinishEatingAllPilesWithinH(self, piles, k, h):
        res = [math.ceil(x/k) for x in piles]
        #print("for k =", k, " ", res, " eating time = ", sum(res))
        #print(sum(res) <= h, h)
        return sum(res) <= h