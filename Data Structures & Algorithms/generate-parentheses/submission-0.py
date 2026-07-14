class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # explore both ( and ) in the dfs tree,
        # when the count of ) exceeds (, then it is invalid
        # discard that path and continue exploring other paths
        # when length = 2n, add to result set

        soln = []


        def backtrack(current, openb, closeb):
            if closeb > openb or openb > n or closeb > n:
                # invalid
                return
            if len(current) == 2*n:
                soln.append(current[:])
            
            current.append('(')
            backtrack(current, openb+1, closeb)
            current.pop()

            current.append(')')
            backtrack(current, openb, closeb+1)
            current.pop()
        
        backtrack([], 0, 0)
        return [''.join(x) for x in soln]
            
