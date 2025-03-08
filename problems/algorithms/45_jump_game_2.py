from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        curr_idx = 0
        cpt = 0
        # While we don't have reach the end of nums
        while curr_idx < len(nums) - 1:
            # If we can already reach the last
            if curr_idx + nums[curr_idx] >= len(nums) - 1:
                return cpt + 1

            max_dist = 0 
            # We jump from the current cell to the one
            # that makes each reach the highest number 
            # of new cells
            best = 0
            for i in range(1, nums[curr_idx] + 1):
                if (curr_idx + i) < len(nums):
                    next_idx = curr_idx + i
                    dist = next_idx + nums[next_idx]
                    if dist > max_dist:
                        best = next_idx
                        max_dist = dist
            curr_idx = best
            cpt += 1
        return cpt