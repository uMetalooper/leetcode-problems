from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        nRows = len(grid)
        nCols = len(grid[0])
        maxArea = 0
        
        def dfs(w, h, area=None):
            if area == None:
                area = 0
            if (
                w not in range(nCols)
                or h not in range(nRows)
                or (w, h) in visited
                or grid[h][w] == 0
            ):
                return area
            area += 1
            visited.add((w, h))
            d = [-1, 0, 1, 0, -1]
            for i in range(4):
                area = dfs(w+d[i], h+d[i+1], area)
            return area
        
        for h in range(nRows):
            for w in range(nCols):
                if (w, h) not in visited and grid[h][w] == 1:
                    area = dfs(w, h)
                    if area > maxArea:
                        maxArea = area
        return maxArea

grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,1,1,0,1,0,0,0,0,0,0,0,0],
        [0,1,0,0,1,1,0,0,1,0,1,0,0],
        [0,1,0,0,1,1,0,0,1,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,0,0,0,0,0,0,1,1,0,0,0,0]]
Solution().maxAreaOfIsland(grid)