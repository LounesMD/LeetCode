from typing import List 

class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        ## Without the use of the extra space:
        # x + y = sum + Psum, (x - y)^2 = sum^2 - Psum^2
        res = [0,0]

        all_elt = [0] * (len(grid)*len(grid))
        for i in range(len(grid)):
            for j in range(len(grid)):
                all_elt[grid[i][j] - 1] += 1

        for i, elt in enumerate(all_elt):
            if elt == 0:
                res[1] = (i+1)
            elif elt == 2:
                res[0] = (i+1)

        return res 