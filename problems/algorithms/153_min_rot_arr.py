from typing import List 

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            middle = (l + r) // 2

            if nums[middle] >= nums[r]:
                l = middle + 1
            
            else:
                r = middle

        return nums[middle]