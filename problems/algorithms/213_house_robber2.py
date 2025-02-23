from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def rob(arr: List[int]) -> int:
            prev2, prev1 = 0, 0            
            for num in arr:
                temp = prev1
                prev1 = max(prev1, prev2 + num)
                prev2 = temp 

            return prev1
        
        return max(rob(nums[:-1]), rob(nums[1:]))
