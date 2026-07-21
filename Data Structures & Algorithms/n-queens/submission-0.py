class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.' for k in range(n)] for _ in range(n)]
        soln = []

        def check_left_row(row, col):
            for i in range(0, col):
                if board[row][i] == 'Q':
                    return False
            return True
        
        def check_left_upper_diag(row, col):
            #print(row, col)
            while row >= 0 and col >= 0:
                if board[row][col] == 'Q':
                    return False
                row -= 1
                col -= 1
            return True

        
        def check_left_lower_diag(row, col):
            while row < n and col >= 0:
                if board[row][col] == 'Q':
                    return False
                row += 1
                col -= 1
            return True
        
        def backtrack(col):
            if col == n:
                # copy over
                soln.append([''.join(r[:]) for r in board])
                return
            
            for row in range(n):
                if check_left_row(row, col) and check_left_upper_diag(row, col) and check_left_lower_diag(row, col):
                    board[row][col] = 'Q'
                    backtrack(col+1)
                    board[row][col] = '.'
            
        backtrack(0)
        return soln