class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        '''
        problem statement: given an m x n grid

        naive: for each land cell, use bfs until you find a treasure chest.
            * this quickly becomes a lot of overhead and repeated work

        solution: from each treasure chest, use bfs layers to update ONLY LAND cells
        '''

        rows = len(grid)
        cols = len(grid[0])

        inf = pow(2, 31) - 1

        queue = collections.deque()

        def bfs(i, j):
            queue.append((i, j, 0))
            dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]

            while queue:
                pi, pj, layer = queue.popleft()

                for di, dj in dirs:
                    ni, nj = pi + di, pj + dj

                    # changed from == inf to > layer + 1. a future bfs call may update the true distance
                    # and == inf doesn't allow updates. > 0 will end up making repeat calls to already set 
                    # distances
                    if ni in range(rows) and nj in range(cols) and grid[ni][nj] > layer + 1:
                        # found a land cell in bounds
                        grid[ni][nj] = min(grid[ni][nj], layer + 1)
                        queue.append((ni, nj, layer + 1))


        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    # found a treasure chest! use bfs now to update values of all land cells
                    bfs(i, j)
        
        return
