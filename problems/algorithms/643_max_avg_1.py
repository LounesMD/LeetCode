class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """        
        prev_avg = sum(nums[:k])

        max_avg = prev_avg

        for i in range(1, len(nums) - k + 1):

            prev_avg = prev_avg - nums[i-1] + nums[i+k - 1]
            

            max_avg = max(max_avg, prev_avg)

        return float(max_avg) / k