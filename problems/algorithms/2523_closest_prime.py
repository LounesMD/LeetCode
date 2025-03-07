from math import sqrt 
from typing import List

class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        all_primes = [True] * (right+1)
        all_primes[0] = False
        all_primes[1] = False
        for i in range(2,int(sqrt(right))+1):
            if all_primes[i]:
                for k in range(i**2, right+1, i):
                    all_primes[k] = False

        idx = [i for i in range(left, right+1) if all_primes[i]==True]

        if len(idx) < 2:
            return [-1,-1]
        res = [0,0]
        m_diff = float("inf")

        for k in range(1,len(idx)):
            if (idx[k] - idx[k-1]) < m_diff:
                m_diff = (idx[k] - idx[k-1])
                res = [idx[k-1], idx[k]]
        return res