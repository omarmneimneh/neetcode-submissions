class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        visited = set()
        r, c = len(grid), len(grid[0])
        def flood(i, j):
            if (i not in range(r)
            or j not in range(c)
            or grid[i][j] == "0"
            or (i,j) in visited):
                return
            
            visited.add((i, j))
            directions = [[0, 1], [0, -1], [1,0], [-1, 0]]

            for dr, dc in directions:
                flood(i + dr,j + dc)
                
        for i in range(r):
            for j in range(c):
                if grid[i][j] == "1" and (i,j) not in visited:
                    res += 1
                    flood(i, j)
        return res