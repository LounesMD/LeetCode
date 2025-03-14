from typing import List 

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        l, r = 0, (len(matrix[0])*len(matrix)) - 1

        while l <= r:

            middle = (l+r) // 2
            middle_i, middle_j = middle//n, middle%n

            if matrix[middle_i][middle_j] == target:
                return True

            if matrix[middle_i][middle_j] < target:
                l = middle + 1    

            else:
                r = middle - 1

        return False 