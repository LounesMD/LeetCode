class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # We look for i and j such that arr[i] - arr[j-1] = k
        # i.e. arr[i] = k - arr[j-1]
        res = 0
        t = {0: 1}

        curr_sum = 0

        for j in range(len(nums)):
            curr_sum += nums[j]

            look_for = curr_sum - k

            if look_for in t:
                res += t[look_for]
            if curr_sum in t:
                t[curr_sum] += 1
            else:
                t[curr_sum] = 1

        return res 
