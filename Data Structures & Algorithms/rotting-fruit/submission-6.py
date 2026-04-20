class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        '''
        problem statement: return the minimum number of minutes needed until no fresh fruit remain, and -1 if 
        some fresh fruit will remain no matter what.

        solution: use BFS to go layer by layer from every rotten fruit. store a count of all fresh fruit, and after
        bfs concludes, remaining fresh fruit means return -1. bfs calls should store the "layer" in terms of minutes
        to store the running maximum.
        '''

        rows = len(grid)
        cols = len(grid[0])
        self.res = 0
        self.freshfruitremaining = 0

        q = collections.deque()

        def bfs():
            dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
            
            while q:
                xi, xj, time = q.popleft()
                self.res = max(self.res, time)

                for di, dj in dirs:
                    ni, nj = xi + di, xj + dj

                    if ni in range(rows) and nj in range(cols) and grid[ni][nj] == 1:
                        # rot!
                        q.append([ni, nj, time + 1])
                        self.freshfruitremaining -= 1
                        grid[ni][nj] = 2
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    self.freshfruitremaining += 1
                if grid[i][j] == 2:
                    q.append([i, j, 0])
        
        bfs()

        if self.freshfruitremaining > 0:
            return -1
        else:
            return self.res
                        
