from typing import List

class Solution:    
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        In this version we chase non zeroes instead of zeroes.
        """  
        swap_index = 0

        for i in range(len(nums)):
            if nums[i] != 0 and nums[swap_index] == 0:
                nums[i], nums[swap_index] = nums[swap_index], nums[i]

            if nums[swap_index] != 0:
                swap_index += 1 