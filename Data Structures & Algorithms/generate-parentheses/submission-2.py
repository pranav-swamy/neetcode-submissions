class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # when len == 2n, collect and return
        # at each node, check if numopen > numclosed

        soln = []
        cur = []

        def backtrack(num_open, num_closed):
            if num_open < num_closed or len(cur) > 2*n:
                # invalid
                return
            if num_open == num_closed and len(cur) == 2*n:
                soln.append(''.join(cur[:]))
            
            cur.append("(")
            backtrack(num_open+1, num_closed)
            cur.pop()

            cur.append(")")
            backtrack(num_open, num_closed+1)
            cur.pop()
        
        backtrack(0, 0)
        return soln