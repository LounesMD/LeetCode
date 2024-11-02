class Solution:
    def hammingWeight(self, n: int) -> int:
        cpt = 0
        while n > 0:
            cpt += n%2
            n //= 2 
        return cpt 