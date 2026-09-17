class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0
        q = deque()
        time = 0

        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 1:
                    fresh +=1
                if grid[r][c] == 2:
                    q.append((r, c))
        
        directions = [[0,1], [0,-1], [1,0], [-1,0]]
        while fresh > 0 and q:
            time += 1
            for _ in range(len(q)):
                r,c = q.popleft()
                for dx, dy in directions:
                    x, y = r + dx, c + dy

                    if x in range(len(grid)) and y in range(len(grid[0])) and grid[x][y] == 1:
                        grid[x][y] = 2
                        fresh -= 1
                        q.append((x, y))
        return time if fresh == 0 else -1