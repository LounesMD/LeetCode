from typing import List 

class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        res = 0

        l, r = 1, max(candies)
        while l<=r:
            middle = (l+r)//2
            ct = sum([candie//middle for candie in candies])
            if ct >= k:
                l = middle + 1
            else:
                r = middle - 1
        return r