class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set) 
        cols = defaultdict(set)
        squares = defaultdict(set)


        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                if board[r][c] not in rows[r] and board[r][c] not in cols[c] and board[r][c] not in  squares[(r//3, c//3)]:
                    rows[r].add(board[r][c])
                    cols[c].add(board[r][c])
                    squares[(r//3, c//3)].add(board[r][c])
                else:
                    return False
        return True