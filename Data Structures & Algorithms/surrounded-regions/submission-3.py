class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # start from Os in the border, dfs
        # mark all reachable Os as escapable
        # then mark the rest as X

        escapable = [[False for _ in range(len(board[0]))] for _ in range(len(board))]
        escape_points = set()

        for i in range(len(board)):
            for j in range(len(board[0])):
                if i == 0 or i == len(board)-1:
                    if board[i][j] == 'O':
                        escape_points.add((i, j))
                if j == 0 or j == len(board[0])-1:
                    if board[i][j] == 'O':
                        escape_points.add((i, j))
        
        # dfs from escape points
        # mark escapable points as visited
        d = [(-1, 0), (0, -1), (1, 0), (0, 1)]

        def is_valid(i, j):
            within_bounds = 0 <= i < len(board) and 0 <= j < len(board[0])
            if not within_bounds:
                return False
            
            is_O = board[i][j] == 'O'
            is_still_pending = escapable[i][j] == False
            return within_bounds and is_O and is_still_pending

        def dfs(i, j):
            if not is_valid(i, j):
                return
            
            escapable[i][j] = True
            
            for dx, dy in d:
                dfs(i + dx, j + dy)
        
        for x, y in escape_points:
            dfs(x, y)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O' and escapable[i][j] == False:
                    board[i][j] = 'X'
        
                



        