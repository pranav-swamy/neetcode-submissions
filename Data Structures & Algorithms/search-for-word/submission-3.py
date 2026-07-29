class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = [[False]*len(board[0]) for _ in range(len(board))]
        d = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        def valid(row, col):
            return 0 <= row < len(board) and 0 <= col < len(board[0])

        def backtrack(idx, row, col):
            if word[idx] == board[row][col]:
                if idx == len(word)-1:
                    return True
                
                visited[row][col] = True

                for dr, dc in d:
                    newr = row+dr
                    newc = col+dc
                    if valid(newr, newc) and not visited[newr][newc]:
                        if backtrack(idx+1, newr, newc):
                            return True
                
                visited[row][col] = False
            
            else:
                return False

            
            
            # if idx == len(word):
            #     return True

            # if word[idx] != board[row][col]:
            #     return False

            # visited[row][col] = True

            # for dr, dc in d:
            #     newr = row+dr
            #     newc = col+dc
            #     if valid(newr, newc) and not visited[newr][newc] and backtrack(idx+1, newr, newc):
            #         return True
            
            # visited[row][col] = False
            

        for row in range(len(board)):
            for col in range(len(board[0])):
                if backtrack(0, row, col):
                    return True
        
        return False