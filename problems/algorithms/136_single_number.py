from typing import List 

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0 
        for elt in nums:
            res ^= elt
        return res 