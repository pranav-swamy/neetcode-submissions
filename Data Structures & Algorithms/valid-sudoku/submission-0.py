class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for col in range(len(board[0])):
            if not self.check_col(board, col):
                return False
        
        for row in range(len(board)):
            if not self.check_row(board, row):
                return False
        
        if not self.check_boxes(board):
            return False

        return True

    
    def check_col(self, board, col):
        seen = set()
        for row in range(len(board)):
            if board[row][col] != '.' and board[row][col] in seen:
                return False
            seen.add(board[row][col])
        return True
    
    def check_row(self, board, row):
        seen = set()
        for col in range(len(board[0])):
            if board[row][col] != '.' and board[row][col] in seen:
                return False
            seen.add(board[row][col])
        return True
    
    def check_boxes(self, board):
        seens = [set() for _ in range(9)]

        for row in range(len(board)):
            for col in range(len(board[0])):
                row_major_indexing = (row // 3) * 3 + (col // 3)
                # # of rows * # of columns in each row + # of columns
                # row * width + columns
                if board[row][col] != '.' and board[row][col] in seens[row_major_indexing]:
                    return False
                seens[row_major_indexing].add(board[row][col])
        return True
        


    

    


