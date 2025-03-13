from typing import List

class Solution:
    def canJump0(self, nums: List[int]) -> bool:
        # Step 1: recursion done
        # Step 2: Memoization
        def dp_canJump(memo, idx):
            if idx in memo:
                return memo[idx]

            if idx >= len(nums) - 1:
                return True 

            res = False

            for i in range(1,nums[idx]+1):
                if dp_canJump(memo, idx+i):
                    res = True
                    break
            
            memo[idx] = res
            return res 

        return dp_canJump({},0)

    def canJump(self, nums):
        idx = len(nums) - 1

        for i in range(len(nums)-2, -1, -1):
            if i + nums[i] >= idx:
                idx = i
        return idx == 0