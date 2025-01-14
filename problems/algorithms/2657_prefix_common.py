from typing import List 

class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        elt = [0] * n
        res = []
        cpt = 0
        for i in range(n):
            elt[A[i]-1] += 1
            if elt[A[i]-1] == 2:
                cpt +=1
            elt[B[i]-1] += 1
            if elt[B[i]-1] == 2:
                cpt += 1
            res.append(cpt)
        return res 