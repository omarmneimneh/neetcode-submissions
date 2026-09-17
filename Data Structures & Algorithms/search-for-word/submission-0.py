class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()
        def dfs(i,j, idx):
            if idx == len(word):
                return True
            if i not in range(len(board)) or j not in range(len(board[i])) or board[i][j] != word[idx] or (i,j) in visited:
                return False
            visited.add((i,j))
            res = dfs(i+1, j, idx+1) or dfs(i-1, j, idx+1) or dfs(i, j+1, idx+1) or dfs(i, j-1, idx+1)
            visited.remove((i,j))
            return res
        for i in range(len(board)):
            for j in range(len(board[i])):
                if dfs(i, j, 0):
                    return True
        return False
