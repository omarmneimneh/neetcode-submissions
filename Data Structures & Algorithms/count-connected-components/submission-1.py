class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        visit = [False] * n
        for src, dest in edges:  
            graph[src].append(dest)
            graph[dest].append(src)
        def dfs(node):
            for nei in graph[node]:
                if not visit[nei]:
                    visit[nei] = True
                    dfs(nei)
            

        

        
        
        res = 0
        for i in range(n):
            if not visit[i]:
                visit[i] = True
                dfs(i)
                res += 1
        
        return res