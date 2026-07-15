class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        dadj = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        visited = [[False]*len(board[0]) for _ in range(len(board))]
        
        def backtrack(row, col, word_index):
            visited[row][col] = True
            if board[row][col] != word[word_index]:
                # prune, this is not the answer
                visited[row][col] = False
                return False
            if board[row][col] == word[word_index]:
                if word_index == len(word)-1:
                    # soln found
                    return True
                # explore all 8 adjacent nodes
                for dr, dc in dadj:
                    newr = row + dr
                    newc = col + dc
                    if 0 <= newr < len(board) and 0 <= newc < len(board[0]) and not visited[newr][newc]:
                        # valid adj node
                        success = backtrack(newr, newc, word_index+1)
                        if success:
                            return True
            visited[row][col] = False


        for i in range(len(board)):
            for j in range(len(board[0])):
                # visited[i][j] = True
                if backtrack(i, j, 0):
                    return True
                # visited[i][j] = False
        
        return False
