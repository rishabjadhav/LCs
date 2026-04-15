class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        seen = set()
        res = 0

        def bfs(i, j):
            dirs = [[0, 1],[0, -1],[-1, 0],[1, 0]]
            queue = collections.deque()

            queue.append((i, j))
            seen.add((i, j))

            while queue:
                pi, pj = queue.popleft()
                for di, dj in dirs:
                    ni = pi + di
                    nj = pj + dj

                    if ni in range(rows) and nj in range(cols) and grid[ni][nj] == "1" and (ni, nj) not in seen:
                        queue.append((ni, nj))
                        seen.add((ni, nj))


        for i in range(rows):
            for j in range(cols):
                print(f"looking at grid[{i}][{j}]")
                if grid[i][j] == "1" and (i, j) not in seen:
                    print(f"found island at grid[{i}][{j}]")
                    res += 1
                    bfs(i, j)
                    
                
        return res