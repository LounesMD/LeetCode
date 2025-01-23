from typing import List

class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        if n == 0:
            return 0
        res = 0 
        row = [0] * n
        column = [0] * m

        for i in range(n):
            for j in range(m):
                if grid[i][j]:
                    row[i] += 1
                    column[j] += 1

        for i in range(n):
            for j in range(m):
                if grid[i][j] and (row[i]>1 or column[j]>1):
                    res += 1 
        return res 