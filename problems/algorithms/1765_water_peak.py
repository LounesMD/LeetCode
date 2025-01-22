from typing import List 
from queue import deque

class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        r, c = len(isWater), len(isWater[0])
        w_grid = [[-1] * c for _ in range(r)]
        queue = deque()

        for i in range(r):
            for j in range(c):
                if isWater[i][j] == 1:
                    w_grid[i][j] = 0
                    queue.append((i, j))

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while queue:
            x, y = queue.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < r and 0 <= ny < c and w_grid[nx][ny] == -1:
                    w_grid[nx][ny] = w_grid[x][y] + 1
                    queue.append((nx, ny))

        return w_grid