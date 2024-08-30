from typing import List 

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        length = len(matrix)
        for i in range(length):
            for j in range(length - i):
                matrix[i][j], matrix[length - 1 - j][length - 1 - i] = matrix[length - 1 - j][length - 1 - i], matrix[i][j]

        # We split in order to get the right line order
        for i in range(len(matrix) // 2):
            matrix[i],matrix[(len(matrix) - i - 1)] = matrix[(len(matrix) - i - 1)], matrix[i]

        return matrix

sol = Solution()
mat = [[5,1,9,11],
       [2,4,8,10],
       [13,3,6,7],
       [15,14,12,16]]

# mat = [[1, 2, 3],
#        [4, 5, 6],
#        [7, 8, 9]]

        
# sol.rotate(mat)        
print("res: ", sol.rotate(mat)   )