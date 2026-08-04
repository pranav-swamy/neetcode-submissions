class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # multi source bfs approach
        # when we do a bfs simultaneously from all tresure cells,
        # it automatically allocates the lowest number to each land cell

        # to do a multi source bfs, use one queue
        # add all sources to the queue and start bfs

        visited = [[False]*len(grid[0]) for _ in range(len(grid))]
        queue = []
        d = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        def is_valid_next_cell(row, col):
            # within bounds
            # is a land cell
            # not visited
            withinBounds = 0 <= row < len(grid) and 0 <= col < len(grid[0])
            if not withinBounds:
                return False
            is_land = grid[row][col] == 2**31 - 1
            not_visited = visited[row][col] == False

            return withinBounds and is_land and not_visited
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 0:
                    queue.append((row, col))
        
        # bfs
        while queue:
            children = []
            for (row, col) in queue:
                # mark as visited
                # make all child nodes as val+1
                # add all child nodes

                visited[row][col] = True
                for (dx, dy) in d:
                    newr = row + dx
                    newc = col + dy
                    if is_valid_next_cell(newr, newc):
                        grid[newr][newc] = grid[row][col] + 1
                        children.append((newr, newc))
            
            queue = children
                


