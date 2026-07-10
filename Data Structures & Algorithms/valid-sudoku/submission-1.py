class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # one set per row, per col, and per square

        rows = [set() for _ in range(len(board))]
        cols = [set() for _ in range(len(board[0]))]
        squares = [set() for _ in range(9)]

        for row in range(len(board)):
            for col in range(len(board[0])):
                val = board[row][col]
                if val != '.':
                    if val in rows[row] or val in cols[col] or val in squares[(row//3)*3 + (col//3)]:
                        return False
                    rows[row].add(val)
                    cols[col].add(val)
                    squares[(row//3)*3 + (col//3)].add(val)
        return True
