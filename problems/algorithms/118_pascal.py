from typing import List 

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        for i in range(1, numRows):
            next_e = [1]
            for k in range(1, len(res[-1])):
                next_e.append( sum(res[-1][k-1:k+1]))
            next_e.append(1)
            res.append(next_e)
        return res 
