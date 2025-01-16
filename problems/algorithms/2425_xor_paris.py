from typing import List

class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        n, m = len(nums1), len(nums2)
        x1, x2 = 0, 0

        if m % 2 != 0:
            for elt in nums1:
                x1 ^= elt

        if n % 2 != 0:
            for elt in nums2:
                x2 ^= elt        

        return x1 ^x2