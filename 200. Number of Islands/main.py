from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        Adj = dict()
        for i in range(m):
            for j in range(n):
                Adj[(i, j)] = []
        for p in Adj:
            directions = [-1, 0, 1, 0, -1]
            for k in range(4):
                _i = directions[k] + p[0]
                _j = directions[k+1] + p[1]
                if (0 <= _i < m) and (0 <= _j < n) and grid[_i][_j] == "1":
                    Adj[p].append((_i, _j))
                    
        def dfs(Adj, s, parent = None, order = None):
            if parent is None:
                parent = {v: None for v in Adj}
                parent[s] = s
                order = []
            for v in Adj[s]:
                if parent[v] is None:
                    parent[v] = s
                    dfs(Adj, v, parent, order)
            order.append(s)
            return parent, order

        def full_dfs(Adj):
            parent = {v:None for v in Adj}
            order = []
            count = 0
            for v in Adj:
                if parent[v] is None and grid[v[0]][v[1]]=="1":
                    parent[v] = v
                    p, o = dfs(Adj, v, parent, order)
                    count += 1
                    print(o)
            return order
        print(full_dfs(Adj))
        

if __name__ == "__main__":
    Solution().numIslands([["1","1","1","1","0"],
                           ["1","1","0","1","0"],
                           ["1","1","0","0","0"],
                           ["0","0","0","0","0"]])