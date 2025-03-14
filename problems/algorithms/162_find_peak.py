from typing import List 

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l<r:
            middle = (l+r)//2
            if nums[middle] > nums[middle +1]:
                r = middle
            else:
                l = middle + 1 
        return l