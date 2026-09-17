class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        r, c = len(grid), len(grid[0])

        def dfs(i, j):
            if i not in range(r) or j not in range(c) or  grid[i][j] == 0:
                return 0
            
            grid[i][j] = 0
            curr = 1
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for dr, dc in directions:
                curr += dfs(i+dr, j+dc)
            return curr
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1:
                    res = max(res, dfs(i, j))
        return res