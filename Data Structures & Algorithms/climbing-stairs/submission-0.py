class Solution:
    def climbStairs(self, n: int) -> int:
        # climb 1 or 2 steps at a time
        # ways_to_climb(step n)
        # = ways_to_climb(step n-1)
        # + ways_to_climb(step n-2)
        # since you can reach step n in one go from 
        # either step n-1 or step n-2

        ways_to_climb = [0]*(n+1)
        ways_to_climb[0] = 1
        ways_to_climb[1] = 1

        for i in range(2, n+1):
            ways_to_climb[i] = ways_to_climb[i-1] + ways_to_climb[i-2]
        
        return ways_to_climb[n]