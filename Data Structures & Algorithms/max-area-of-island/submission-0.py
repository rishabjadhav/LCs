class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        '''
        problem statement: given a 2D array where 0 is water and 1 is land, return the maximum area of
        an island in grid
        
        solution: classic dfs/bfs.

            * iterate through grid till you find a 1
            * use dfs/bfs on the 1 and count the total number of 1s adjacent
            * store this area in a global var
            * return after done with grid

        notes:
            * how do i keep count of the area of an island? bfs is layer by layer, dfs is the natural choice?
            * recursion is much easier to use when counting total calls
        '''

        rows = len(grid)
        cols = len(grid[0])
        
        # holds tuples of already visited coords
        seen = set()

        stk = collections.deque()

        self.res = 0

        # recursive dfs helps us keep track of island cells
        def dfs(i, j):
            if i in range(rows) and j in range(cols) and (i, j) not in seen and grid[i][j] == 1:
                seen.add((i, j))

                # recursively call
                return 1 + dfs(i+1, j) + dfs(i, j+1) + dfs(i-1, j) + dfs(i, j-1)
            else:
                return 0
        
        for i in range(rows):
            for j in range(cols):
                self.res = max(self.res, dfs(i, j))
        
        return self.res
