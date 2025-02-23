from typing import List 

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        res = [0] * len(nums)
        
        res[0] = nums[0]
        res[1] = max(nums[0], nums[1])
        
        for i in range(2, len(nums)):
            res[i] = max(res[i-1], nums[i] + res[i-2])
        
        return res[-1] 
