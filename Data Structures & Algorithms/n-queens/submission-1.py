class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # if placing queens row-wise - only need to check top left diag, top right diag, upper vertical
        # if placing queens col-wise - only need to check top left diag, bottom left diag, left horizontal

        soln = []
        board = [['.' for _ in range(n)] for _ in range(n)]
        visited = [[False for _ in range(n)] for _ in range(n)]
        #print(visited)
        #print(board)

        def is_valid_placement(row, col):
            # top-left-diag
            i = row
            j = col
            while i >= 0 and j >= 0:
                if visited[i][j]:
                    return False
                i -= 1
                j -= 1

            # top-right-diag
            i = row
            j = col
            while i >= 0 and j < n:
                if visited[i][j]:
                    return False
                i -= 1
                j += 1

            # upper vertical
            i = row
            j = col
            while i >= 0:
                if visited[i][j]:
                    return False
                i -= 1
            
            return True
        
        # placing row-wise
        def backtrack(row):
            if row == n:
                # copy board over
                soln.append([''.join(ans_row[:]) for ans_row in board])
                return
            
            for col in range(n):
                if is_valid_placement(row, col):
                    visited[row][col] = True
                    board[row][col] = 'Q'
                    backtrack(row+1)
                    visited[row][col] = False
                    board[row][col] = '.'
        
        backtrack(0)
        return soln

