from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums)-1

        while l <= r:
            middle = (l+r)//2
            if nums[middle] == target:
                left, right = middle, middle
                while left>=0 and nums[left] == target:
                    left -= 1
                while right<len(nums) and nums[right] == target:
                    right += 1
                return [left+1, right-1]
            elif nums[middle] < target:
                l = middle + 1
            else:
                r = middle - 1
        return [-1,-1]