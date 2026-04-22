class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        '''
        problem statement: given an m x n grid

        naive: for each land cell, use bfs until you find a treasure chest.
            * this quickly becomes a lot of overhead and repeated work

        solution: from each treasure chest, use bfs layers to update ONLY LAND cells
            * use MULTI-SOURCE BFS, meaning add all treasure chests to queue, THEN and only THEN,
            run BFS to avoid repeated work
            * multi-source guarantees correctness, as BFS travels in layers.
        '''

        rows = len(grid)
        cols = len(grid[0])

        inf = pow(2, 31) - 1

        queue = deque()

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    # found a treasure chest! put in queue for multi-source BFS after all chests discovered
                    queue.append((i, j))

        
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        while queue:
            i, j = queue.popleft()

            for di, dj in dirs:
                ni, nj = i + di, j + dj

                # we don't have to worry about updating values more than once.
                if ni in range(rows) and nj in range(cols) and grid[ni][nj] == inf:
                    # found a land cell in bounds that can be updated.
                    grid[ni][nj] = grid[i][j] + 1
                    queue.append((ni, nj))

        return
