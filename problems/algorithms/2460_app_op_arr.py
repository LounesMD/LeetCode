from typing import List 

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n - 1):
            if nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i + 1] = 0

        cn = 0
        for i in range(n):
            if nums[i] != 0:
                nums[cn] = nums[i]
                cn += 1
        for ci in range(cn, n):
            nums[ci] = 0
        return nums
        i = 0
        while i < n:            
            if nums[i] == 0:
                j = i+1
                while j < n and nums[j] == 0:
                    j += 1
                if j<n:
                    nums[i], nums[j] = nums[j], nums[i]
            i += 1
        return nums