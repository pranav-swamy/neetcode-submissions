class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        soln = []

        def backtrack(cur, numopen, numclose):
            if numclose > numopen or numopen > n:
                return

            if len(cur) == 2*n:
                soln.append(''.join(cur))
                return
            
            cur.append('(')
            backtrack(cur, numopen+1, numclose)
            cur.pop()

            cur.append(')')
            backtrack(cur, numopen, numclose+1)
            cur.pop()
        
        backtrack([], 0, 0)
        return soln