class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS = len(board)
        COLS = len(board[0])
        def dfs(r, c):
            if r not in range(ROWS) or c not in range(COLS) or board[r][c] != 'O':
                return
            
            board[r][c] = "T"
            directions = [[0,1], [0,-1], [1,0], [-1,0]]
            
            for dx, dy in directions:
                x = r + dx
                y = c + dy
                dfs(x,y)

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == "O" and (r in [0, ROWS-1] or c in [0, COLS-1]):
                    dfs(r,c)
        print(board)
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
        print(board)
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "T":
                    board[r][c] = "O"
        
            