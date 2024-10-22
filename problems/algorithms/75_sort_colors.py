from typing import List 

class Solution:
    def sortColors_0(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        Complexity: O(n) Time and O(1) Space
        """
        colors = {0: 0, 1: 0, 2: 0}

        for elt in nums:
            colors[elt] += 1 

        idx = 0
        for color in colors:
            nums[idx: idx+colors[color]] = [color] * colors[color]
            idx += colors[color]