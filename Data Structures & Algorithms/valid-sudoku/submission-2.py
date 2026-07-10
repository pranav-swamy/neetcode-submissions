class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # check validity of rows
        # check validity of columns
        # check validity of boxes

        # at any point, if it is invalid, return False
        return self.areRowsValid(board) and self.areColsValid(board) and self.areBoxesValid(board)

    
    def areRowsValid(self, board):
        for row in board:
            seen = set()
            for num in row:
                if num in seen:
                    return False
                if num != '.':
                    seen.add(num)
        return True
    
    def areColsValid(self, board):
        for col in range(len(board[0])):
            seen = set()
            for row in range(len(board)):
                cell = board[row][col]
                if cell in seen:
                    return False
                if cell != ".":
                    seen.add(cell)
        return True
    
    def areBoxesValid(self, board):
        # use formula
        # box = row * number of cols + col
        seens = [set() for _ in range(9)]
        for row in range(0, len(board)):
            for col in range(0, len(board[0])):
                box = (row // 3) * 3 + (col // 3)
                cell = board[row][col]
                if cell in seens[box]:
                    return False
                if cell != '.':
                    seens[box].add(cell)
        return True
                

                
                    
        