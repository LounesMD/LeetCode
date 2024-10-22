from typing import List 

class Solution:
    """
    Solution based on the flood fill technique.
    """
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def change_color(x: int,y: int , grid: List[List[str]]):
            if 0<=x<len(grid) and 0<=y<len(grid[0]) and grid[x][y] == "1":
                grid[x][y] = "2"
                change_color(x+1,y, grid)
                change_color(x, y+1, grid)
                change_color(x-1, y, grid)
                change_color(x, y-1, grid)


        nb_island = 0 

        for x in range(len(grid)):

            for y in range(len(grid[x])):

                if grid[x][y] == "1":
                    nb_island += 1
                    change_color(x,y, grid)

        return nb_island