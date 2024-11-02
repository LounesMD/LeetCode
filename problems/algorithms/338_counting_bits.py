from typing import List 

class Solution:

    def countBits(self, n: int) -> List[int]:
        res = [0]
        if n == 0:
            return res

        res.append(1)

        for i in range(2, n+1):
            if i%2 == 0:
                res.append(res[i//2])
            else:
                res.append(res[i//2] + 1)
        
        return res 


    def nb_bits(self, n: int) -> int:
        cpt = 0 
        while n > 0:
            cpt += n % 2
            n //= 2
        return cpt
        
    def countBits_nlogn(self, n: int) -> List[int]:
        """
        Complexity: 0(n) and O(nlog(n))
        """
        res = []
        for i in range(n+1):
            res.append(self.nb_bits(i))
        return res 