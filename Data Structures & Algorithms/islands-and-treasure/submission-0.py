class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()
        visited = set()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    q.append((r, c))
                    visited.add((r, c))
        directions = [[0,1], [0,-1], [1,0], [-1,0]]

        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dx, dy in directions:
                    x, y = r + dx, c + dy
                    if x in range(len(grid)) and y in range(len(grid[x])) and grid[x][y] != -1 and (x, y) not in visited:
                        grid[x][y] = min(grid[r][c] + 1, grid[x][y])
                        q.append((x,y))
                        visited.add((x,y))
        return grid