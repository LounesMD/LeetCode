from typing import List

class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        n = len(nums)
        l = 0
        r = n
        pos, neg = 0, 0

        while l < r:
            middle = (l+r) // 2 # l + (r-l)/2
            if nums[middle] > 0:
                r = middle
            else:
                l = middle + 1
        pos = n - l

        l = 0
        r = n
        while l < r:
            middle = (l+r) // 2 # l + (r-l)/2
            if nums[middle] >= 0:
                r = middle
            else:
                l = middle + 1
        neg = l
        return max(neg, pos)

    def maximumCount0(self, nums: List[int]) -> int:
        neg = 0
        pos = 0 
        for elt in nums:
            if elt < 0:
                neg += 1
            elif elt > 0:
                pos += 1
        return max(pos, neg)