from typing import List

class Solution:

    def waysToSplitArray(self, nums: List[int]) -> int:
        """
        O(n) and O(1)
        """
        if len(nums) == 0:
            return 0

        left_sum = 0
        right_sum = sum(nums)
        cpt = 0

        for i in range(0,len(nums) - 1):
            left_sum += nums[i]
            right_sum -= nums[i]

            if left_sum >= right_sum:
                cpt += 1

        return cpt

    def waysToSplitArray_(self, nums: List[int]) -> int:
        """
        O(n) and O(n)
        """
        if len(nums) == 0:
            return 0

        n = len(nums)
        left_sum = [0 for _ in range(n - 1)]
        left_sum[0] = nums[0]

        right_sum = [0 for i in range(n - 1)]
        right_sum[0] = nums[-1]

        for i in range(1,n-1):
            left_sum[i] += left_sum[i - 1] + nums[i]
            right_sum[i] += right_sum[i - 1] + nums[n - i - 1]

        cpt = 0
        for k in range(n - 1):
            if left_sum[k] >= right_sum[n - 2 - k]:
                cpt += 1

        return cpt