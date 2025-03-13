from typing import List 

class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        sar = [0] * len(nums)

        for quer in queries:
            sar[quer[0]] += 1
            if (quer[1] + 1) < len(nums):
                sar[quer[1] + 1] -= 1
            
        if sar[0] < nums[0]:
            return False 
        for k in range(1, len(sar)):
            sar[k] += sar[k - 1]
            if sar[k] < nums[k]:
                return False

        return True