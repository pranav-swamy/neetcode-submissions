class Solution:
    def countSubstrings(self, s: str) -> int:
        ispali = [[False]* len(s) for _ in range(len(s))]

        count = 0

        for i in range(len(s) - 1, -1, -1):
            for j in range(i, len(s)):
                if j - i + 1 <= 2 and s[i] == s[j]: # diagonals and 2 char strings that don't depend on a previos subproblem
                    count += 1
                    ispali[i][j] = True
                elif ispali[i+1][j-1] and s[i] == s[j]: # all problems that depend on a previos subproblem below it.
                    count += 1
                    ispali[i][j] = True
        
        return count