from typing import List 

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        max_i, max_j = len(matrix), len(matrix[0])
        res = []
        i, j = 0, -1
        d = 1 
        while max_i>0 and max_j>0:
            for _ in range(max_j):
                j += d 
                res.append(matrix[i][j])
            max_i -= 1 
        
            for _ in range(max_i):
                i += d
                res.append(matrix[i][j])
            max_j -= 1

            d *= -1

        return res 