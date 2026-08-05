class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # multi source bfs
        # add all rotten fruit to queue
        # count fresh fruit
        # when marking every fruit as rotten, count down
        # if count is 0, success, else -1

        queue = []
        visited = set()
        fresh = 0
        d = [(-1, 0), (0, -1), (1, 0), (0, 1)]

        def is_valid_cell(row, col):
            within_bounds =  0 <= row < len(grid) and 0 <= col < len(grid[0])
            if not within_bounds:
                return False
            
            not_visited = (row, col) not in visited
            fresh_fruit = grid[row][col] == 1
            return within_bounds and not_visited and fresh_fruit

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    fresh += 1
                if grid[row][col] == 2:    
                    queue.append((row, col))
    
        minutes = 0
        while queue:
            children = []
            for (row, col) in queue:
                for (dx, dy) in d:
                    newr = row + dx
                    newc = col + dy
                    if is_valid_cell(newr, newc):
                        visited.add((newr, newc))
                        fresh -= 1
                        children.append((newr, newc))
            if children:
                minutes += 1
            queue = children
        
        return -1 if fresh != 0 else minutes
        